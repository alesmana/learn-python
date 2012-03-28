people = 30
cars = 40
buses = 15

if cars > people: 
    print "We should take the cars" 
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide"
    
if buses > cars: 
    print "So many bus"
elif buses < cars:
    print "Maybe we could take the bus"
else: 
    print "Uh oh!"
    
if people > buses: 
    print "Alrite, lets take buses"
else: 
    print "Fine, lets stay home then"