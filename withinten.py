import random

while True:
    kimball = random.randint(1,100)
    far_fall = input("Guess a number between 1 and 100")
    if (kimball <= far_fall + 10) and (kimball >= far_fall - 10):
        print("Your guess was within 10 of the number.")
    print(kimball)
