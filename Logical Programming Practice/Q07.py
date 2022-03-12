sum = 0
n = 4
q = int(input("Enter the Number of terms you want in the series after 4,16.... :"))
print(n)
next_term = n**2
print(next_term)
for i in range(0,q):
    digit = next_term % 10
    sum += digit**2
    next_term //= 10
    sum = sum + (next_term**2)
    next_term = sum
    sum = 0
    print(next_term)
