import numpy as np

def moving_avg_numpy(vector,win_size):

    final = []
    for x in range(len(vector)-win_size+1):
        avg = np.sum(vector[x:x+win_size])/win_size
        final.append(avg)
    return final


print(moving_avg_numpy([1,2],2))
