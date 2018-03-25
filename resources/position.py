#!python

class Position:
    def __init__(self, player):
        self.player = player
    
    def right_defence(self):
        raise NotImplementedError()
        
    def left_defence(self):
        raise NotImplementedError()
        
    def central_defence(self):
        raise NotImplementedError()
        
    def midfield(self):
        raise NotImplementedError()
        
    def right_attack(self):
        raise NotImplementedError()
        
    def left_attack(self):
        raise NotImplementedError()
        
    def central_attack(self):
        raise NotImplementedError()
        
    def offensive_sp(self):
        raise NotImplementedError()
        
    def defensive_sp(self):
        raise NotImplementedError()
        
    
class Keeper(Position):
    def right_defence(self, minute):
        return self.player.get_keeper(minute)
        
    def left_defence(self):
        return 0
        
    def central_defence(self):
        return 0
        
    def midfield(self):
        return 0
        
    def left_attack(self):
        return 0
        
    def right_attack(self):
        return 0
        
    def central_attack(self):
        return 0
        
    def offensive_sp(self):
        return 0
        
    def defensive_sp(self):
        return 0
        
        
# TODO define all other positions
