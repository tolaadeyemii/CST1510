""
#9Addition quiz

#Step 1: Generate two single digit intergers for number 1 (e.g 4) and number 2 (e.g 5)
#Step 2: Prompt the student to answer "What is 4 + 5?" (user input)
#Step 3: Check whether the students answer is correct 

num1 = 4
num2 = 5

answer = int(input(f"What is {num1} + {num2}? "))

if answer == num1 + num2:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {num1 + num2}.")