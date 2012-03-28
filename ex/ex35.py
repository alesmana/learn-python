from sys import exit

def gold_room():
    print "So many gold. Take some?"
    next = raw_input("> ")
    
    try:
        how_much = int(next)
    except ValueError:
        dead("Learn to type a number") #interesting
    
    if how_much < 50:
        print "Not greedy. Win"
        exit(0)
    else:
        dead("Greedy die")

def bear_room():
    print "Got bear with tons of honey"
    print "Fat bear block a door"
    print "How do you plan to move the bear"
    bear_moved = False
    
    while True: 
        next = raw_input("> ")
        
        if next == "take honey":
            dead("Bear sees bear kills you")
        elif next == "taunt bear" and not bear_moved:
            print "Bear moved"
            bear_moved = True
        elif next == "Taunt bear" and bear_moved:
            dead("Bear pissed and kills you")
        elif next == "Open door" and bear_moved:
            gold_room()
        else:
            print "huh?"
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
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

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()