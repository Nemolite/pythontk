# from window import *
# from db import *
#
# DB().create('people')
# Window().show()
import random
class Human:
    def __init__(self,name,health):
        self._name = name
        self._health = health

    def attack(self,enemy):
        self.damage = random.randint(1,10)
        print(f"{self._name} наносит персонажу {enemy} {self.damage} урона!")

    def get_damage(self,damage):
        self._health = self._health - damage
        print(f"{self._name} получает {damage} урона! Текущее здоровье — {self._health}.")

    def healing(self):
        health = random.randint(5,15)
        self._health = self._health + health
        print(f"{self._name} восстанавливает {health} здоровья. Текущее здоровье — {self._health}.")

class Warrior(Human):
    def __init__(self, name,health,defense):
        super().__init__(name,health)
        self._defense = defense

    def attack(self, enemy):
        self.damage = random.randint(10, 20)
        print(f"{self._name} наносит персонажу {enemy} {self.damage} урона!")

    def get_damage(self,damage):
        self._health = self._health - (damage - self._defense)
        if self._health<0:
            self._health=0
        print(f"{self._name} получает {damage} урона! Текущее здоровье — {self._health}.")

class Archer(Human):
    def __init__(self, name,health,accuracy,agility):
        super().__init__(name,health)
        self._accuracy = accuracy
        self._agility = agility

    def attack(self,enemy):
        self.damage = random.randint(15,25)
        print(f"{self._name} наносит персонажу {enemy} {self.damage} урона!")

    def get_damage(self,damage):
        if self._agility>=damage:
            print(f"{self._name} увернулся от удара!")

