list1 = [1,2,3]
list2 = ['a', 'b', 'c']
n = len(list1)
list3 = []
for index, item in enumerate(list1):
    list3.append(item)
    list3.append(list2[index])

print (list3)
