#!python

from resources.random_generator import *

class Player:
    def __init__(self, pid, name, age, days, nationality, keeper, defending, playmaking, winger, scoring, passing, setpieces, stamina, experience, charisma, loyalty, motherclub, character, moral, form):
        self._id = pid
        self._name = name
        self._age = age
        self._days = days
        self._nationality = nationality
        
        # Basic Skills
        self._keeper = keeper
        self._defending = defending
        self._playmaking = playmaking
        self._winger = winger
        self._scoring = scoring
        self._passing = passing
        self._setpieces = setpieces
        self._stamina = stamina
        
        # Other skills
        self._experience = experience
        self._charisma = charisma
        self._wage = Player.compute_wage()
        self._loyalty = loyalty
        self._motherclub = motherclub
        self._injury = 0
        self._character = character
        self._moral = moral
        self._form = form

        
    def to_string(self):
        print "id: " + str(self._id)
        print "Name: " + self._name
        print "Nationality: " + str(self._nationality)
        print "Age: " + str(self._age) + "." + str(self._days)
        print "Keeper: " + str(self._keeper)
        print "Defending: " + str(self._defending)
        print "Winger: " + str(self._winger)
        print "Playmaking: " + str(self._playmaking)
        print "Scoring: " + str(self._scoring)
        print "Passing: " + str(self._passing)
        print "Set Pieces: " + str(self._setpieces)
        print "Stamina: " + str(self._stamina)
        print "Experience: " + str(self._experience)
        print "Charisma: " + str(self._charisma)
        print "Wage: " + str(self._wage)
        print "Loyalty: " + str(self._loyalty)
        print "Mother Club: " + str(self._motherclub)
        print "Injury: " + str(self._injury)
        print "Character: " + str(self._character)
        print "Moral: " + str(self._moral)
        print "Form: " + str(self._form)
        
        
#############################
# Player generation methods #
#############################
        
    @classmethod
    def compute_wage(cls):
        return 0
        
    @classmethod
    def generate_name(cls, nationality):
        return "Name Surname"
        
    @classmethod
    def generate_age(cls, rng, level):
        age = rng.generate_int(17 + 2*level,34)
        days = rng.generate_int(0,111)
        return (age, days)
        
    @classmethod
    def generate_charisma(cls, rng):
        val = rng.generate_uniform(0,1)
        if val > 0.95:
            return 7
        elif val > 0.8:
            return 6
        else:
            return rng.generate_int(1,5)
      
    @classmethod
    # Output is an int [0,5]
    def generate_character_and_moral(cls, rng):
        val = rng.generate_uniform(0,1)
        if val > 0.8:
            return 5
        elif val < 0.2:
            return 1
        elif val > 0.6:
            return 4
        elif val < 0.4:
            return 2
        else:
            return 3
            
            
    @classmethod
    def check_level(cls, level):
        if level < 0 or level > 5:
            raise Exception("Level must be between 0 and 5")

    @classmethod
    def generate_main_skill(cls, rng, level):
        Player.check_level(level)
        skill = 4 + 2*level
        val = rng.generate_uniform(0,1)
        decimals = rng.generate_uniform(0,1)
        if val > 0.8:
            return skill + 1
        elif val > 0.2:
            return skill + decimals
        else:
            return skill - 1 + decimals
        
    @classmethod
    def generate_secondary_skill(cls, rng, level):
        Player.check_level(level)
        decimals = rng.generate_uniform(0,1)
        skill = 3 + 1.5*level
        return skill + decimals
        
    @classmethod
    def generate_non_important_skill(cls, rng):
        return rng.generate_uniform(1,4)
        
    @classmethod
    def generate_stamina(cls, rng, age, level):
        if age < 18 or age > 33:
            return rng.generate_uniform(4,5 + 0.2*level)
        elif (age >= 18 and age < 20) or (age > 31 and age <= 33):
            return rng.generate_uniform(4,6 + 0.2*level)
        elif (age >= 20 and age < 22) or (age > 29 and age <= 31):
            return rng.generate_uniform(5,7 + 0.2*level)
        else:
            return rng.generate_uniform(5,8 + 0.2*level)
        
    @classmethod
    def generate_experience(cls, rng, age):
        return rng.generate_uniform(1 + 0.4*(age-17), 2 + 0.6*(age-17))
        
    @classmethod
    def generate_loyalty(cls, rng):
        return rng.generate_uniform(1, 20)
        
    @classmethod
    def generate_motherclub(cls, rng, loyalty):
        if loyalty < 20:
            return False
        else:
            return rng.generate_uniform(0,1) > 0.5
            
    @classmethod
    def generate_setpieces(cls, rng, age, level):
        if age < 19:
            max_v = 7 + 0.5*level
        elif age < 23:
            max_v = 7 + level
        else:
            max_v = 7 + 2*level
            
        return rng.generate_uniform(1, max_v)
        
    @classmethod
    def generate_form(cls, rng):
        return rng.generate_uniform(1, 8)
    
    
    @classmethod
    def generate_basics(cls, nationality, rng, level):
        name = Player.generate_name(nationality)
        pid = 0 # TODO, generate a unique id
        (age, days) = Player.generate_age(rng, level)
        loyalty = Player.generate_loyalty(rng)
        form = Player.generate_form(rng)
        
        return (pid, name, age, days, loyalty, form)
    
    # Generate with fixed values
    @classmethod
    def generate_keeper(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, Player.generate_main_skill(rng, level), Player.generate_secondary_skill(rng, level), 1, 1, 1, 1, Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_central_defender(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_main_skill(rng, level), Player.generate_secondary_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)  
        
    @classmethod
    def generate_wingback(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_main_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_non_important_skill(rng), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_central_midfielder(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_secondary_skill(rng, level), Player.generate_main_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_midfielder_tw(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_secondary_skill(rng, level), Player.generate_main_skill(rng, level), Player.generate_secondary_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_non_important_skill(rng), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_winger(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_main_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_central_forward(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_non_important_skill(rng), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_main_skill(rng, level), Player.generate_secondary_skill(rng, level), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)
        
    @classmethod
    def generate_defensive_forward(cls, rng, nationality, level):
        (pid, name, age, days, loyalty, form) = Player.generate_basics(nationality, rng, level)
        
        return Player(pid, name, age, days, nationality, 1, Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_non_important_skill(rng), Player.generate_secondary_skill(rng, level), Player.generate_main_skill(rng, level), Player.generate_setpieces(rng, age, level), Player.generate_stamina(rng, age, level), Player.generate_experience(rng, age), Player.generate_charisma(rng), loyalty, Player.generate_motherclub(rng, loyalty), Player.generate_character_and_moral(rng), Player.generate_character_and_moral(rng), form)        
        
# (self, id, name, age, days, nationality, keeper, defending, playmaking, winger, scoring, passing, setpieces, stamina, experience, charisma, loyalty, motherclub, character, moral):        
    
    # generate a starting team
    
    # generate specific team types (CA, LS, AOA, ....)
    
    # Read skills from json file
    

    

        
    


