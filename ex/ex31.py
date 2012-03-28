print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take a cake"
    print "2. Scream at the bear"
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face" 
    elif bear == "2":
        print "The bear eats your legs" 
    else: 
        print "Well, doing %s is better. Bear runs" % bear
        
elif door == "2":
    print "You stare at Cthulu eyes" 
    print "1. Blueberies"
    print "2. yellow jackets" 
    print "3. Understanding revolvers"
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body is jello"
    else: 
        print "The insanity glob you"
        
else: 
    print "You fall and die"