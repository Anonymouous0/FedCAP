import torch
import numpy as np
import copy
from flcore.clients.clientbase import Client
from torch.utils.data import DataLoader
from utils.data_utils import read_client_data


class clientFomo(Client):
    def __init__(self, args, id, malicious, **kwargs):
        super().__init__(args, id, malicious, **kwargs)
        
        self.val_ratio = 0.2
        self.old_model = copy.deepcopy(self.model)
        self.received_ids = []
        self.received_models = []

    def train(self):
        trainloader, _ = self.load_train_data()

        self.model.train()
        
        max_local_steps = self.local_steps

        for step in range(max_local_steps):
            for x, y in trainloader:
                if type(x) == type([]):
                    x[0] = x[0].to(self.device)
                else:
                    x = x.to(self.device)
                y = y.to(self.device)
                self.optimizer.zero_grad()
                output = self.model(x)
                loss = self.loss(output, y)
                loss.backward()
                self.optimizer.step()

        if self.learning_rate_decay:
            self.learning_rate_scheduler.step()

    def load_train_data(self, batch_size=None):
        if batch_size == None:
            batch_size = self.batch_size
        train_data = read_client_data(self.dataset, self.data_path, self.id, is_train=True)
        val_idx = -int(self.val_ratio*len(train_data))
        val_data = train_data[val_idx:]
        train_data = train_data[:val_idx]
        # label flipping attack
        if self.malicious and self.attack_type == 'A1':
            for idx in range(len(train_data)):
                train_data[idx][1] = self.num_classes - train_data[idx][1] - 1
        
        trainloader = DataLoader(train_data, self.batch_size, drop_last=True, shuffle=False)
        val_loader = DataLoader(val_data, self.batch_size, drop_last=self.has_BatchNorm, shuffle=False)

        return trainloader, val_loader


    def train_metrics(self):
        trainloader, _ = self.load_train_data()
        
        self.model.eval()

        train_num = 0
        loss = 0
        for x, y in trainloader:
            if type(x) == type([]):
                x[0] = x[0].to(self.device)
            else:
                x = x.to(self.device)
            y = y.to(self.device)
            output = self.model(x)
            train_num += y.shape[0]
            loss += self.loss(output, y).item() * y.shape[0]

        return loss, train_num
    
    def train_metrics_personalized(self):
        trainloader, _ = self.load_train_data()

        self.model.eval()

        train_num = 0
        losses = 0
        with torch.no_grad():
            for x, y in trainloader:
                if type(x) == type([]):
                    x[0] = x[0].to(self.device)
                else:
                    x = x.to(self.device)
                y = y.to(self.device)
                output = self.model(x)
                loss = self.loss(output, y)
                train_num += y.shape[0]
                losses += loss.item() * y.shape[0]

        return losses, train_num
    
    def receive_models(self, ids, models):
        self.received_ids = ids
        self.received_models = models

    def weight_cal(self, val_loader):
        weight_list = []
        if len(self.received_models) != 0:
            L = self.recalculate_loss(self.old_model, val_loader)
            for received_model in self.received_models:
                params_dif = []
                for param_n, param_i in zip(received_model.parameters(), self.old_model.parameters()):
                    params_dif.append((param_n - param_i).view(-1))
                params_dif = torch.cat(params_dif)

                weight_list.append((L - self.recalculate_loss(received_model, val_loader)) / (torch.norm(params_dif) + 1e-9))

        self.weight_vector_update(weight_list)

        return torch.tensor(weight_list)
        

    def weight_vector_update(self, weight_list):
        self.weight_vector = np.zeros(self.weight_vector.shape[0])
        for w, id in zip(weight_list, self.received_ids):
            self.weight_vector[id] += w.item()
        self.weight_vector = torch.tensor(self.weight_vector).to(self.device)

    def recalculate_loss(self, model, val_loader):
        L = 0
        for x, y in val_loader:
            if type(x) == type([]):
                x[0] = x[0].to(self.device)
            else:
                x = x.to(self.device)
            y = y.to(self.device)
            output = model(x)
            loss = self.loss(output, y)
            L += loss.item()
        
        return L / len(val_loader)

    def add_parameters(self, w, received_model):
        for param, received_param in zip(self.model.parameters(), received_model.parameters()):
            param.data += received_param.data.clone() * w
        
    def aggregate_parameters(self, val_loader):
        weights = self.weight_scale(self.weight_cal(val_loader))

        if len(weights) > 0:
            for param in self.model.parameters():
                param.data.zero_()

            for w, received_model in zip(weights, self.received_models):
                self.add_parameters(w, received_model)
        return weights
    
    def weight_scale(self, weights):
        weights = torch.maximum(weights, torch.tensor(0))
        w_sum = torch.sum(weights)
        if w_sum > 0:
            weights = [w/w_sum for w in weights]
            return torch.tensor(weights)
        else:
            return torch.tensor([])
