import random
choice = input("Enter your choice:")
possiblity = ["rock","paper","scissor"]
computer_choice = random.choice(possiblity)
print("Computer choice:"+computer_choice)
if choice == "rock" :
    if computer_choice == "rock" : print("draw")
    elif computer_choice == "paper" : print("computer wins")
    elif computer_choice == "scissor" : print("user wins")
elif choice == "paper" :
    if computer_choice == "rock" : print("user wins")
    elif computer_choice == "paper" : print("draw")
    elif computer_choice == "scissor" : print("scissor wins")
elif choice == "scissor" :
    if computer_choice == "rock" : print("computer wins")
    elif computer_choice == "paper" : print("user wins")
    elif computer_choice == "scissor" : print("draw")
else :
    print("Invalid Choice")