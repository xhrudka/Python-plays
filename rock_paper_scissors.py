computer_choice = "scissors"
user_choice=input("Do you want - rock, papper or scissors?\n")

if computer_choice == user_choice:
    print("Tie")
elif user_choice == 'rock' and computer_choice =='scissors':
    print("You win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win!")
else:
    print("You lose :( Computer wins :D ")
    