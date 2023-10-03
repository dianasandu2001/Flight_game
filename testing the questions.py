import random

Questions = ["Romania is the largest salt mine in Europe", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
Answers = ["true", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a8", "a9", "a10"]

number = random.randint(0, (len(Questions) - 1))
print(Questions[number])
answer = input("Is this true or false: ").lower()
if answer == Answers[number]:
    #fuel = fuel + 5000
    print("Answer is correct, 5000l of fuel awarded")
else:
    print("Answer is wrong, no fuel awarded")