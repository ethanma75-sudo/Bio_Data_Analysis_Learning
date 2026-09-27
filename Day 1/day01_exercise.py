import numpy as np

protein_data = np.loadtxt("protein_data.csv", delimiter=",")
print(protein_data)

print(protein_data[1])

print(protein_data[:, 2])

print(protein_data[1:, 1:3])

print(protein_data[0, 3])