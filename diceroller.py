import random
min = 1
max = 6

game = input("Roll the dice? (Y/N) ")

roll_dice = True

while roll_dice == True:

    if game == "Y" or game == "yes" or game == "Yes" or game == "y":
        print("Rolling the dice...")
        print("You rolled: ")
        print(random.randint(min, max))

        game = input("Roll the dice again? (Y/N) ")

    else:
        print("No dice rolled.")


        game = input("Roll the dice? (Y/N) ")
