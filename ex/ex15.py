# import argv module
from sys import argv

# put argv into variables. note first one is alwayws script
script, filename = argv

# open file 
txt = open(filename)

# just make sure the name is ok
print "Here's your file %r:" % filename

# churn out the content of the file
print txt.read()

txt.close() # important

# repeat but with prompt 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close() #important

# windows user
# look python -m pydoc file 