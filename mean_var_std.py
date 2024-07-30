import numpy as np
#Eg input 
#[0 1 2
#3 4 5
#6 7 8]

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(list).reshape(3,3)
        #calculate mean on axis 1 n axis 2
        ax1_mean = np.mean(matrix, axis= 0).tolist() #col
        ax2_mean = np.mean(matrix, axis= 1).tolist() #row
        flat_mean = np.mean(matrix)

        #calculate variance on axis 1 n 2
        ax1_var = np.var(matrix, axis= 0).tolist()
        ax2_var = np.var(matrix, axis= 1).tolist()
        flat_var = np.var(matrix)

        #calculate standard deviation
        ax1_std = np.std(matrix, axis= 0).tolist()
        ax2_std = np.std(matrix, axis= 1).tolist()
        flat_std = np.std(matrix)

        #calculate max 
        ax1_max = np.max(matrix, 0).tolist()
        ax2_max = np.max(matrix, 1).tolist()
        flat_max = np.max(matrix)

        #calculate min 
        ax1_min = np.min(matrix, 0).tolist()
        ax2_min = np.min(matrix, 1).tolist()
        flat_min = np.min(matrix)

        #calculate sum 
        ax1_sum = np.sum(matrix, 0).tolist()
        ax2_sum = np.sum(matrix, 1).tolist()
        flat_sum = np.sum(matrix)

        #creating dictionaries for output format as mentioned
        calculations = {
        'mean': [ax1_mean, ax2_mean, flat_mean],
        'variance': [ax1_var, ax2_var, flat_var],
        'standard deviation': [ax1_std, ax2_std, flat_std],
        'max': [ax1_max, ax2_max, flat_max],
        'min': [ax1_min, ax2_min, flat_min],
        'sum': [ax1_sum, ax2_sum, flat_sum]
        }

    return calculations