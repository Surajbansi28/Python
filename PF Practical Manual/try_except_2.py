value = [1,2,3,4]
data = 0
try:
    data = value[3]
except IndexError:
    print("CSIT Index Error",end='' '\n')
except:
    print("NEDUET Index Error",end='' '\n')
finally:
    print("Python Index Error", end='' '\n')

data = 10
try: 
    data = data/0
except ZeroDivisionError:
    print("CSIT ZeroDivisionError",end='' '\n')
finally:
    print("Python ZeroDivisionError")



