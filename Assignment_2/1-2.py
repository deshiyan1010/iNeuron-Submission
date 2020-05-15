lst = [x for x in "ACADGILD"]
print(lst)

lst = [i*x for x in "xyz" for i in range(1,4)  ]
print(lst)

lst = [i*x for i in range(1,4) for x in "xyz"  ]
print(lst)

lst = [[x+i] for i in range(3) for x in range(2,5) ]
print(lst)

lst = [[x+i for i in range(4)] for x in range(2,6) ]
print(lst)

lst = [(x,y) for y in range(1,4) for x in range(1,4) ]
print(lst)
