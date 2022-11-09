from random import randint

name = input("Hi! What is your name? ")

for guess_number in range(5):
    random_month = randint(1,12)
    random_year = randint(1924, 2004)
    print("Guess", str(guess_number + 1), ":", name, "were you born in", random_month, "/", random_year, "?")
    yes_or_no = input("yes or no? ")
    if yes_or_no == "yes":
        print("I knew it!")
        break
    elif guess_number == 4 and yes_or_no == "no":
        print("I have other things to do. Goodbye.")
    else:
        print("Drat! Lemme try again!")
