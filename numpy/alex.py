import numpy as np

def alex(vector,degree,increasing=True):
    overall = []
    n = len(vector)
    vector = np.array(vector)

    for i in range(n):
        overall.append(np.power(vector,i))
    if increasing==False:
        overall = np.fliplr(overall)
    return np.array(overall)

print(alex([1,2,3,4],4,False))
print(alex([1,2,3,4],4,True))
            
