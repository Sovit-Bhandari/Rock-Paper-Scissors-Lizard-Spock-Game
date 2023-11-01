'''Full Name = Sovit Bhandari
   U-number = U83561265
   Brief discription = This code is an updated version of the game rock, paper and scissors. This code take the input from the user
   and match with the random input form the computer to check who wins the game with the help of conditions provided'''

#Providing options to input for the user and assigning computer to choose random choices from the given options
import random                                                                           #using modules
print("Let's play Rock, Paper, Scissors, Lizard, Spock!")   
your_choice = input("Enter your choice:").lower()                                       #assigning lower case for input
computer_options = ("rock", "paper", "scissors", "lizard", "spock" )                    # providing options for the computer
computer = random.choice(computer_options)                                #assigning computer to chose random number from the given options
print("Computer chose", computer)

#Conditions when player wins the game and explaination for the wining cause
if your_choice == 'scissors' and computer == 'paper':
    print('Scissors cuts Paper! You Win!')
elif your_choice == 'scissors' and computer == 'lizard':
    print('Scissors decapitates Lizard! You Win!')
elif your_choice == 'lizard' and computer == 'spock':
    print('Lizard poisons Spock! You Win!')
elif your_choice == 'lizard' and computer == 'paper':
    print('Lizard eats Paper! You Win!')
elif your_choice == 'spock' and computer == 'scissors':
    print('Spock smashes Scissors! You Win!')
elif your_choice == 'spock' and computer == 'rock':
    print('Spock vaporizes Rock! You Win!')
elif your_choice == 'rock' and computer == 'lizard':
    print('Rock crushes Lizard! You Win!')
elif your_choice == 'rock' and computer == 'scissors':
    print('Rock crushes scissors! You Win!')
elif your_choice == 'paper' and computer == 'spock':
    print('Paper disproves Spock! You Win!')
elif your_choice == 'paper' and computer == 'rock':
    print('Paper covers Rock! You Win!')


#conditons when computer wins and the the explaination of wins is also provided
elif computer == 'scissors' and your_choice == 'paper':
    print('Scissors cuts Paper! Computer wins!')
elif computer == 'scissors' and your_choice == 'lizard':
    print('Scissors decapitates Lizard! Computer wins!')
elif computer == 'lizard' and your_choice == 'spock':
    print('Lizard poisons Spock! Computer wins!')
elif computer == 'lizard' and your_choice == 'paper':
    print('Lizard eats Paper! Computer wins!')
elif computer == 'spock' and your_choice == 'scissors':
    print('Spock smashes Scissors! Computer wins!')
elif computer == 'spock' and your_choice == 'rock':
    print('Spock vaporizes Rock! Computer wins!')
elif computer == 'rock' and your_choice == 'lizard':
    print('Rock crushes Lizard! Computer wins!')
elif computer == 'rock' and your_choice == 'scissors':
    print('Rock crushes scissors! Computer wins!!')
elif computer == 'paper' and your_choice == 'spock':
    print('Paper disproves Spock! Computer wins!')
elif computer == 'paper' and your_choice == 'rock':
    print('Paper covers Rock! Computer wins!')


#Conditions when game can be draw
elif your_choice == computer:
    print("It's a tie!")

print("Thanks for playing!")