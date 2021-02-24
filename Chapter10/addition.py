#Hands on 3
#Exercise 10-6 / 10-7
print("-----10-6 / 10-7-----\n")
print("Input two numbers to be added together: ")
print("Enter 'q' to quit\n")

while True:
    first_number = input("Enter 1st number: ")
    if first_number == 'q':
        break
    second_number = input("Enter 2nd number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("\tYou need to enter two numbers")
    else:
        print(f"{first_number} + {second_number} = {answer}")