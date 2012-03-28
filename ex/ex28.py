print "%r is true" % (True and True)
print "%r is false" % (False and True)
print "%r is false" % (1==1 and 2==1)
print "%r is true" % ("test" == "test")
print "%r is true" % (1 == 1 or 2 != 1)
print "%r is true" % (True and 1 == 1)
print "%r is false" % (False and 0 != 0)
print "%r is true" % (True or 1 == 1)
print "%r is false" % ("test" == "testing")
print "%r is false" % (1 != 0 and 2 == 1)
print "%r is true" % ("test" != "testing")
print "%r is false" % ("test" == 1)

print "%r is true" % (not (True and False))
print "%r is false" % (not (1 == 1 and 0 != 1))
print "%r is false" % (not (10 == 1 or 1000 == 1000))
print "%r is false" % (not (1 != 10 or 3 == 4))
print "%r is true" % (not ("testing" == "testing" and "Zed" == "Cool Guy"))
print "%r is true" % (1 == 1 and not ("testing" == 1 or 1 == 0))
print "%r is false" % ("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print "%r is false" % (3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))












