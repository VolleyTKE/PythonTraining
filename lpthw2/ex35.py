from sys import exit
world_travel = False

def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input("> "))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break


def gold_room():
    print "this room is full of gold. How much do you take?"
    how_much = 0
    how_much = inputNumber(input)

    if how_much < 50 and how_much != 2:
        print "Nice, you're not greedy, you win!"
        exit(0)
    elif how_much == 2 and not world_travel:
        secret_room()
    else:
        print world_travel
        dead("you greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "the bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        global world_travel
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def secret_room():
    print "You are transported to an awesome place"
    print """\tIt Says: \nNo man has the right to be an amateur in the matter of physical training.\n
        It is a shame for a man to grow old without seeing the beauty and strength of which his body is capable."""

    dead("SUPER WINNER")
    exit(0)

start()
