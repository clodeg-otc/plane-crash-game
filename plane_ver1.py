# THIS IS A TEST
import time
import random


def playtutorial():
    print("This game will inform you on how to better your chances of surviving a plane crash.")
    time.sleep(3)
    print("For more information, visit https://www.cbsnews.com/news/how-to-survive-a-plane-crash/")
    time.sleep(3)
    print("\n")
    print("How to survive a plane crash! (Created by Griffin Chode)")
    time.sleep(3)
    playtutorial1()

def playtutorial1():
    try:
        playtutorialchoice = int(input("Would you like to go play through the tutorial? yes(1) no(2) :"))
        if playtutorialchoice == 1:
            print("Ok.")
            time.sleep(3)
            tutorial1()
        elif playtutorialchoice == 2:
            print("Ok.")
            time.sleep(3)
            tutorial2()
        else:
            print("1Invalid answer, try again.")
            playtutorial1()
    except:
        print("2Invalid answer, try again.")
        playtutorial1()


def tutorial1():
    print("This game involves multiple choice questions.")
    time.sleep(3)
    print("To select one of the choices, you must choose the number that is assigned to that choice.")
    time.sleep(3)
    print("A test question will now be asked.")
    time.sleep(3)
    try:
        test1 = int(input("Would you like to play the game? yes(1) no(2) :"))
        if test1 == 1:
            print("Great.")
            time.sleep(3)
            print("Next, your name will be asked.")
            time.sleep(3)
            tutorial2()
        elif test1 == 2:
            tutorial3()
        else:
            print("3Invalid answer, try again.")
            tutorial1()
    except:
        print("4Invalid answer, try again.")
        tutorial1()


def tutorial2():
    name = str(input("What is your name? :"))
    print("Ok {}, you have completed the tutorial.".format(name))
    time.sleep(3)
    print("The game will now begin.")
    time.sleep(3)
    part1sub1(name)


def tutorial3():
    try:
        exit1 = int(input("Are you sure? yes(1) no(2) :"))
        if exit1 == 1:
            print("Ok, exiting game.")
            exit
        elif exit1 == 2:
            print("Ok, you will now be redirected to the last question.")
            time.sleep(3)
            tutorial1()
        else:
            print("5Invalid answer, try again.")
            tutorial3()
    except:
        print("6Invalid answer, try again.")
        tutorial3()


def part1sub1(name):
    print("GAME START")
    time.sleep(3)
    print("PART 1: WAITING FOR THE PLANE")
    time.sleep(3)
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
    time.sleep(3)
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
    print("With an authoritative tone of voice, he asks;")
    time.sleep(3)
    print("'What part of the plane would you like to be seated in, {}?'".format(name))
    time.sleep(3)
    part1sub2(name)


def part1sub2(name):
    try:
        seat_choice = int(input("Front of the plane(1) Middle of the plane(2) Back of the plane(3) :"))
        if seat_choice == 1:
            print("You have chosen to sit in the front of the plane.")
            time.sleep(3)
            print("For future knowledge, try to get a seat on at the back of the plane next time.")
            time.sleep(3)
            print("It is proven that the chances of survival in the rear of the plane")
            print("are much higher than in the front.")
            time.sleep(3)
            part1sub3front(name)
        elif seat_choice == 2:
            print("You have chosen to sit in the middle of the plane.")
            time.sleep(3)
            print("This is a reasonable choice, however, the rear of the plane offers")
            print("a higher chance of survival in a plane crash.")
            time.sleep(3)
            part1sub3middle(name)
        elif seat_choice == 3:
            print("You have chosen to sit in the back of the plane.")
            time.sleep(3)
            print("This is a great choice. In the rear of the plane,")
            print("chances of survival in a plane crash are proven to be")
            print("far higher.")
            time.sleep(3)
            part1sub3back(name)
        else:
            print("7Invalid answer, try again.")
            part1sub2(name)
    except:
        print("8Invalid answer, try again.")
        part1sub2(name)


def part1sub3front(name):
    print("Ticket in hand, you make your way over to the docking port.")
    time.sleep(3)
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    time.sleep(3)
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightfront(name)
        else:
            print("9Invalid answer, try again.")
            part1sub3front(name)
    except:
        print("10Invalid answer, try again.")
        part1sub3front(name)


def part1sub3middle(name):
    print("Ticket in hand, you make your way over to the docking port.")
    time.sleep(3)
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    time.sleep(3)
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightmiddle(name)
        else:
            print("11Invalid answer, try again.")
            part1sub3middle(name)
    except:
        print("12Invalid answer, try again.")
        part1sub3middle(name)


def part1sub3back(name):
    print("Ticket in hand, you make your way over to the docking port.")
    time.sleep(3)
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    time.sleep(3)
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            part1sub5_title_notwaitingfornextflightback(name)
        else:
            print("13Invalid answer, try again.")
            part1sub3back(name)
    except:
        print("14Invalid answer, try again.")
        part1sub3back(name)


def part1sub5_title_waitingfornextflight():
    print("You decide that it is probably safest to wait.")
    time.sleep(3)
    print("You don't want to fly in dangerous weather now, do you?")
    time.sleep(3)
    print("You wait, for hours. Eventually, you board the next flight.")
    time.sleep(3)
    print("As you're boarding, you look up at the announcement screen.")
    time.sleep(3)
    print("The flight you had scheduled for crashed in the pacific, with only 26 survivors.")
    time.sleep(3)
    print("Sometimes, the best preventative action you can take")
    print("is to simply get a different flight, depending on the conditions.")
    time.sleep(3)
    playagain()


def part1sub5_title_notwaitingfornextflightfront(name):
    seat_numberfront = random.randint(1, 99)
    print("You decide not to wait.")
    time.sleep(3)
    print("A flight attendant greets you as you board the plane.")
    time.sleep(3)
    print("Good morning {}, please make your way to the front of the plane.".format(name))
    time.sleep(3)
    print("Your seat number is section A, {}.".format(seat_numberfront))
    time.sleep(3)
    part2sub1(name)


def part1sub5_title_notwaitingfornextflightmiddle(name):
    seat_numbermiddle = random.randint(100, 199)
    print("You decide not to wait.")
    time.sleep(3)
    print("A flight attendant greets you as you board the plane.")
    time.sleep(3)
    print("Good morning {}, please make your way to the middle of the plane.".format(name))
    time.sleep(3)
    print("Your seat number is section B, {}.".format(seat_numbermiddle))
    time.sleep(3)
    part2sub1(name)


def part1sub5_title_notwaitingfornextflightback(name):
    seat_numberback = random.randint(200, 300)
    print("You decide not to wait.")
    time.sleep(3)
    print("A flight attendant greets you as you board the plane.")
    time.sleep(3)
    print("Good morning {}, please make your way to the back of the plane.".format(name))
    time.sleep(3)
    print("Your seat number is section C, {}.".format(seat_numberback))
    time.sleep(3)
    part2sub1(name)

def part2sub1(name):
    print("PART 2: THE PLANE")
    time.sleep(3)
    print("You make yourself comfortable in your seat.")
    time.sleep(3)
    print("The plane begins to take off with a large rumbling sound.")
    time.sleep(3)
    print("Strange. You didn't expect it to sound like that.")
    time.sleep(3)
    print("You ignore it, and lie back in the chair...")
    time.sleep(3)
    print("The sudden sound of boisterous children awake you.")
    time.sleep(3)
    print("You had fallen asleep.")
    time.sleep(3)
    print("'Hello {}, would you like a glass of water?', the flight attendant asks.".format(name))
    time.sleep(3)
    print("You try to reply, but your throat is raspy and sore.")
    time.sleep(3)
    print("'Ok, you obviously need water. Here you go.'")
    time.sleep(3)
    print("You take the glass of water, and have a phat chug of it.")
    time.sleep(3)
    print("The urge to relieve yourself in the restroom is intense.")
    time.sleep(3)
    print("RUN to the bathroom!")
    time.sleep(3)
    print("children are in your way!")
    time.sleep(3)
    print("go left to get around them, or right?")
    part2sub2()

def part2sub2():
    part2sub2choice1 = int(input("left(1) right(2) :"))
    try:
        if part2sub2choice1 == 1:
            print("You turn left and keep running...")
            time.sleep(3)
            print("a SUITCASE falls on you!")
            time.sleep(3)
            print("You begin running again, obviously at a slower rate.")
            time.sleep(3)
            part2sub3()
        elif part2sub2choice1 == 2:
            print("You dodge to the right...")
            time.sleep(3)
            print("Hitting an old lady on her way to ask the flight attendant")
            print("if she could have a choco bikkie.")
            time.sleep(3)
            print("You trample over her.")
            time.sleep(3)
            part2sub3()
        else:
            print("15Invalid answer, try again.")
            part2sub2()
    except:
        print("16Invalid answer, try again.")
        part2sub2()

def part2sub3():
    print("The flight attendant is in your way!")
    time.sleep(3)
    print("Run around her, or ask her to move out of the way?")
    part2sub3choice1 = int(input("Run around(1) Ask to move(2) :"))
    try:
        if part2sub3choice1 == 1:
            print("You try to run around the flight attendant,")
            print("but fail miserably.")
            time.sleep(3)
            print("You fall, hitting the side of")
            print("a chair, cracking your skull.")
            time.sleep(3)
            print("You die. Next time, try to be more polite.")
            time.sleep(3)
            playagain()
        elif part2sub3choice1 == 2:
            print("You politely ask the flight attendant to move out of the way.")
            time.sleep(3)
            print("She does, and passes you a choco bikkie on your way.")
            time.sleep(3)
            print("You manage to get to the toilet and relieve yourself.")
            time.sleep(3)
            part2sub4()
        else:
            print("17Invalid answer, try again.")
            part2sub3()
    except:
        print("18Invalid answer, try again.")
        part2sub3()

def part2sub4():
    print("You make your way back to your seat.")
    print("You go to grab your water, but the plane starts to shake.")
    print("It stops for a moment. What is going on?")
    print("A large BOOM comes from the right wing of the plane.")
    print("You look out the window and see the wing; IT'S ON FIRE!?!?")
    print("The plane begins to decline towards the ground;")
    print("Oxygen masks fall from the roof of the plane,")
    print("and the pilots announce that everyone should prepare for impact.")
    print("You are about to crash into the ocean.")
    print("The pilots, in an obviously panicked state,")
    print("ask all passengers to ")
    print("What are you going to do?")
    part2sub4choice1 = int(input("")

# PlayAgain
def playagain():
    try:
        restart = int(input("Would you like to replay the game? yes(1) no(2) :"))
        if restart == 1:
            print("Restarting...")
            playtutorial()
        elif restart == 2:
            print("Quitting...")
            quit()
        else:
            print("15Invalid answer, try again.")
            playagain()
    except TypeError:
        print("16Invalid answer, try again.")
        playagain()

playtutorial()
