import random
R_list = ["rock","paper","scissor"]
while True:
    AI_choice=random.choice(R_list)
    user = input("Input [rock,paper,scissor] choice according to given value:")
    user = user.lower()
    if AI_choice==user:
        print("You Win!")
        print("If want to quit this game Enter 'exit'")
    elif user=="exit":
        break
    else:
        print("You Loose!")
        print("If want to quit this game Enter 'exit'")