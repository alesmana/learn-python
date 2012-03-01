from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# see http://docs.python.org/library/functions.html#open for more info
# w is for writing operation by default, open is just for read 
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!" 
# actually, this one is not needed
target.truncate() #delete existing 'filename' file


print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# EXTRA: open the file that has just created 
txt = open(filename)
print "\n" * 2
print "You have just written this to %s" % filename
print txt.read()
txt.close()
