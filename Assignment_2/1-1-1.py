def myreduce(func,iterable):
    for i in range(len(iterable)-1):
        if i==0:
            x=func(iterable[i],iterable[i+1])
        else:
            x=func(x,iterable[i+1])
    return x

def add(x,y):
    return x+y

myreduce(add,[1,2,3,4])
