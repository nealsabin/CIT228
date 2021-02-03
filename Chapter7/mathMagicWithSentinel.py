#Hands on #2 | #1
print("-----Hands On #2 | #6-----\n")

import random
prompt = "\nWould you like to continue?"
prompt += " Enter 'q' to end the program or press enter to continue.\n"

keepGoing = ""
counter=0
numberCorrect=0

while keepGoing != "q":
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    answer = int(randNum1 + randNum2)
    questionNumber = counter + 1

    inputAnswer = int(input(f"{questionNumber}) What is the answer to {randNum1} + {randNum2}?"))
    if answer==inputAnswer:
        print("   > Correct!")
        numberCorrect+=1
    else:
        print(f"   > Your answer is incorrect. Correct answer: {answer}.")
    counter+=1
    keepGoing = input(prompt)

print(f"\nQuestions answered correctly: {numberCorrect}.")

