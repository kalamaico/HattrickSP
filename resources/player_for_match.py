import math

class PlayerForMatch:
    def __init__(self, player):
        self._id = player._id
        self._name = player._name
        
        # Basic Skills
        self._keeper = player._keeper
        self._defending = player._defending
        self._playmaking = player._playmaking
        self._winger = player._winger
        self._scoring = player._scoring
        self._passing = player._passing
        self._setpieces = player._setpieces
        self._stamina = player._stamina
        
        # Other skills
        self._experience = player._experience
        self._charisma = player._charisma
        self._loyalty = player._loyalty
        self._motherclub = player._motherclub
        self._character = player._character
        self._moral = player._moral
        self._form = player._form
        
    def get_keeper(self, minute):
        return self.adjust_skill(self._keeper) * self.stamina_multiplier(minute)
        
    def get_defending(self, minute):
        return self.adjust_skill(self._defending) * self.stamina_multiplier(minute)
        
    def get_winger(self, minute):
        return self.adjust_skill(self._winger) * self.stamina_multiplier(minute)
        
    def get_scoring(self, minute):
        return self.adjust_skill(self._scoring) * self.stamina_multiplier(minute)
        
    def get_passing(self, minute):
        return self.adjust_skill(self._passing) * self.stamina_multiplier(minute)
        
    def get_setpieces(self, minute):
        return self.adjust_skill(self._setpieces) * self.stamina_multiplier(minute)
        
    def get_playmaking(self, minute):
        return self.adjust_skill(self._playmaking) * self.stamina_multiplier(minute)        
        
# Private helper methods        

    def stamina_multiplier(self, minute):
        #return 1
        #((stamina+6.5)/14)^0.6 
        
        if minute <= 45:
            return self.stamina_first_half(minute)
        else:  
            return self.stamina_second_half(minute)
        # TODO for overtime
            
        
    # minute at which stamina starts to fall
    def stamina_first_half(self, minute):
        if minute < 0 or minute > 45:
            raise Exception("Minute must be between 0 and 45")
            
        max_minutes = { 1:10, 2:15, 3:20, 4:25, 5:30, 6:35, 7:40, 8:45, 9:45 }
        drop_point = 0
        
        if self._stamina >= 8:
            drop_point = 45
        else:
            # compute at which minute stamina starts to fall
            base = math.floor(self._stamina)
            fractional = self._stamina % 1
            left = max_minutes[base]
            right = max_minutes[base+1]
            # 1 : (right - left) = fractional : x
            drop_point = left + math.floor((right - left) * fractional)
            
        if minute < drop_point:
            return 1
        else:
            return 1 - 0.01 * (minute - drop_point)
            
    def stamina_second_half(self, minute):
        if minute < 46 or minute > 90:
            raise Exception("Minute must be between 0 and 45")
            
        max_minutes = { 1:45, 2:45, 3:45, 4:45, 5:45, 6:50, 7:60, 8:70, 9:80 }
        starting_value = { 1:0.8, 2:0.85, 3:0.9, 4:0.95, 5:1, 6:1, 7:1, 8:1 }
        
        base = math.floor(self._stamina)
        fractional = self._stamina % 1
        left = max_minutes[base]
        right = max_minutes[base+1]
        drop_point = left + math.floor((right - left) * fractional)
        
        print starting_value[base]
        print drop_point
        print 0.01 * (minute - drop_point)
        
        if minute < drop_point:
            return starting_value[base]
        else:
            return starting_value[base] - 0.01 * (minute - drop_point)
        
        
        
    def adjust_skill(self, skill):
        return (skill + self.add_experience() + self.add_motherclub() + self.add_loyalty() ) * self.form_multiplier()
        
    def add_experience(self):
        return math.log(self._experience) * 4/3
        
    def add_motherclub(self):
        if self._motherclub == True:
            return 0.5
        else:
            return 0
            
    def form_multiplier(self):
        f = math.pow( (self._form-0.5)/7, 0.45)
        if f > 1:
            return 1
        else:
            return f
            
    def add_loyalty(self):
        return self._loyalty / 20
        

        
