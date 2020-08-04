#THIS IS A TEST
import time
print("This game will inform you on how to better your chances of surviving a plane crash.")
print("For more information, visit https://www.cbsnews.com/news/how-to-survive-a-plane-crash/")
time.sleep(3)
print("\n")
print("How to survive a plane crash! (Created by Griffin Clode)")
time.sleep(3)
print("This game involves multiple choice questions.")
time.sleep(3)
print("To select one of the choices, you must choose the number that is assigned to that choice.")
time.sleep(3)
print("A test question will now be asked.")
time.sleep(3)

def tutorial1():
    try:
        test1 = int(input("Would you like to play the game? yes(1) no(2) :"))
        if test1 == 1:
            print("Great.")
            time.sleep(1.5)
            print("Next, your name will be asked.")
            time.sleep(2)
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
    time.sleep(2)
    print("The game will now begin.")
    time.sleep(2)
    part1sub1(name)


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

def part1sub1(name):
    print("\n")
    print("The clock on the wall ticks away.")
    time.sleep(3)
    print("3 hours have passed since you arrived.")
    time.sleep(3)
    print("Other than the occasional family rushing to catch their flight, you are alone.")
    time.sleep(3)
    print("You glance over at the screen showing upcoming flights.")
    time.sleep(3)
    print("One more hour.")
    time.sleep(2)
    print("You wait, feeling as though your flight will never arrive.")
    time.sleep(3)
    print("A robotic voice calmly announces;'flight 362 to arrive in 5 minutes.'")
    time.sleep(3)
    print("'Please prepare for departure immediately.'")
    time.sleep(3)
    print("Suddenly, masses of people start to flood through the entry way.")
    time.sleep(3)
    print("By the time you pick up your items from the luggage collection point,")
    time.sleep(3)
    print("The same robotic announcer says;'Plane 362 has arrived.'")
    time.sleep(3)
    print("'Please make your way onto the plane.'")
    time.sleep(3)
    print("You go through the metal detector, and come out without any trouble.")
    time.sleep(3)
    print("Next, you make your way to the ticket issuer.")
    time.sleep(3)
    print("With an authoratative tone of voice, he asks;")
    time.sleep(3)
    print("'What part of the plane would you like to be seated in, {}?'".format(name))
    part1sub2()

def part1sub2():
    try:
        seat_choice = int(input("Front of the plane(1) Middle of the plane(2) Back of the plane(3) :"))
        if seat_choice == 1:
            print("You have chosen to sit in the front of the plane.")
            print("For future knowledge, try to get a seat on at the back of the plane next time.")
            print("It is proven that the chances of survival in the rear of the plane")
            print("are much higher than in the front.")
        elif seat_choice == 2:
            print("You have chosen to sit in the middle of the plane.")
            print("This is a reasonable choice, however, the rear of the plane offers")
            print("a higher chance of survival in a plane crash.")
        elif seat_choice == 3:
            print("You have chosen to sit in the back of the plane.")
            print("This is a great choice. In the rear of the plane,")
            print("chances of survival in a plane crash are proven to be")
            print("far higher.")
        else:
            print("Invalid answer, try again.")
    except:
        print("Invalid answer, try again.")

tutorial1()
