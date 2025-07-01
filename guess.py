import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Guess the number (1-100):")

while True:
    guess = int(input("Enter guess: "))
    attempts += 1

    if guess < number:
        print("Too low!\n")
    elif guess > number:
        print("Too high!\n")
    else:
        print(f"🎉 Correct! You guessed in {attempts} tries.")
        break
