def FactR(x):
    if x == 1:
        return x
    else:
        return x * FactR(x-1)

print(FactR(5))