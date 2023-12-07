def bank(X, Y):
    for i in range(Y):
        X += X * 0.10
    return X

X = 1000 
Y = 5  
result = bank(X, Y)
print(result) 