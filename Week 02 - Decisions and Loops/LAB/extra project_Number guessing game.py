secret_number = 7
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Congratulations! Well done tola!")
        print(f"You guessed the number in {attempts} attempts.")