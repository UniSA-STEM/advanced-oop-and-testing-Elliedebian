'''
File: main.py
Description: Demonstrates the zoo management system using the Animal, Enclosure, and Staff classes.
Author: Ellie Debian
ID: 110444485
Username: debey003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from staff import Staff

def main() -> None:
    """Build and demonstrate the zoo system"""

    leo = Animal("Leo", "Lion", 5, "Carnivore", "Savannah", "mammal")
    shelly = Animal("Shelly", "Turtle", 40, "Herbivore", "Aquatic", "reptile")
    piper = Animal("Piper", "Parrot", 2, "Seeds", "Aviary", "bird")
    rocky = Animal("Rocky", "Crocodile", 25, "Carnivore", "Aquatic", "reptile")

