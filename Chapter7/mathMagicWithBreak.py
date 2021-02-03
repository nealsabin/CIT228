#Hands on #2 | #1
import random
# problems = int(input("Enter the nunber of problems you would like: "))

counter=0
numberCorrect=0
while counter != 'q':
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    answer = int(randNum1 + randNum2)
    questionNumber = counter + 1
    inputAnswer = int(input(f"{questionNumber}) What is the answer to {randNum1} + {randNum2}?"))
    if answer==inputAnswer:
        print("Correct!")
        numberCorrect+=1
    else:
        print(f"Your answer is incorrect. Correct answer: {answer}.")
    counter+=1
    if counter == 10:
        break

print(f"\nQuestions answered correctly: {numberCorrect}.")
if numberCorrect < 5:
    print("\tYou should consider getting a tutor.")
else:
    print("\tGreat job!")

