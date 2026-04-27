#IMPORT NEEDED LIBRARIES
import time
import json
import random

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
                print(f"You have accumulated {iq_points} in total!")
                if iq_points >= 100:
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
        time.sleep(2)
        print(
            "1. This game has a Gacha system where you can wish for 10 times at once and for 1 time only. Proceed to the gacha interface to make a wish! "
            "Additionally, you can see your wish history there as well.")
        time.sleep(5)
        print(
            "2. This is a quiz type game that contains 300 questions. 50 EASY questions, 100 NORMAL questions, and 150 HARD questions. "
            "It covers the different subjects and topics of grade 8.")
        time.sleep(5)
        print(
            "3. This game has chances, also known as, pity where you can get guaranteed to have the highest and amazing magical helper if you have a high pity.")
        time.sleep(5)
        print("4. IQ points serve as currency to make wishes!")
        time.sleep(3)
        print("5. 1 correct answer from an EASY question = +10 IQ points")
        time.sleep(1)
        print("6. 1 correct answer from a NORMAL question = +20 IQ points")
        time.sleep(1)
        print("7. 1 correct answer from a HARD question = +30 IQ points")
        time.sleep(1)
        print("8. 1 wish = 50 IQ points")
        time.sleep(1)
        print("9. 10 wishes = 500 IQ points")
        time.sleep(5)
        print("Let's now proceed to the instructions!")
        time.sleep(1)
        print(
            "First, as you open the game, you'll be given options where you can find the menu, the gacha interface and the achievement page. ")
        time.sleep(3)
        print(
            "If you start with the menu, you'll find the options where you can be directed to the Manual, Play, or Exit!")
        time.sleep(4)
        print(
            "Else if you chose to go to the Gacha Interface, you'll be directed to a page where it asks you to pull. ")
        time.sleep(3)
        print("Lastly, if you want to see the record of your achievements, then you may go to the achievement page. ")
        time.sleep(4)
        print("Now, in the menu, if you chose to go to the Manual, you'll be directed here!")
        time.sleep(3)
        print("But if you want to exit, then choose the exit option!")
        time.sleep(3)
        print("And of course, if you chose to start, you'll be led to the game already. ")
        time.sleep(2)
        print("As you start the game, one of the questions will now start to be given. "
              "The questions will be randomly given! If you answered an easy one, the next one might be a hard question. ")
        time.sleep(3)
        print(
            "With this, you can now answer them in a certain amount of time. (The higher the difficulty level, the longer the time!)")
        time.sleep(4)
        menu()

    #Main gameplay loop function
    def play(iq_points, question_number,fanfare, hint_cost, hint):
        for question in data:
            print(f"Question {question_number}: {question['question']}")
            print(f"This is {question['level']}.")
            options = question['options']
            for i in range(len(options)):
                print(f"{letters[i]}. {options[i]} ")

            while True:
                user_input = input("Your choice(A/B/C/D): ").upper().strip()
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
                        if fanfare <= 0:
                            exit()
                    break

                elif user_input in hint:
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