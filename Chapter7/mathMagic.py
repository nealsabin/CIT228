#Hands on #2 | #1
import random
problems = int(input("Enter the nunber of problems you would like: "))
counter=0
numberCorrect=0
while counter < problems:
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    answer = int(randNum1 + randNum2)
    inputAnswer = int(input(f"What is the answer to {randNum1} + {randNum2}?"))
    if answer==inputAnswer:
        print("Correct!")
        numberCorrect+=1
    else:
        print(f"Your answer is incorrect. Correct answer: {answer}.")
    counter+=1

print(f"Questions answered correctly: {numberCorrect}.")

