import numpy as np

# read numpy array from file
d = np.load('/home/bnair/SEAM/outcam/0014716_007.npy', allow_pickle=True).item()
print(d)