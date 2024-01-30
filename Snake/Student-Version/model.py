import torch
import torch.nn as nn

#QNetwork is our main model in this problem
class QNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(QNetwork, self).__init__()
        #four initial linear layers for our prediction representation
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, hidden_dim)
        self.fc4 = nn.Linear(hidden_dim, output_dim)
        #this is how we model our last outputs with relu layer
        self.relu = nn.ReLU()

    def forward(self, x):
        #this is the main rule for model the problems! we will give our linear layers to relu function(or sigmoid) for better modeling \
        # and representation of our model
        l1 = self.relu(self.fc1(x.float()))
        l2 = self.relu(self.fc2(l1))
        l3 = self.relu(self.fc3(l2))
        l4 = self.fc4(l3)
        return l4

#this get network function will give us the initial of current state of apples and snakes
def get_network_input(player, apple):
    proximity = player.get_proximity()
    x = torch.cat([torch.from_numpy(player.pos).double(), torch.from_numpy(apple.pos).double(),
                   torch.from_numpy(player.dir).double(), torch.tensor(proximity).double()])
    return x
