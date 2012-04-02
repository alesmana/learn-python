ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait they are not 10 things... lets fix it"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Lets do some stuff with stuff"

print stuff[1]
print stuff[-1] # see here
print stuff.pop()
print ' '.join(stuff) # see here again # no more corn
print '#'.join(stuff[3:5]) # another cool stuff # start at index 3 (inclusive) stop at 5 (excluded)

