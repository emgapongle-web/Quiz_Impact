import time
import json
import random

print("THIS IS A WORKING PROTOTYPE")
user_name = str(input("What's your name?"))
print(f"What an amazing name you got there, {user_name}!")
time.sleep(1)
print("Well then, welcome to Quiz Impact.")
time.sleep(1)
print("I hope you enjoy and learn something new throughout the game.")
time.sleep(1)

question_number = 1
letters = ['A', 'B','C','D']
iq_points = 0

print("\n")
try:
    # READING from the file
    filename = "questions.json"
    with open(filename, 'r') as file:
    # Load the JSON data from the file
        data = json.load(file)

    random.shuffle(data)

    def menu():
        print("\n")
        print("MENU")
        print("1. Play")
        print("2. Manual")
        print("3. Exit")
        user_wow = input("What are you choosing to open? ")
        if user_wow == "1":
            play()
        elif user_wow == "2":
            instructions()
        elif user_wow == "3":
            print("Goodbye.")
            exit()
        else:
            print("Invalid Input.")

    def instructions():
        print(" I N S T R U C T I O N S ")
        print("Now, how do you play Quiz Impact?")
        time.sleep(1)
        print("But before that, you might want to take note of these things: ")
        time.sleep(2)
        print("1. This game has a Gacha system where you can wish for 10 times at once and for 1 time only. Proceed to the gacha interface to make a wish! "
              "Additionally, you can see your wish history there as well.")
        time.sleep(5)
        print("2. This is a quiz type game that contains 300 questions. 50 EASY questions, 100 NORMAL questions, and 150 HARD questions. "
              "It covers the different subjects and topics of grade 8.")
        time.sleep(5)
        print("3. This game has chances, also known as, pity where you can get guaranteed to have the highest and amazing magical helper if you have a high pity.")
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
        print("First, as you open the game, you'll be given options where you can find the menu, the gacha interface and the achievement page. ")
        time.sleep(3)
        print("If you start with the menu, you'll find the options where you can be directed to the Manual, Play, or Exit!")
        time.sleep(4)
        print("Else if you chose to go to the Gacha Interface, you'll be directed to a page where it asks you to pull. ")
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
        print("With this, you can now answer them in a certain amount of time. (The higher the difficulty level, the longer the time!)")
        time.sleep(4)
        print("After answering a question, the program will tell you if your answer is wrong or right. ")
        time.sleep(3)
        print("Then, it will ask you if you want to continue or not. ")
        time.sleep(3)
        print("If you chose to continue, then it will proceed to ask you some questions.")
        time.sleep(2)
        print("But if you chose to exit, it will let you go back to the menu.")

    def play():
        global question_number, iq_points
        for question in data:
            print(f"Question {question_number}: {question['question']}")
            print(f"This is {question['level']}.")
            options = question['options']

            for letter, option in zip(letters, options):
                print(f"  {letter}. {options} ")

            user_input = input("Your choice(A/B/C/D): ").upper().strip()

            valid_letters = letters[:len(options)]
            if user_input in valid_letters:
                index = valid_letters.index(user_input)
                selected = options[index]

                if selected == question['answer']:
                    print("\n Correct! \n")
                    iq_points += question["score increase"]
                else:
                    print(f"\n Wrong! Correct answer: {question['answer']} \n")
                    iq_points +=question["score penalty"]
            else:
                print("\n Invalid choice. ")

            print(f"Your current IQ points are {iq_points}")

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