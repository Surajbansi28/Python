#create a file 'employee.txt'. Get input employee id, employee name and salary from the user

f = open("employee.txt", 'w')
while True:
    employee_id = input("Enter the Employee ID:")
    name = input("Enter the name of the Employee:")
    Salary = input("Enter the salary of the Employee:")
    print("Do you want to add more data in to the file(Y/N):")
    choice = input()
    if choice == 'Y':
        employee_id = input("Enter the Employee ID:")
        name = input("Enter the name of the Employee:")
        Salary = input("Enter the salary of the Employee:")
    else:
        break
f.close

f = open("employee.txt", "r")
f.readlines