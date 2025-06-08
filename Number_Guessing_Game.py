import random

secret_number = random.randint(1, 10, )
print("Guess the number between 1 and 10. You have 5 attempts!")

for attempt in range(1, 6):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high")
        continue
    if guess < secret_number:
        print("Too low")
        continue
    else:
        print(f"You guessed {guess} correctly")
        break

print("Thank you for using my programme")
print(f"The answer was: {secret_number}")