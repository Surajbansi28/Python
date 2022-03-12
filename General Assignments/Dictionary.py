# Creating a Dictionary
myDict = {
        "Bansi":"Soon to be the biggest Content Creator of Pakistan ",
        "anotherdict" : {"Suraj" : "First name of the legend"}
    }
myDict['Bansi'] = "Youtuber"

print(myDict['Bansi'])
print(myDict['anotherdict']['Suraj'])

# Dictionary Methods
print(myDict.keys())
print(type(myDict.keys()))
print(myDict.values())
print(myDict.items())

newdict = { "kamlesh" : "Dun dun dun"} 
myDict.update(newdict)
print(myDict)

print(myDict.get("Bansi"))

# Empty Dictionary
a = {}
print(a)