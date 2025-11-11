'''
File: animal.py
Description: Defines the aminal hierarchy and basic health tracking for the zoo management system.
Author: Ellie Debian
ID: 110444485
Username: debey003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from datetime import date

"""Base class for all animals in the zoo"""
class Animal:
    def __init__(self, name: str, species: str, age: int, diet: str, environment_type: str) -> None:
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__environment_type = environment_type
        self.__health_records = []

        self.set_name(name)
        self.set_species(species)
        self.set_age(age)
        self.set_diet(diet)
        self.set_environment_type(environment_type)