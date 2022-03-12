a = "Mississippi"
index = 0
index2 = 0
index3 = 0
for i in range(0,len(a)):
    if a[i] == 'i':
        index = index + 1
    if a[i] == 's':
        index2 = index2 + 1
    if a[i] == 'p':
        index3 = index3 + 1
    occurence_dict = {
                    "i": index,
                    "s": index2,
                    "p": index3 
        }

print(occurence_dict)
