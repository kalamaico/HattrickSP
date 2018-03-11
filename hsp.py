#!python

import random, time
import decimal
from resources.player import *



## MAIN ##
#random.seed(time.clock())
rng = RandomGenerator()

g = Player.generate_central_defender(rng, "Italy", 5)
g.to_string()




