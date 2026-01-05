# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1

#homework

guess_count = 1
while guess_count <= 3:
    number = int(input("Guess Number between 1 and 10 \n"))
    guess_count += 1
    if guess_count > 3:
        print("Better luck next time")
    elif number > 10:
        print("Only 1 - 10 is allowed")
    elif number == 9:
        print("Good guess")
        exit()
    else:
        print("Incorrect")
