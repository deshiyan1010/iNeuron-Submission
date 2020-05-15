def myfilter(func,iterable):
    lst = []
    for i in range(len(iterable)):
        if func(iterable[i])==0:
            pass
        else:
            lst.append(iterable[i])
    return lst

myfilter(lambda x:x>2,[1,2,3,4])
