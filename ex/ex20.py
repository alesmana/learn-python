from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind like a tape" 

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# finding out file using 
# UNIX: pydoc file
# WINDOWS: python -m pydoc file

# seek(...)
#     seek(offset[, whence]) -> None.  Move to new file position.
#
#     Argument offset is a byte count.  Optional argument whence defaults to
#     0 (offset from start of file, offset should be >= 0); other values are 1
#     (move relative to current position, positive or negative), and 2 (move
#     relative to end of file, usually negative, although many platforms allow
#     seeking beyond the end of a file).  If the file is opened in text mode,
#     only offsets returned by tell() are legal.  Use of other offsets causes
#     undefined behavior.
#     Note that not all file objects are seekable.
