#Hands on 1
print("------------Hands on 1-----------")
foods = ["peanut butter","tacos", "brocoli","pizza","steak","chicken"]
print("Foods: ",foods)

numbers = [1,234,8,4,6,8]
print("Numbers: ",numbers)

movies = ["Lord of the Rings","Arrival","Bladerunner 2049"]
print("Movies: ",movies)

favorites = ["tacos","pizza",6,8,"Lord of the Rings","Arrival"]
print("Favorites: ",favorites)

print("Last food: ",foods[-1])
print("2nd, 4th, and 6th numbers: ",numbers[1], numbers[3], numbers[-1])
print("All movies: ",movies[0],movies[1],movies[2])
print("First food: ", favorites[0], "First number: ", favorites[2], "First Movie: ",favorites[4])

#Hands on 2
print("\n\n------------Hands on 2-----------")
foods = ["peanut butter","tacos", "brocoli","pizza","steak","chicken"]
foods.insert(5,"bread")
del foods[0]
print("Foods: ",foods)

numbers = [1,234,8,4,6,8]
numbers.insert(3,44)
removedNumber = numbers.pop()
removedNumber2 = numbers.pop(2)
print("Numbers: ",numbers)

movies = ["Lord of the Rings","Arrival","Bladerunner 2049"]
movies.append("Rogue One")
print("Movies: ",movies)

favorites = ["tacos","pizza",6,8,"Lord of the Rings","Arrival"]
print("Favorites: ",favorites)

print("Last food: ",foods[-1])
print("2nd, 4th, and 6th numbers: ",numbers[1], numbers[3], numbers[-1])
print("All movies: ",movies[0],movies[1],movies[2])
print("First food: ", favorites[0], "First number: ", favorites[2], "First Movie: ",favorites[4])

#Hands on 3
print("\n\n------------Hands on 3-----------")
movies.sort()
print("Sorted Movies: ",movies)

foods.sort()
print("Sorted Foods: ",foods)

sorted(numbers)
print("Temp Number Sorted: ",numbers)
print("Unsorted Numbers: ",numbers)

movies.reverse()
print("Reversed Sorted Movies: ",movies)

