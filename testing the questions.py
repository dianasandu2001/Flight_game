Questions = ["Romania is the largest salt mine in Europe", ]
Answers = ["true", ]

number = random.randint(0, (len(Questions) - 1))
print(random.choice(Questions))
answer = lower.input("Is this true or false: ")
if answer in Answers:
    fuel = fuel + 5000
    print("Answer is correct, 5000l of fuel awarded")
else:
    print("Answer is wrong, no fuel awarded")