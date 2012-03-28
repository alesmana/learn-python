the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of fooor loop
for number in the_count:
    print "this is count %d" % number
    
# same same
for fruit in fruits:
    print "A fruit is a fruit like %s" % fruit
    
# loop through mix list, notice %r
for i in change:
    print "I got %r" % i
    
# buld list first start with empty one
elements = []

#  then use range
for i in range(0,6):
    print "Addint %d to the list." % i
    #append is a function for list
    elements.append(i)
    
# now we can print them too
for i in elements:
    print "Element was: %d" % i
    
    
# see http://docs.python.org/tutorial/datastructures.html for more info on list