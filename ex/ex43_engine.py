class Engine(object):

    def __init__(self, map, position):
        self.map = map
        self.position = position
        
    def play(self):
        nextlocation = self.position
        
        while True:
            print "\n--------"
            
            location = getattr(self.map, nextlocation) #IMPORTANT

            nextlocation = location()
            