import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/paper/scissors or E to Exit: ").lower()
    if user_input == "e":
        print("Good bye buddy..!!")

        continue

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock:0 , Paper:1, Scissors:2

    computer_pick = options[random_number]
    print("computer picked", computer_pick + '.')

    if user_input == "scissors" and computer_pick == "paper":
        print("You won..!!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won..!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win..!!")
        user_wins += 1

    else:
        print('computer wins..!!')
        computer_wins += 1

    print("You won", user_wins, "times.")
    print("Computer won", computer_wins, "times.")









