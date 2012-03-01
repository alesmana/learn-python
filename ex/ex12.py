#see ex11 for comparison

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
    
# finding out raw_input using 
# UNIX: pydoc raw_input
# WINDOWS: python -m pydoc raw_input 

# http://docs.python.org/library/pydoc.html
# The pydoc module automatically generates documentation from P
# ython modules. The documentation can be presented as pages of text on 
# the console, served to a Web browser, or saved to HTML files.