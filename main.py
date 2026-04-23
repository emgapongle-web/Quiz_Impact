#IMPORT NEEDED LIBRARIES
import time
import json
import random

print("THIS IS A WORKING PROTOTYPE")
user_name = str(input("What's your name?"))
print(f"What an amazing name you got there, {user_name}!")
time.sleep(1)
print("Well then, welcome to...")
print(fr"   ____  __  ___________      ______  _______  ___   ______________")
print(fr"  / __ \/ / / /  _/__  /     /  _/  |/  / __ \/   | / ____/_  __/ /")
print(fr" / / / / / / // /   / /      / // /|_/ / /_/ / /| |/ /     / / / / ")
print(fr"/ /_/ / /_/ // /   / /__   _/ // /  / / ____/ ___ / /___  / / /_/  ")
print(fr"\___\_\____/___/  /____/  /___/_/  /_/_/   /_/  |_\____/ /_/ (_)   ")
time.sleep(1)
print("I hope you enjoy and learn something new throughout the game.")
time.sleep(1)

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
                print("Nice playing with you. Goodbye!")
                exit()
            else:
                print("girl, invalid.")

        # Created an instructions or the manual for the player


    def instructions():
        print(" I N S T R U C T I O N S ")
        print("Now, how do you play Quiz Impact?")
        time.sleep(1)
        print("But before that, you might want to take note of these things: ")
        time.sleep(2)
        print(
            "1. This is a quiz game where you have to answer questions to gain iq points.")
        time.sleep(5)
        print(
            "2.These IQ points will serve as the currency to buy hints")
        time.sleep(5)
        print(
            "3. Hints can help you answer questions!.")
        time.sleep(3)
        print("4. 1 correct answer from an EASY question = +10 IQ points")
        time.sleep(1)
        print("5. 1 correct answer from a MEDUM question = +20 IQ points")
        time.sleep(1)
        print("6. 1 correct answer from a HARD question = +30 IQ points")
        time.sleep(1)
        print("A hint costs 20 IQ points! ")
        time.sleep(2)
        print("7. Additionally, we also have a fanfare feature where you have to maintain your fanfare to be able to continue playing")
        time.sleep(3)
        print("8. If you have 0 of them, you will be directed to the menu. ")
        time.sleep(3)
        print("9. Moreover, there is only one hint per question!")
        print("Let's now proceed to the instructions!")
        time.sleep(1)
        print(
            "First, as you open the game, you'll be given options where you can find the play, manual and the exit. ")
        time.sleep(3)
        print(
            "If you start with the manual, you'll find the instructions, which you are in right now. ")
        time.sleep(4)
        print(
            "Else if you chose to go to the exit, of course the game will close.")
        time.sleep(4)
        print("Now, if you chose to play, you'll be led to the game immediately!")
        time.sleep(3)
        print("As you start the game, one of the questions will now start to be given. "
              "The questions will be randomly given! If you answered an easy one, the next one might be a hard question. ")
        time.sleep(3)
        print(
            "With this, you can now answer them.")
        time.sleep(4)
        print("The choices will also include a hint input where you can only buy them if you have enough IQ points. ")


    #Main gameplay loop function
    def play(iq_points, question_number,fanfare, hint_cost, hint):
        for question in data:
            print(f"Question {question_number}: {question['question']}")
            print(f"This is {question['level']}.")
            options = question['options']
            for i in range(len(options)):
                print(f"{letters[i]}. {options[i]} ")

            used_hint = False
            while True:
                if iq_points >= hint_cost and not used_hint:
                    text = ("Your choice(A/B/C/D)? or Would you like a hint?(H): ")
                else:
                    text = ("Your choice(A/B/C/D): ")

                user_input = input(text).upper().strip()
                
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
                        if fanfare > 0:
                            break
                            
                        else:
                            print("Sorry, you have wasted all your fanfare already. ")
                            time.sleep(1)
                            print("Returning")
                            time.sleep(1)
                            print("to")
                            time.sleep(1)
                            print("menu . . . ")
                            time.sleep(1)
                            menu()
                    break
                elif user_input in hint and iq_points >= hint_cost and not used_hint:
                    print("Using your hint: ")
                    iq_points = iq_points - hint_cost
                    print(f"HINT: {question['hint']}")
                    used_hint = True
                    continue
                    
                    break

                
                else:
                    print("\n Invalid choice. ")

            print(f"Your current fanfare are {fanfare}")
            print(f"You have accumulated {iq_points} iq points so far!")

            while True:
                user_yn = input("Do you want to continue? (Y/N) ")
                if user_yn.lower() == 'y':
                    print("Alright, let's continue.")
                    break
                elif user_yn.lower() == 'n':
                    print("Oh alright then, goodbye!")
                    menu()
                else:
                    print("Invalid, girl.")

            question_number += 1


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

menu()
