# KEYWORDS SECTION

# print
# print keyword is use to print numbers and characters to the console.
print_temp_string = "Hello"
print "*" * 40
print 
print "\tAditya Lesmana"
print "The string that I want to type is: %s" % print_temp_string
print 
print "*" * 40

# and
# is
# not
# or
# used for boolean operations via 'short circuit evaluation'
# notice the difference between == and is
print "None == None :", None == None 
print "None is None :", None is None
print "True is True :", True is True
print "[] == []:",[] == []
print "[] is []:",[] is []
print "\"Aditya\" == \"Aditya\":","Aditya" == "Aditya"
print "\"Aditya\" is \"Aditya\":","Aditya" is "Aditya"
no_fly_list = ["Osama", "Saddam", "Gadafi", "Palin"]
passenger = "Obama"
if passenger not in no_fly_list:
   print "Let %s fly" % passenger
   
# from
# importing a specific variable, class or a function from a module
from sys import version
print "Current python version is %r" % version

# while
# statements inside the while loop are executed, until the expression evaluates to False.
while_height = [150.5, 160.5, 155.4, 172.0]
while_sum = 0
i = len(while_height)
while (i != 0):
    i -= 1
    while_sum = while_sum + while_height[i]
print "The average height is: ", while_sum/len(while_height)

# global
# access variables defined outside functions
x = 15
def function_with_global():
   global x
   x = 45
def function_sans_global():
    x=60
function_sans_global()
print "X after function_sans_global() %d" % x
function_with_global()
print "X after function_with_global() %d" % x
print x

# if
# elif
# else
# determine, which statements are going to be executed.
age = 19
if age > 55:
    print "Driving licence revoked... too old"
elif age > 17:
    print "Driving licence issued"
else:
    print "Driving licence not permitted"
    
# break
# interrupt the cycle, if needed.
import random
break_breaker = 13
while (True):
    break_temp_integer = random.randint(10, 15)
    print "The randomly generated number is %d" % break_temp_integer
    if (break_temp_integer == break_breaker):
        break
print "Operation is stopped because of %d" % break_breaker

# import
# to import other modules into a script.
import math
print "Pi + e = %r" % (math.pi + math.e)

# as
# give a module a different name
import random as chaos
for i in range(10):
    print chaos.randint(1,1000),
    
# continue
# interrupt the current cycle, without jumping out of the whole cycle.
import random
continue_num = 0
while (continue_num < 10):
    continue_num  = continue_num  + 1
    if (continue_num  % 2) == 0:
        continue # basically start the while loop without execute the below print
    print continue_num ,

# def
# return
# to create a function
def say_hello(country, name):
    if country is "India":
        print "Namaste %s" % name
        return "%s is from India" % name
    elif country is "Japan":
        print "Konichiwa %s" % name
        return "%s is from Japan" % name
    else:
        print "Hello %s" % name
        return "%s is from unknown place" % name
origin_one = say_hello("Japan", "Kumar")
origin_two = say_hello("Singapore", "Mio")
print origin_one, origin_two

# for
# iterate over items of a collection in order that they appear in the container.
for_speech = """
When I am abroad, 
I always make it a rule never to criticize 
or attack the government of my own country. 
I make up for lost time when I come home.
"""
for_numbers = [4,1,2,5,76,9,9,0]
for i in for_speech:
    print i,
for i in for_numbers:
    print i,
print

# lambda
# creates a new anonymous function. 
# An anonymous function is a function, which is not bound to a specific name. 
# It is also called an inline function.
for i in (1, 2, 3, 4, 5):
   a =  lambda x: x * x
   print a(i),
print

# exec
# executes Python code dynamically.
command_string = "for i in [1, 2, 3]: print i,"
exec("print \"this is done via exec\"")
exec(command_string)

# in
print 4 in (2, 3, 5, 6) # this will return false
for i in range(5):
    print i,
print

# class
# create user defined class
class Person:
    age =22
    height =170
    weight = 70
i = Person()
print "Person's age is %d, height is %d, weight is %d" % (i.age, i.height, i.weight)
class Square:
    def __init__(self, x):
        self.a = x
    def area(self):
        return self.a * self.a
sq = Square(10)
print "Area of the square is %d" % sq.area()

# pass
# does nothing, useful to make placeholder VERY USEFUL
def someComplexFunctionIHaveNoIdeaHowToWrite():
    pass

# yield
# used with generators
# check more tutorial
def gen():
   x = 11
   yield x
it = gen()
print it.next()

# del
# deletes objects
employee_id = [123,566,234,892,392,132,342,985,230]
print employee_id
del employee_id[2]
print employee_id
del employee_id[:5]
print employee_id

# with
# find out more about this, basically setting some prerequisite before starting a method or provess
# see http://effbot.org/zone/python-with-statement.htm

# raise
# create a user defined exception
class SpicyException(Exception):
    def __init__(self):
        print 'So spicy'
        
# try
# try to do something
# except
# except keyword catches the exception and executes its code
# finally
# finally keyword is always executed in the end
f = None
try:
   f = open('randomFileThatDoesNotExist.txt', 'r')
   f.read()
   print
except IOError:
   print "Error reading file"
finally:
   if f:
       f.close()
       
try: 
    meal = 'Tomyam'
    print "Meal is %s" % meal
    if (meal != 'Porridge'):
        raise SpicyException
    else:
        print "So yummy and not spicy"
except SpicyException:
    print "SpicyException is catched"
finally:
    print "End of Tomyam adventure"
    
# assert
# used for debugging purposes
# for some reason, this will stop the remaining script
weight = 75
weight -= 80 #  cannot be 
assert weight > 0

# DATA TYPES SECTION

# True
# False
# Boolean values


# None
# non existent, not known or empty.

# strings
# textual data in computer programs

# numbers
# floats

# lists
# mutable sequence data type, can contain mixed data types

# Dictionaries 
# associative arrays similar to hashmap
dictionary = { 'food': 'Taco', 'gadget': 'iPad', 'phone': 'iPhone' }




# STRING ESCAPES SEQUENCES 

# \\
# backlash

# \'
# Single quote (')

# \"
# Double quote (")

# \a
# beep sound

# \b
# backspace

# \f
# page break

# \n
# new line

# \r
# carriage return

# \t
# tab

# \v
# vertical tab


# STRING FORMAT 

# %d
# %i
# %o
# %u
# %x
# %X
# %e
# %E
# %f
# %F
# %g
# %G
# %c
# %r
# %s
# %%

# OPERATORS
# Some of these may be unfamiliar to you, but look them up anyway. Find out what they do, and if you still can't figure it out, save it for later.

# +
# -
# *
# **
# /
# //
# %
# <
# >
# <=
# >=
# ==
# !=
# <>
# ( )
# [ ]
# { }
# @
# ,
# :
# .
# =
# ;
# +=
# -=
# *=
# /=
# //=
# %=
# **=


# read more http://zetcode.com/tutorials/pythontutorial/

