print("Welcome to treasure island")
print("Your mission is to find the treasure.")

choice1 = input('You reach a cross road. Where do you want to go? Type "left" or "right" ').lower()

if choice1 == "left":
    choice2 = input("You reach a lake. Type 'swim' to swim across or 'wait' to wait for a boat. ").lower()

    if choice2 == "wait":
        choice3 = input("Three doors appear: red, blue or yellow. Which one do you choose? ").lower()

        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("You were burned by fire. Game Over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("You were attacked in the lake. Game Over.")
else:
    print("You fell into a hole. Game Over.")


