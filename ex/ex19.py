def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Wow, that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine both variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10)

# Write at least one more function of your own design, and run it 10 different ways.

def walkers_and_ammo(number_of_walkers, number_of_ammo):
    print "You have %d ammo" % number_of_ammo
    print "%d walkers are coming after you" % number_of_walkers
    if number_of_walkers > number_of_ammo:
        print "You are screwed"
    elif number_of_walkers == number_of_ammo:
        print "Make every shot counts"
    else: 
        print "Keep shooting"
      
print "Running walkers and ammo"
walkers_and_ammo(100,100)