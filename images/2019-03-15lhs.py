import numpy as np
import matplotlib.pyplot as plt

#makes a Latin Hyper Cube sample
#returns a matrix X of size n by p
#of a LHS of n values on each of p variables
#for each column of X, the n values are randomly distributed with one from each interval
# (0,1/n), (1/n,2/n), ... (1-1/n,1)
#and they are randomly permuted

def lhssample(n=10,p=2):
    x = np.random.uniform(size=[n,p])
    for i in range(0,p):
        x[:,i] = (np.argsort(x[:,i])+0.5)/n
    return x

x = lhssample(20,2)
# print(x)

fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
n = len(x)
ax.set_xticks(np.arange(0, 1+1/n, step=1/n))
ax.set_yticks(np.arange(0, 1+1/n, step=1/n))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(axis="both", direction="in", which="both", right=True, top=True, labelsize=10 , width=1.5)
ax.spines["left"].set_linewidth(1.5)
ax.spines["top"].set_linewidth(1.5)
ax.spines["right"].set_linewidth(1.5)
ax.spines["bottom"].set_linewidth(1.5)
ax.scatter(x[:,0],x[:,1])
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.grid(linewidth=1.5)
plt.savefig('lhs.png',dpi=600)

# fig = plt.figure(figsize=(3,3))
# ax = fig.add_subplot(111, projection='3d')
# n = len(x)
# # ax.set_xticks(np.arange(0, 1+1/n, step=1/n))
# # ax.set_yticks(np.arange(0, 1+1/n, step=1/n))
# # ax.set_zticks(np.arange(0, 1+1/n, step=1/n))
# ax.set_xticklabels([])
# ax.set_yticklabels([])
# ax.set_zticklabels([])
# ax.tick_params(axis="both", direction="in", which="both", right=True, top=True, labelsize=10 , width=1.5)
# ax.spines["left"].set_linewidth(1.5)
# ax.spines["top"].set_linewidth(1.5)
# ax.spines["right"].set_linewidth(1.5)
# ax.spines["bottom"].set_linewidth(1.5)
# ax.scatter(x[:,0],x[:,1],x[:,2], marker='.')
# ax.set_xlim(0,1)
# ax.set_ylim(0,1)
# ax.set_zlim(0,1)
# ax.grid(linewidth=1.5)
# plt.savefig('lhs.png',dpi=600)
