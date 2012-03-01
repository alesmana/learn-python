 # -- coding: utf-8 --

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy" 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# tricky line
print "If I add %d, %d and %d I get %d." % (
  my_age, my_height, my_weight, my_age + my_height + my_weight)

  
# extra credit
# note the outut due to %r is different from %s
# check http://docs.python.org/library/stdtypes.html#string-formatting-operations

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy" 
print "He's got %r eyes and %s hair." % (eyes, hair) 
print "His teeth are usually %s depending on the coffee." % teeth

# tricky line
print "If I add %d, %d and %d I get %d." % (
  age, height, weight, age + height + weight)

# inches and pounds converter
inches_to_centimeters_factor = 2.54
pounds_to_kilos_factor = 0.45359237

inches_input = 12.0
pounds_input = 13.0

# set as basic decimal
print "%d inches == %d cm" % (inches_input, inches_to_centimeters_factor * inches_input)
print "%d pounds == %d kg" % (pounds_input, pounds_to_kilos_factor * pounds_input)

# defalt %f contains 6 decimal
print "%f inches == %f cm" % (inches_input, inches_to_centimeters_factor * inches_input)
print "%f pounds == %f kg" % (pounds_input, pounds_to_kilos_factor * pounds_input)

# set decimal to 2 
print "%.2f inches == %.2f cm" % (inches_input, inches_to_centimeters_factor * inches_input)
print "%.2f pounds == %.2f kg" % (pounds_input, pounds_to_kilos_factor * pounds_input)

