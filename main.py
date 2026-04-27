#IMPORT NEEDED LIBRARIES
import time
import json
import random

user_name = str(input("What's your name?")) #This line asks for the user's name
print(f"What an amazing name you got there, {user_name}!")
time.sleep(1)
print("Well then, welcome to...")
#Print the game's title
print(fr"   ____  __  ___________      ______  _______  ___   ______________")
print(fr"  / __ \/ / / /  _/__  /     /  _/  |/  / __ \/   | / ____/_  __/ /")
print(fr" / / / / / / // /   / /      / // /|_/ / /_/ / /| |/ /     / / / / ")
print(fr"/ /_/ / /_/ // /   / /__   _/ // /  / / ____/ ___ / /___  / / /_/  ")
print(fr"\___\_\____/___/  /____/  /___/_/  /_/_/   /_/  |_\____/ /_/ (_)   ")
time.sleep(1)
print("I hope you enjoy and learn something new throughout the game.")
time.sleep(1)

#Initialize needed variables
question_number = 1
letters = ['A', 'B','C','D']
hint = ['H']
iq_points = 0
fanfare = 100
hint_cost = 20

print("\n")
try:
    # READING from the file
    filename = "questions.json"
    with open(filename, 'r') as file:
    # Load the JSON data from the file
        data = json.load(file)

    random.shuffle(data)

    #Created a menu function
    def menu():
        print("Let's continue! ")
        print(r""" 
1. PLAY
2. MANUAL 
3. EXIT
        """)
        while True:
            userC = input("Where would you like to go? ")
            if userC == '1':
                play(iq_points,question_number,fanfare, hint_cost, hint)
                break
            elif userC == '2':
                instructions()
                break
            elif userC == '3':
                print(f"You have accumulated {iq_points} iq points in total!") #Special message will display if the player got 130 iq_points.
                if iq_points >= 130:
                    print("Good Job! And because of that you have five heart pitiks from QUIZ IMPACT!")
                    time.sleep(3)
                    print("<3 !")
                    time.sleep(1)
                    print("<3 !")
                    time.sleep(1)
                    print("<3 !")
                    time.sleep(1)
                    print("<3 !")
                    time.sleep(1)
                    print("<3 !")
                    time.sleep(1)
                    print("Nice playing with you. Goodbye!")
                else:
                    print("Good bye.")
                exit()
            else:
                print("girl, invalid.")

        # Created an instructions or the manual for the player

    def instructions():
        print(" I N S T R U C T I O N S ")
        print("Now, how do you play Quiz Impact?")
        time.sleep(1)
        print("But before that, you might want to take note of these things: ")
        time.sleep(5)
        print(
            "\nThis is a quiz type game includes general knowledge questions")
        time.sleep(5)
        print(
            "The game keeps track of your score through a mechanic called fanfare")
        time.sleep(3)
        print("If your fanfare drops too low you might risk ending the game quickly!")
        time.sleep(5)
        print("\nFurthermore, IQ points serve as currency to ask for hints!")
        time.sleep(3)
        print("1 correct answer from an EASY question = +10 IQ points")
        time.sleep(1)
        print("1 correct answer from a NORMAL question = +20 IQ points")
        time.sleep(1)
        print("1 correct answer from a HARD question = +30 IQ points")
        time.sleep(1)
        print("1 Hint = 20 IQ points")
        time.sleep(1)
        print("You may use the hint button; 'H' to ask for a hint")
        time.sleep(1)
        print("You may get a hint only once per question")
        time.sleep(5)
        print("\nLet's now proceed to the instructions!")
        time.sleep(1)
        print("First, as you open the game, you shall be directed to the menu page.")
        time.sleep(2)
        print("You'll find the options where you can be directed to the Manual, Play, or Exit!")
        time.sleep(1)
        print("Else if you chose to go to the 'Play', you'll be directed to the main gameplay loop")
        time.sleep(1)
        print("If you go to the Manual you will be directed here")
        time.sleep(3)
        print("But if you want to exit, then choose the exit option!")
        time.sleep(1)
        print("As you start the game, one of the questions will now start to be given. "
              "The questions will be randomly given! If you answered an easy one, the next one might be a hard question. ")
        time.sleep(3)
        print("Finally, good luck and have fun!")
        menu()

    #Main gameplay loop function
    def play(iq_points, question_number,fanfare, hint_cost, hint):
        for question in data:
            print(f"\nQuestion {question_number}: {question['question']}")
            print(f"This is {question['level']}.")
            options = question['options']
            for i in range(len(options)):
                print(f"{letters[i]}. {options[i]} ")

            while True:
                user_input = input("Your choice(A/B/C/D): ").upper().strip() #Validates the input whether capital or lowercase
                if user_input in letters:
                    index = letters.index(user_input)
                    selected = options[index]
                    if selected == question['answer']:
                        print("\n Correct! \n")
                        fanfare += question["fanfare increase"]
                        iq_points +=question["iq_points"]
                        break
                    else:
                        print(f"\n Wrong! Correct answer: {question['answer']} \n")
                        fanfare +=question["fanfare penalty"]
                        print(fr"           /^\/^\ ")
                        print(fr"         _|__|  O| ")
                        print(fr"\/     /~     \_/ \ ")
                        print(fr" \____|__________/  \ ")
                        print(fr"       \_______      \ ")
                        print(fr"                `\     \                 \ ")
                        print(fr"                  |     |                  \ ")
                        print(fr"                 /      /                    \ ")
                        print(fr"                /     /                       \\")
                        print(fr"              /      /                         \ \ ")
                        print(fr"             /     /                            \  \ ")
                        print(fr"           /     /             ----            \   \ ")
                        print(fr"          /     /           -~      ~-         |   | ")
                        print(fr"        (      (        -~    _--    ~-_     _/   |")
                        print(fr"          \      -____-    -~    -    ~-_-    / ")
                        print(fr"           -_           -          -       _- ")
                        print(fr"             --______-                -___- ")
                        if fanfare <= 0: #Fanfare mechanic
                            exit()
                    break
                elif user_input in hint: #The hint system
                    if iq_points >= hint_cost:
                        iq_points = iq_points - hint_cost
                        print(f"HINT: {question['hint']}")
                        continue
                    else:
                        user_input = print("Not enough! You may still answer though")
                        continue
                    break
                else:
                    print("\n Invalid choice. ")

            #Shows how many fanfare and the iq points the player has
            print(f"Your current fanfare are {fanfare}")
            print(f"You have accumulated {iq_points} iq points so far!")

            while True:
                user_yn = input("Do you want to continue? (Y/N) ") #Asks the player if they want to continue
                if user_yn.lower() == 'y':
                    print("Alright, let's continue.")
                    break
                elif user_yn.lower() == 'n':
                    print("Oh alright then, goodbye!")
                    menu()
                else:
                    print("Invalid, girl.")

            question_number += 1 #Proceeds to the next question item

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

menu()