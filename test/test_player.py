import unittest
from resources.player import *
from resources.random_generator import *

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.rand_iterations = 10000
        self.rng = RandomGenerator() 
    
    def test_generate_age(self):
        for i in range(0, self.rand_iterations):
            level = self.rng.generate_int(0,5)
            (age, days) = Player.generate_age(self.rng, level)
            self.assertGreaterEqual(age, 17)
            self.assertLessEqual(age, 34)
            self.assertGreaterEqual(days, 0)
            self.assertLessEqual(days, 111)
            
    def test_generate_charisma(self):
        for i in range(0, self.rand_iterations):
            charisma = Player.generate_charisma(self.rng)
            self.assertLessEqual(charisma, 7)
            self.assertGreaterEqual(charisma, 1)
            
    def test_generate_main_skill(self):
        for i in range(0, self.rand_iterations):
            level = self.rng.generate_int(0,5)
            skill = Player.generate_main_skill(self.rng, level)
            self.assertLessEqual(skill, 15)
            self.assertGreaterEqual(skill, 3)
            
    def test_generate_secondary_skill(self):
        for i in range(0, self.rand_iterations):
            level = self.rng.generate_int(0,5)
            skill = Player.generate_secondary_skill(self.rng, level)
            self.assertLess(skill, 11.5)
            self.assertGreaterEqual(skill, 3)
            
    def test_generate_non_important_skill(self):
        for i in range(0, self.rand_iterations):
            skill = Player.generate_non_important_skill(self.rng)
            self.assertLessEqual(skill, 4)
            self.assertGreaterEqual(skill, 1)
        
    def test_generate_stamina(self):
        for i in range(0, self.rand_iterations):
            level = self.rng.generate_int(0,5)
            age = self.rng.generate_int(17, 34)
            skill = Player.generate_stamina(self.rng, age, level)
            if age < 18 or age > 33:
                self.assertLessEqual(skill, 6)
                self.assertGreaterEqual(skill, 4)
            elif (age >= 18 and age < 20) or (age > 31 and age <= 33):
                self.assertLessEqual(skill, 7)
                self.assertGreaterEqual(skill, 4)
            elif (age >= 20 and age < 22) or (age > 29 and age <= 31):
                self.assertLessEqual(skill, 8)
                self.assertGreaterEqual(skill, 5)
            else:
                self.assertLessEqual(skill, 9)
                self.assertGreaterEqual(skill, 5)
        
    def test_generate_experience(self):
        for i in range(0, self.rand_iterations):
            age = self.rng.generate_int(17,34)
            skill = Player.generate_experience(self.rng, age)
            self.assertLessEqual(skill, 12.2)
            self.assertGreaterEqual(skill, 1)
            
    def test_generate_loyalty(self):
        for i in range(0, self.rand_iterations):
            skill = Player.generate_non_important_skill(self.rng)
            self.assertLessEqual(skill, 20)
            self.assertGreaterEqual(skill, 1)
            
    def test_generate_motherclub(self):
        generatedFalse = False
        generatedTrue = False
        for i in range(0, self.rand_iterations):
            loyalty = self.rng.generate_int(1,20)
            skill = Player.generate_motherclub(self.rng, loyalty)
            if skill == False:
                generatedFalse = True
            if skill == True:
                generatedTrue = True
                
        self.assertTrue(generatedTrue)
        self.assertTrue(generatedFalse)
        
    def test_generate_setpieces(self):
        for i in range(0, self.rand_iterations):
            level = self.rng.generate_int(0,5)
            age = self.rng.generate_int(17,34)
            skill = Player.generate_setpieces(self.rng, age, level)
            if age < 19:
                self.assertLessEqual(skill, 10.5)
                self.assertGreaterEqual(skill, 1)
            elif age < 23:
                self.assertLessEqual(skill, 12)
                self.assertGreaterEqual(skill, 1)
            else:
                self.assertLess(skill, 17)
                self.assertGreaterEqual(skill, 1)
            
            
            
            
            
            
            
