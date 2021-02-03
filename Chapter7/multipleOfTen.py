#Hands on #1 | 7-3
print("-----Exercise 7-3-----\n")

number = input("Enter in a number: " )
number = int(number)
multiple = 10

if number % multiple == 0:
    print("\tThe input number is a multiple of 10.")
else:
    print("\tThe input number is not a multiple of 10.")