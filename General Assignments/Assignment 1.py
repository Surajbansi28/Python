u = input("Enter the value you want to convert into ASCII code : ")
y = ord (u)
print(y)

#TASK 2

x = int(input("Enter an integer value from 0 to 9 : "))
count = 0
for count in range(1, 11):      
   print (x, 'x', count, '=', x * count)