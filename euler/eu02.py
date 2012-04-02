total = 0

# assuming starting point is 1 and 2
num_x = 1
num_y = 2

print "%d %d" % (num_x, num_y),
while True:        
    if num_y % 2 == 0:
        total = total + num_y
        
    num_temp = num_x + num_y
    print num_temp,
    
    if num_temp > 4000000:
        break
    
    num_x = num_y
    num_y = num_temp
    
print "total is %d" % total
        
  
    