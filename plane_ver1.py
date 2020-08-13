# THIS IS A TEST
import time
import random


def playtutorial():
    print("This game will inform you on how to better your chances of surviving a plane crash.")
    print("For more information, visit https://www.cbsnews.com/news/how-to-survive-a-plane-crash/")
    print("\n")
    print("How to survive a plane crash! (Created by Griffin Chode)")
    try:
        playtutorialchoice = int(input("Would you like to go play through the tutorial? yes(1) no(2) :"))
        if playtutorialchoice == 1:
            print("Ok.")
            tutorial1()
        elif playtutorialchoice == 2:
            print("Ok.")
            tutorial2()
        else:
            print("Invalid answer, try again.")
    except TypeError:
        print("Invalid answer, try again.")


def tutorial1():
    print("This game involves multiple choice questions.")
    print("To select one of the choices, you must choose the number that is assigned to that choice.")
    print("A test question will now be asked.")
    try:
        test1 = int(input("Would you like to play the game? yes(1) no(2) :"))
        if test1 == 1:
            print("Great.")
            print("Next, your name will be asked.")
            tutorial2()
        elif test1 == 2:
            tutorial3()
        else:
            print("Invalid answer, try again.")
            tutorial1()
    except TypeError:
        print("Invalid answer, try again.")
        tutorial1()


def tutorial2():
    name = str(input("What is your name? :"))
    print("Ok {}, you have completed the tutorial.".format(name))
    print("The game will now begin.")
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
    except TypeError:
        print("Invalid answer, try again.")
        tutorial3()


def part1sub1(name):
    print("\n")
    print("The clock on the wall ticks away.")
    print("3 hours have passed since you arrived.")
    print("Other than the occasional family rushing to catch their flight, you are alone.")
    print("You glance over at the screen showing upcoming flights.")
    print("One more hour.")
    print("You wait, feeling as though your flight will never arrive.")
    print("A robotic voice calmly announces;'flight 362 to arrive in 5 minutes.'")
    print("'Please prepare for departure immediately.'")
    print("Suddenly, masses of people start to flood through the entry way.")
    print("By the time you pick up your items from the luggage collection point,")
    print("The same robotic announcer says;'Plane 362 has arrived.'")
    print("'Please make your way onto the plane.'")
    print("You go through the metal detector, and come out without any trouble.")
    print("Next, you make your way to the ticket issuer.")
    print("With an authoratative tone of voice, he asks;")
    print("'What part of the plane would you like to be seated in, {}?'".format(name))
    part1sub2(name)


def part1sub2(name):
    try:
        seat_choice = int(input("Front of the plane(1) Middle of the plane(2) Back of the plane(3) :"))
        if seat_choice == 1:
            print("You have chosen to sit in the front of the plane.")
            print("For future knowledge, try to get a seat on at the back of the plane next time.")
            print("It is proven that the chances of survival in the rear of the plane")
            print("are much higher than in the front.")
            part1sub3front(name)
        elif seat_choice == 2:
            print("You have chosen to sit in the middle of the plane.")
            print("This is a reasonable choice, however, the rear of the plane offers")
            print("a higher chance of survival in a plane crash.")
            part1sub3middle(name)
        elif seat_choice == 3:
            print("You have chosen to sit in the back of the plane.")
            print("This is a great choice. In the rear of the plane,")
            print("chances of survival in a plane crash are proven to be")
            print("far higher.")
            part1sub3back(name)
        else:
            print("Invalid answer, try again.")
            part1sub2()
    except TypeError:
        print("Invalid answer, try again.")
        part1sub2()


def part1sub3front(name):
    print("Ticket in hand, you make your way over to the docking port.")
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightfront(name)
        else:
            print("Invalid answer, try again.")
            part1sub3front()
    except TypeError:
        print("Invalid answer, try again.")
        part1sub3front()


def part1sub3middle(name):
    print("Ticket in hand, you make your way over to the docking port.")
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightmiddle(name)
        else:
            print("Invalid answer, try again.")
            part1sub3middle()
    except TypeError:
        print("Invalid answer, try again.")
        part1sub3middle()


def part1sub3back(name):
    print("Ticket in hand, you make your way over to the docking port.")
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightback(name)
        else:
            print("Invalid answer, try again.")
            part1sub3back()
    except TypeError:
        print("Invalid answer, try again.")
        part1sub3back()


def part1sub5_title_waitingfornextflight():
    print("You decide that it is probably safest to wait.")
    print("You don't want to fly in dangerous weather now, do you?")
    print("You wait, for hours. Eventually, you board the next flight.")
    print("As you're boarding, you look up at the announcement screen.")
    print("The flight you had scheduled for crashed in the pacific, with only 26 survivors.")
    print("Sometimes, the best preventative action you can take")
    print("is to simply get a different flight, depending on the conditions.")
    playagain()


def part1sub5_title_notwaitingfornextflightfront(name):
    seat_numberfront = random.randint(1, 99)
    print("You decide not to wait.")
    print("A flight attendant greets you as you board the plane.")
    print("Good morning {}, please make your way to the front of the plane.".format(name))
    print("Your seat number is {}.".format(seat_numberfront))


def part1sub5_title_notwaitingfornextflightmiddle(name):
    seat_numbermiddle = random.randint(100, 199)
    print("You decide not to wait.")
    print("A flight attendant greets you as you board the plane.")
    print("Good morning {}, please make your way to the middle of the plane.".format(name))
    print("Your seat number is {}.".format(seat_numbermiddle))


def part1sub5_title_notwaitingfornextflightback(name):
    seat_numberback = random.randint(200, 300)
    print("You decide not to wait.")
    print("A flight attendant greets you as you board the plane.")
    print("Good morning {}, please make your way to the back of the plane.".format(name))
    print("Your seat number is {}.".format(seat_numberback))


# PlayAgain
def playagain():
    try:
        restart = int(input("Would you like to replay the game? yes(1) no(2) :"))
        if restart == 1:
            print("Restarting...")
            playtutorial()
        elif restart == 2:
            print("Quitting...")
            exit()
        else:
            print("Invalid answer, try again.")
    except TypeError:
        print("Invalid answer, try again.")


playtutorial()
