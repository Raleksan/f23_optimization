import numpy as np
import itertools as itls

approx = 0.001

C = np.array([
    [6,  4, 1, 0, 0, 0],
    [1,  2, 0, 1, 0, 0],
    [-1, 1, 0 ,0, 1, 0],
    [0,  1, 0, 0, 0, 1]
])

A = np.array([
    5, 4, 0, 0, 0, 0
])

b = np.array([
    24, 6, 1, 2
])

# Save shape of array 
n, m = C.shape

# Find basic feasible solution
for seq in itls.permutations(((m - n) * [0] + n * [1]), m):

    # Generate index sequence for array shaping
    true_seq = [i for i in range(0, len(seq)) if seq[i] == 1]
    anti_seq = [i for i in range(0, len(seq)) if seq[i] == 0]

    A_tmp = A[true_seq]
    C_tmp = C[:, true_seq]

    # Check linear dependency
    lambdas, V = np.linalg.eig(C_tmp.T)
    # print(C_tmp[lambdas == 0, :])
    if len(C_tmp[lambdas == 0, :]) != 0 :
        continue
    else:
        X_b = C_tmp @ b # np.transpose may be needed
        # z = A_tmp @ X_b
        
        Z_c = A_tmp @ C_tmp @ C[:, anti_seq] - A[anti_seq]
        
        exit()



print("endd")