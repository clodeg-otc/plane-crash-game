#THIS IS A TEST
import time
print("This game will inform you on how to better your chances of surviving a plane crash.")
print("For more information, visit https://www.cbsnews.com/news/how-to-survive-a-plane-crash/")
print("\n")
print("How to survive a plane crash! (Created by Griffin Clode)")
print("This game involves multiple choice questions.")
print("To select one of the choices, you must choose the number that is assigned to the choice.")
print("A test question will now be asked.")

def tutorial1():
    try:
        test1 = int(input("Would you like to play the game? yes(1) no(2) :"))
        if test1 == 1:
            print("Great. Next, your name will be asked.")
            tutorial2()
        elif test1 == 2:
            tutorial3()
        else:
            print("Invalid answer, try again.")
            tutorial1()
    except:
        print("Invalid answer, try again.")
        tutorial1()

def tutorial2():
    name = str(input("What is your name? :"))
    print("Ok {}, you have completed the tutorial.".format(name))
    print("The game will now begin.")


def tutorial3():
    try:
        exit1 = int(input("Are you sure? yes(1) no(2) :"))
        if exit1 == 1:
            print("Ok, exiting game.")
            exit
        elif exit1 == 2:
            print("Ok, you will now be redirected to last question.")
            tutorial1()
        else:
            print("Invalid answer, try again.")
            tutorial3()
    except:
        print("Invalid answer, try again.")
        tutorial3()

tutorial1()
