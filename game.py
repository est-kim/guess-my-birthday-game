#First Guess My Birthday Exercise
# from random import randint

# name = input("Hi! What is your name? ")

# for guess_number in range(5):
#     random_month = randint(1,12)
#     random_year = randint(1924, 2004)
#     print("Guess", str(guess_number + 1), ":", name, "were you born in", random_month, "/", random_year, "?")
#     yes_or_no = input("yes or no? ")
#     if yes_or_no == "yes":
#         print("I knew it!")
#         break
#     elif guess_number == 4 and yes_or_no == "no":
#         print("I have other things to do. Goodbye.")
#     else:
#         print("Drat! Lemme try again!")


#Stretch Goal Attempt
import random
from random import randint
import calendar

guess_count = 1

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

low_day = 1
high_day = 31

# low_month = months[0]
# high_month = months[11]
low_month = calendar.month_name[1]
high_month = calendar.month_name[12]

low_year = 1924
high_year = 2004

name = input("Hi! What is your name? ")

for guess_number in range(5):

    guess_day = randint(low_day, high_day)
    guess_month = random.choice(months)
    guess_year = randint(low_year, high_year)

    print("Guess", str(guess_number + 1), ":", name, "were you born on", guess_month, guess_day, guess_year, "?")
    yes_later_earlier = input("yes, later, or earlier? ").lower()
    if guess_count == 4:
        print("I have other things to do. Goodbye.")
    elif yes_later_earlier == "yes":
        print("I knew it!")
        print("It took me", guess_count, "guesses!")
        break
    elif yes_later_earlier == "later":
        print("Drat! Lemme try again!")
        low_year = guess_year + 1
        guess_count = guess_count + 1
    elif yes_later_earlier == "earlier":
        print("Drat! Lemme try again!")
        high_year = guess_year - 1
        guess_count = guess_count + 1
