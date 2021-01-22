print("----Ch4 Ex. 4-9----\n")

cubeList = []
for value in range(1,11):
    cube = value**3
    cubeList.append(cube)
print(cubeList)

#With comprehension
cubeList2 = [value**3 for value in range(1,11)]
print(cubeList2)