import random

# print("Print your name:")
name = input("Print your name:")
question = input("Ask question:")

random_number = random.randint(1, 10)
answer = random_number

# print(random_number)

if answer:
    print(name, "asks:", question)
    if name:

        if random_number == 1:
            answer = "Yes - definitely."
        elif random_number == 2:
            answer = "It is decidedly so."
        elif random_number == 3:
            answer = "Without a doubt."
        elif random_number == 4:
            answer = "Reply hazy, try again."
        elif random_number == 5:
            answer = "Ask again later."
        elif random_number == 6:
            answer = "Better not tell you now."
        elif random_number == 7:
            answer = "My sources say no."
        elif random_number == 8:
            answer = "Outlook not so good."
        elif random_number == 9:
            answer = "Very doubtful."
        elif random_number == 10:
            answer = "Cheerful."
        else:
            answer = "Error"

        print("Magic 8-Ball's answer:", answer)

    else:
        print("Outlook not so good")
else:
    print("There is no a question asked")