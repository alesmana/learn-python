class Engine(object):

    def __init__(self, map, position):
        self.map = map
        self.position = position
        
    def play(self):
        next_location = self.position
        
        while True:
            print "\n--------"
            
            location = getattr(self.map, next_location) #IMPORTANT

            # get the next_location from map.xxx() method
            next_location = location()
            