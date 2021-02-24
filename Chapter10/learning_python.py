#Hands on #1
#Exercise 10-1
print('-----Exercise 10-1-----')

filename="Chapter10/learning_python.txt"

with open(filename) as pythonFile:
    contents = pythonFile.read()
print(contents)

print("\n")

with open(filename) as pythonFile:
    for line in pythonFile:
        print(line)

print("\n")

with open(filename) as pythonFile:
    myFile=pythonFile.readlines()

for line in myFile:
    print(line)

#10-2
print("\n-----Exercise 10-2-----")
with open(filename) as pythonFile:
    for line in pythonFile:
        print("Original File: ", line)
        print("Altered: ", line.replace("Python","Viper"))