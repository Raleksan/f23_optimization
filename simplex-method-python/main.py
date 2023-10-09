import numpy as np
import itertools as itls
import math

# Disable 'divide by zero' warning
np.seterr(divide='ignore')  

# Welcoming
print("### Welcome to Simplex method programm *_* ")

# Read input values
print("### Is your linear program about maximization?")
maximization = bool(int(input("### If yes, print 1, else print 0: ")))

temp_str = str(input("### Write a vector of coefficients of objective function: \n"))
A = np.array(list(map(float, temp_str.split())), np.float64)

a, b = map(int, input("### Write size of the matrix m and n: ").split())
print("### Write a matrix of coefficients of constraint function: ")

arr = []
for _ in range(a):
    temp_str = str(input())
    arr.append(list(map(float, temp_str.split())))

C = np.array(arr, np.float64)

temp_str = str(input("### Write a vector of right-hand side numbers: \n"))
b = np.array(list(map(float, temp_str.split())), np.float64)

approx = float(input("### Write approximation accuracy: "))

# Save shape of array 
n, m = C.shape

# Step 0
# Find basic feasible solution

# Iterate over all possible variance of 
# basic and non-basic variables (vectors)
for seq in itls.permutations(((m - n) * [0] + n * [1]), m):

    # Generate index sequence for array shaping
    basic_seq = [i for i in range(0, len(seq)) if seq[i] == 1]
    non_basic_seq = [i for i in range(0, len(seq)) if seq[i] == 0]

    # Check linear dependency 
    # using eigenvalue decomposition 
    lambdas, V = np.linalg.eig(C[:, basic_seq].T)
    
    # If vectors are linear dependent,
    # trying to find other
    # else start simplex algorithm 
    if len(C[:, basic_seq][lambdas == 0, :]) != 0 :
        continue
    else:
        break 

while True:
    
    # Step 1 & 2
    # Compute inverse and z - c
    # Check optimality of the solution

    # Count X_b
    X_b = np.linalg.inv(C[:, basic_seq]) @ b

    # Count z - c        
    Z_c = A[basic_seq] @ np.linalg.inv(C[:, basic_seq]) \
            @ C[:, non_basic_seq] - A[non_basic_seq]

    # Count z
    z = A[basic_seq] @ X_b

    # Cheking optimality of the solution

    # Maximization optimal
    if (maximization and all(i > 0 for i in Z_c)):
        print("### Maximum achived ###")
        break

    # Minimazation optimal
    elif (not maximization and all(i <= 0 for i in Z_c)):
        print("### Minimum achived ###")
        break
        
    # Min/Max not optimal
    else:

        # Determine entering variable (vector)
        enter_var_ind = 0
        if maximization:
            enter_var_ind = np.argmin(Z_c)
        else: 
            enter_var_ind = np.argmax(Z_c)


        # Step 3
        # Check solition bound
        # Determine leaving variable (vector)

        # Count B_p
        B_p = np.linalg.inv(C[:, basic_seq]) @ C[:, enter_var_ind]

        # Check solution bound
        if all(i <= 0 for i in B_p):
            print("### Solution is unbounded ###")
            print("### Exit from programm ###")
            exit()

        # Compute slope cooficient
        k = np.divide(X_b, B_p)
        k = [i if (i >= 0 and i != float('inf')) else float('inf') for i in k]

        # Determine leaving value
        leaving_var_ind = np.argmin(k)


        # Step 4
        # Form new basis

        # Update state of the basic and non-basic vectors
        non_basic_seq[enter_var_ind], basic_seq[leaving_var_ind] \
            = basic_seq[leaving_var_ind], non_basic_seq[enter_var_ind]


# Answer output
print()
print("######################################")
print("### ANSWER                         ###")
print("### Vector of decision variables   ###")
print("### X is", X_b)
print("### Z is", math.ceil(z))
print("### Programm finished successfully ###")
print("######################################")
