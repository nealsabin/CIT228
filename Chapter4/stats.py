print("-----Ch4-Hands on 2-----\n")
import random

number = random.randrange(10,100)
numList = list(range(number))
print(numList,"\n")

print(f"The largest number = {max(numList)}")
print(f"The smallest number = {min(numList)}")
print(f"The total of all the numbers = {sum(numList)}")
print(f"the average number = {sum(numList)/len(numList)}")