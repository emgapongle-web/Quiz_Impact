import time
import json
import sys

def main_menu():
    print("... Presents to you")
    print("")
    time.sleep(2)
    print("QUIZ IMPACT!")
    print("")
    time.sleep(3)
    print("WELCOME TO QUIZ IMPACT")
    print("")
    print("Main Menu: ")
    print("1. Play")
    print("2. Manual")
    print("3. Achievements")
    print("4. Exit")
    print("")

def menu_nav(main_menu_nav):
    if main_menu_nav == 1:
        print("THIS PART IS UNDER CONSTRUCTION")
        sys.exit(0)
    elif main_menu_nav == 2:
        print("THIS PART IS THE MANUAL")
    elif main_menu_nav == 3:
        print("THIS PART IS UNDER CONSTRUCTION")
    elif main_menu_nav == 4:
        print("GOODBYE!!")
        sys.exit(0)
    else:
        print("This is not a valid option...")
        print("Enter a number from 1-4 only.")

main_menu()
main_menu_nav = int(input("Enter a number: "))
menu_nav(main_menu_nav)