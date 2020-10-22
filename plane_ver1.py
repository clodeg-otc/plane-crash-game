# THIS IS A TEST
import itertools
import threading
import time
import sys
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
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            tutorial1()
        elif playtutorialchoice == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            # animation
            time.sleep(2)
            print("")
            tutorial3()
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            # animation
            time.sleep(2)
            print("")
            print("1Invalid answer, try again.")
            playtutorial1()
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rloading ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rAnswer verified.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        # animation
        time.sleep(2)
        print("")
        print("Invalid answer, try again.")
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
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            # animation
            time.sleep(2)
            print("")
            print("Next, your name will be asked.")
            time.sleep(3)
            tutorial2()
        elif test1 == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            # animation
            time.sleep(2)
            print("")
            tutorial3()
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            # animation
            time.sleep(2)
            print("")
            print("Invalid answer, try again.")
            tutorial1()
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rloading ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rAnswer verified.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        # animation
        time.sleep(2)
        print("")
        print("Invalid answer, try again.")
        tutorial1()


def tutorial2():
    name = str(input("What is your name? :"))
    # animation
    done = False

    def animate():
        for c in itertools.cycle(['...', '..', '.']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rAnswer verified.')

    t = threading.Thread(target=animate)
    t.start()
    # long process here
    time.sleep(2)
    done = True
    # animation
    time.sleep(2)
    print("")
    print("Ok {}, you have completed the introduction.".format(name))
    time.sleep(3)
    print("The game will now begin.")
    time.sleep(3)
    part1sub1(name)


def tutorial3():
    try:
        exit1 = int(input("Are you sure? yes(1) no(2) :"))
        if exit1 == 1:
            print("Ok, exiting game.")
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            exit()
        elif exit1 == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            tutorial1()
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rAnswer verified.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("Invalid answer, try again.")
            tutorial3()
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rloading ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rAnswer verified.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        time.sleep(2)
        print("")
        # animation
        print("Invalid answer, try again.")
        tutorial3()


def part1sub1(name):
    print("\n")
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
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("You have chosen to sit in the front of the plane.")
            time.sleep(3)
            print("For future knowledge, try to get a seat at the back of the plane next time.")
            time.sleep(3)
            print("It is proven that the chances of survival in the rear of the plane")
            time.sleep(3)
            print("are much higher than in the front.")
            time.sleep(3)
            part1sub3front(name)
        elif seat_choice == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("You have chosen to sit in the middle of the plane.")
            time.sleep(3)
            print("This is a reasonable choice, however, the rear of the plane offers")
            time.sleep(3)
            print("a higher chance of survival in a plane crash.")
            time.sleep(3)
            part1sub3middle(name)
        elif seat_choice == 3:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("You have chosen to sit in the back of the plane.")
            time.sleep(3)
            print("This is a great choice. In the rear of the plane,")
            time.sleep(3)
            print("chances of survival in a plane crash are proven to be")
            time.sleep(3)
            print("far higher than anywhere else.")
            time.sleep(3)
            part1sub3back(name)
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("Invalid answer, try again.")
            part1sub2(name)
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rRedirecting to last question' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rComplete.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        time.sleep(2)
        print("")
        # animation
        print("Invalid answer, try again.")
        part1sub2(name)


def part1sub3front(name):
    print("Ticket in hand, you make your way over to the docking port.")
    time.sleep(3)
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    time.sleep(3)
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            part1sub5_title_notwaitingfornextflightfront(name)
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("Invalid answer, try again.")
            part1sub3front(name)
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rRedirecting to last question' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rComplete.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        time.sleep(2)
        print("")
        # animation
        print("Invalid answer, try again.")
        part1sub3front(name)


def part1sub3middle(name):
    print("Ticket in hand, you make your way over to the docking port.")
    time.sleep(3)
    print("You take a quick glance out the window, and notice gray clouds in the distance.")
    time.sleep(3)
    try:
        waitfornextflight = int(input("Should you wait for the next flight? yes(1) no(2) :"))
        if waitfornextflight == 1:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            part1sub5_title_waitingfornextflight()
        elif waitfornextflight == 2:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            part1sub5_title_notwaitingfornextflightmiddle(name)
        else:
            # animation
            done = False

            def animate():
                for c in itertools.cycle(['...', '..', '.']):
                    if done:
                        break
                    sys.stdout.write('\rRedirecting to last question' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rComplete.')

            t = threading.Thread(target=animate)
            t.start()
            # long process here
            time.sleep(2)
            done = True
            time.sleep(2)
            print("")
            # animation
            print("Invalid answer, try again.")
            part1sub3middle(name)
    except ValueError:
        # animation
        done = False

        def animate():
            for c in itertools.cycle(['...', '..', '.']):
                if done:
                    break
                sys.stdout.write('\rRedirecting to last question' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rComplete.')

        t = threading.Thread(target=animate)
        t.start()
        # long process here
        time.sleep(2)
        done = True
        time.sleep(2)
        print("")
        # animation
        print("Invalid answer, try again.")
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
            print("Invalid answer, try again.")
            part1sub3back(name)
    except ValueError:
        print("Invalid answer, try again.")
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
    print("'Good morning {}, please make your way to the front of the plane.'".format(name))
    time.sleep(3)
    print("'Your seat allocation is section A, {}.'".format(seat_numberfront))
    time.sleep(3)
    part2sub1(name)


def part1sub5_title_notwaitingfornextflightmiddle(name):
    seat_numbermiddle = random.randint(100, 199)
    print("You decide not to wait.")
    time.sleep(3)
    print("A flight attendant greets you as you board the plane.")
    time.sleep(3)
    print("'Good morning {}, please make your way to the middle of the plane.'".format(name))
    time.sleep(3)
    print("'Your seat allocation is section B, {}.'".format(seat_numbermiddle))
    time.sleep(3)
    part2sub1(name)


def part1sub5_title_notwaitingfornextflightback(name):
    seat_numberback = random.randint(200, 300)
    print("You decide not to wait.")
    time.sleep(3)
    print("A flight attendant greets you as you board the plane.")
    time.sleep(3)
    print("'Good morning {}, please make your way to the back of the plane.'".format(name))
    time.sleep(3)
    print("'Your seat allocation is section C, {}.'".format(seat_numberback))
    time.sleep(3)
    part2sub1(name)


def part2sub1(name):
    print("\n")
    print("PART 2: THE PLANE")
    print("Warning: Unrealistic gameplay ahead [JUST FOR THIS PART])")
    print("\n")
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
            time.sleep(3)
            print("if she could have a choco bikkie.")
            time.sleep(3)
            print("You trample over her.")
            time.sleep(3)
            part2sub3()
        else:
            print("Invalid answer, try again.")
            part2sub2()
    except ValueError:
        print("Invalid answer, try again.")
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
            print("Invalid answer, try again.")
            part2sub3()
    except ValueError:
        print("Invalid answer, try again.")
        part2sub3()


def part2sub4():
    print("\n")
    print("PART 3: THE CRASH")
    print("\n")
    time.sleep(3)
    print("You make your way back to your seat.")
    time.sleep(3)
    print("You go to grab your water, but the plane starts to shake.")
    time.sleep(3)
    print("It stops for a moment. What is going on?")
    time.sleep(3)
    print("A large BOOM comes from the right wing of the plane.")
    time.sleep(3)
    print("You look out the window and see the wing; IT'S ON FIRE!?!?")
    time.sleep(3)
    print("The plane begins to decline towards the ground;")
    time.sleep(3)
    print("Oxygen masks fall from the roof of the plane,")
    time.sleep(3)
    print("and the pilots announce that everyone should prepare for impact.")
    time.sleep(3)
    print("You are about to crash into the ocean.")
    time.sleep(3)
    print("The pilots, in an obviously panicked state,")
    time.sleep(3)
    print("ask all passengers to stay seated, for their safety.")
    time.sleep(3)
    print("What are you going to do?")
    time.sleep(3)
    print("Stay seated, or go to see what is going on?")
    time.sleep(3)
    part3sub1()


def part3sub1():
    part2sub4choice1 = int(input("Stay seated(1) Get up(2) :"))
    try:
        if part2sub4choice1 == 1:
            print("You remain in your seat.")
            time.sleep(3)
            print("As you decline towards the ground,")
            time.sleep(3)
            print("the sudden feeling of death fills your mind.")
            time.sleep(3)
            print("You are going to die.")
            time.sleep(3)
            print("Suddenly, the pilot makes another announcement.")
            time.sleep(3)
            print("'This is the captain.'")
            time.sleep(3)
            print("'Brace for impact.'")
            time.sleep(3)
            print("Suddenly everything becomes very clear.")
            time.sleep(3)
            print("You need to prepare for what you're going to do when you hit the water.")
            time.sleep(3)
            print("LOOK! an emergency manual is slotted in the side of your chair.")
            time.sleep(3)
            print("You pick it up, quickly reading over it 2 or 3 times,")
            time.sleep(3)
            print("before bracing in your chair.")
            time.sleep(3)
            print("You hold onto the seat belt, clutching for your life...")
            time.sleep(3)
            print("The impact from hitting the surface of the ocean")
            time.sleep(3)
            print("knocks you out, rendering you unconscious.")
            time.sleep(3)
            print("You awaken to the plane burning from the inside.")
            time.sleep(3)
            print("Its aluminium frame crumbles, dissolving very quickly.")
            time.sleep(3)
            print("Having the knowledge you have from the emergency manual,")
            time.sleep(3)
            print("You make your way to the emergency exit door.")
            time.sleep(3)
            print("A woman attempts to open it, but you can see that she is pulling")
            time.sleep(3)
            print("it incorrectly, making it impossible for her to open it.")
            time.sleep(3)
            print("You walk up to her, and shout over the flames,")
            time.sleep(3)
            print("'You have to pull the mechanism down!'")
            time.sleep(3)
            print("You pull it down, and make your way out of the plane.")
            time.sleep(3)
            print("You jump onto a life raft.")
            time.sleep(3)
            print("Time goes by, for what seems like hours.")
            time.sleep(3)
            print("Eventually, emergency services make it out to you.")
            time.sleep(3)
            print("Well done. You survived.")
            time.sleep(3)
            index()
        elif part2sub4choice1 == 2:
            print("You get out of your seat, and rush towards the flight attendant.")
            time.sleep(3)
            print("'What's going on!?!?' you ask.")
            time.sleep(3)
            print("'The right plane wing caught on fire!'")
            time.sleep(3)
            print("'You need to get back in your seat!' says the flight attendant.")
            time.sleep(3)
            print("You ignore her; the plane rumbles violently, tossing you over a seat.")
            time.sleep(3)
            print("")
        else:
            print("Invalid answer, try again.")
            part3sub1()
    except ValueError:
        print("Invalid answer, try again.")
        part3sub1()


def index():
    print("\n")
    print("INDEX:")
    print("\n")
    time.sleep(3)
    print("(1): The survival rate of plane crashes is approximately 95.7%.")
    time.sleep(3)
    print("(2): When you hit the water, on average you have approximately 90 seconds to get out of the plane.")
    time.sleep(3)
    print("(This is because the aluminium fuselage in the plane burns very quickly).")
    time.sleep(3)
    print(
        "(3): When in a plane crash situation, read the emergency manual supplied, and listen to the flight attendants.")
    time.sleep(3)
    print(
        "(4) Brace for impact in the SAFETY POSITION (Check website https://www.cbsnews.com/news/how-to-survive-a-plane-crash/)")
    time.sleep(3)
    print("(5): Watch the conditions before you hop on; It may be safer to get a later flight.")
    time.sleep(3)
    print("(6): Try to get a seat in the back of the plane, as this will increase your chances of survival.")
    time.sleep(3)
    playagain()


# PlayAgain
def playagain():
    try:
        print("\n")
        restart = int(input("Would you like to replay the game? yes(1) no(2) :"))
        if restart == 1:
            print("Restarting...")
            playtutorial()
        elif restart == 2:
            print("Quitting...")
            quit()
        else:
            print("Invalid answer, try again.")
            playagain()
    except ValueError:
        print("Invalid answer, try again.")
        playagain()


playtutorial()
