# Here are your requirements:
# Make a different game from the one I made.
# Use more than one file, and use import to use them. Make sure you know what that is.
# Use one class per room and give the classes names that fit their purpose. Like GoldRoom, KoiPondRoom.
# Your runner will need to know about these rooms, 
# so make a class that runs them and knows about them. 
# There's plenty of ways to do this, but consider having 
# each room return what room is next or setting a variable of what 
# room is next.

# this file will be the runner
# ex43_engine and ex43_world are the broken down classes

from ex43_world import *
from ex43_engine import *

current_map = Map()

current_engine = Engine(current_map, current_map.starting_point)

current_engine.play()