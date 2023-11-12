import random

    # list of 3 elements scissors, paper, rock
choices = ["scissors", "paper", "rock"]
# while loop to keep the game running
user_points = 0
while True:
    print("Welcome to the game!\nscissors, paper, rock")
    # random choice from the list of choices
    computer_choice = random.choice(choices)
    # user input
    user_choice = input("Enter your choice: ").lower()
    # if statement to check if user input is valid
    if user_choice in choices:
        # if statement to check if user input is equal to computer choice
        if user_choice == computer_choice:
            print("Computer's choice: " + computer_choice)
            print("It's a tie!")
        # if statement to check if user input is scissors
        elif user_choice == "scissors":
            # if statement to check if computer choice is paper
            if computer_choice == "paper":
                user_points += 1
                print("Computer's choice: " + computer_choice)
                print("You win!")
            # if statement to check if computer choice is rock
            elif computer_choice == "rock":
                user_points -= 1
                print("Computer's choice: " + computer_choice)
                print("You lose!")
        # if statement to check if user input is paper
        elif user_choice == "paper":
            # if statement to check if computer choice is scissors
            if computer_choice == "scissors":
                user_points -= 1
                print("Computer's choice: " + computer_choice)
                print("You lose!")
            # if statement to check if computer choice is rock
            elif computer_choice == "rock":
                user_points += 1
                print("Computer's choice: " + computer_choice)
                print("You win!")
        # if statement to check if user input is rock
        elif user_choice == "rock":
            # if statement to check if computer choice is scissors
            if computer_choice == "scissors":
                user_points += 1
                print("Computer's choice: " + computer_choice)
                print("You win!")
            # if statement to check if computer choice is paper
            elif computer_choice == "paper":
                user_points -= 1
                print("Computer's choice: " + computer_choice)
                print("You lose!")
    # if statement to check if user input is not valid
    else:
        print("Invalid input, try again!")
        continue
    # ask user if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    # if statement to check if user input is y
    if play_again == "y":
        continue
    # if statement to check if user input is n
    elif play_again == "n":
        print("Thanks for playing!")
        print("Your points: " + str(user_points))
        break