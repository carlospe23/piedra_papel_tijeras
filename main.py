import random


def check_win(player, computer):
    print(f'You chose {player} and the computer chose {computer}')

    if player == computer:
        return 'it is a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            return 'You win'
        else:
            return 'You lose'
    elif player == 'scissors':
        if computer == 'paper':
            return 'You win'
        else:
            return 'You lose'
    elif player == 'paper':
        if computer == 'rock':
            return 'You win'
        else:
            return 'You lose'


if __name__ == '__main__':
    options = ['rock', 'paper', 'scissors']
    player_choice = input(f'Enter a choice {options}: ')
    computer_choice = random.choice(options)

    result = check_win(player_choice, computer_choice)
    print ( result )