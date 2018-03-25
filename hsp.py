#!python

import random, time
import decimal
from resources.player import *
from resources.player_for_match import *
from resources.position import *



## MAIN ##
#random.seed(time.clock())
rng = RandomGenerator()

g = Player.generate_keeper(rng, "Italy", 5)
g.to_string()
pm = PlayerForMatch(g)

print "Adjusted Keeper: " + str(pm.adjust_skill(pm._keeper))
print "Stamina multiplier: " + str(pm.stamina_multiplier(82))
print "Keeper at given minute: " + str(pm.get_keeper(82))

pos = Keeper(pm)
#print pos.right_defence(66)






