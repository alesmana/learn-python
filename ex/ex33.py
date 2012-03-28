def basic_loop(max):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = 1 + i
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i        
    
    print "The numbers: "

    for num in numbers:     
        print num
        
def basic_loop_step(max, increment):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = increment + i
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i        
    
    print "The numbers: "

    for num in numbers:     
        print num       

def basic_loop_for_range(max):
    i = 0
    numbers = []
    for i in range(0, max):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i        
    
    print "The numbers: "

    for num in numbers:     
        print num
        
def basic_loop_for_range_step(max,increment):
    i = 0
    numbers = []
    for i in range(0, max, increment):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i        
    
    print "The numbers: "

    for num in numbers:     
        print num        

basic_loop(8)
basic_loop_step(10,2)
basic_loop_for_range(20)
basic_loop_for_range_step(20,5)

    

    