def alex(vector, degree,increasing = True):
    overall = []
    n = len(vector)
    for i in range (n):
        row = []
        if increasing == True:
            for j in range(degree+1):
                row.append(vector[i]**j)
            overall.append(row)
        if increasing == False:
            for j in range(degree+1)[::-1]:
                row.append(vector[i]**j)
            overall.append(row)
    return overall

print(alex([1,2,3,4],4,False))
print(alex([1,2,3,4],4,True))
            
