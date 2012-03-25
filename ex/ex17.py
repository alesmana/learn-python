from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying form %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

#exist returns True if a file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright ,all done"

output.close()
input.close()

# If you were writing to real files, your 
# operating system would limit how many open files you could have at any 
# time, so you want to make sure you close file handles you're no longer 
# using.

# apparently the above code can be shortened into one line. I will left it for next time



