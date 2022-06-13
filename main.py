import random
# "R" is for "rock", "P" is for "Paper" and "S" is for "scisors"
player_options = ["R", "P", "S"]
def rock_paper_scisors():
    print('This is Rock-Paper-Scisors. Rock beats Scisors, Paper beats Rock and Scisors beats paper\n "R" is for "rock", "P" is for "Paper" and "S" is for "scisors"')
    
    user_name = input("Enter your name here:")
    
    user_input = input("Choose an option between 'R', 'P', 'S':")
    
    while user_input not in player_options:
        print("Error, enter your input again")
        
    if user_input in player_options:
        print("Your input is ", user_input, "wait for next player turn!")
        
    computer_choice = random.choice(player_options)
    print(user_name, " choice is ", user_input, " next player choice is, ", computer_choice)
    
    if (user_input =="R" and computer_choice =="P"):
        print("Other Player wins")
        
    elif (user_input =="R" and computer_choice =="S"):
        print(user_name, " wins")
        
    elif (user_input =="P" and computer_choice =="R"):
        print(user_name, " wins")
        
    elif (user_input =="P" and computer_choice =="S"):
        print("Other Player wins")
        
    elif (user_input =="S" and computer_choice =="R"):
        print("Other Player wins")
        
    elif (user_input =="S" and computer_choice =="P"):
        print(user_name, " wins")
        
    elif user_input == computer_choice:
        print("Its a Tie")
        
    replay = input("Do you want to play again, if yes enter 'Y', and 'N' if no:")
    if replay == 'Y':
        return rock_paper_scisors()
    else:
        return


rock_paper_scisors()
