import torch
torch.manual_seed(1)

## Creating Tensors

V_data = [1.,2.,3.]
V = torch.tensor(V_data)
print(V)

# Create a matrix
M_data = [[1.,2.,3.], [4.,5.,6.]]
M = torch.tensor(M_data)
print(M)


# Create a 3D tensor of size 2x2x2
T_data = [[[1.,2.],[3.,4.]],
        [[5.,6.],[7.,8.]]]
T = torch.tensor(T_data)
print(T)
