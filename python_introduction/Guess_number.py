import random
while True:
    secret_number =random.randint(1, 3)
    print(secret_number)
    guess = int(input("Guess a number between 1 and 3: "))

    # noinspection PyUnreachableCode
    match True:
        case _ if guess == secret_number:
                print ("Congratulations, you guessed it!")
        case _ if guess > secret_number:
                print ("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print ("Nope, your guess is a bit low. Give it another shot!")

    retry = input("Would you like to try again? (y/n): ")
    if retry == "y":
        continue
    else:
        break

