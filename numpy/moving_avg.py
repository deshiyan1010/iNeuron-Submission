import numpy as np

def moving_avg_numpy(vector,win_size):

    final = []
    for x in range(len(vector)-win_size+1):
        avg = np.sum(vector[x:x+win_size])/win_size
        final.append(avg)
    return final


print(moving_avg_numpy([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150],3))
print(moving_avg_numpy([10,20,30,40,50,60,70,80,90,100],4))
