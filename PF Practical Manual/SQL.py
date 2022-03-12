import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "Bansi", Password = "PFpractical")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE primenumbers")
a = int(input("Enter the no. of values you want to add:"))
for i in range(0,a):
    addingint = int(input("Enter the numbers you want to add to the database:"))
    primecheck = input("If it is a prime number or not(Y/N):")
    mycursor.execute("CREATE TABLE primevalues(values INT(10)")
    sql = "INSERT INTO primevalues(values) VALUES (%s,%s)"
    val = (addingint, primecheck)
    mycursor.execute(sql,val)
    mydb.commit()
    continue

checkint = int(input("Enter the number you want to check as a prime number:"))
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM primevalues")
if checkint == mycursor.fetchone("values"):
    print(checkint)
else:
    mycursor.execute("INSERT INTO primevalues(checkint) VALUES (%s,%s)")
    sql = "INSERT INTO primevalues(checkint) VALUES (%s,%s)"
    val = (checkint, primecheck)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    mydb.commit()
    
