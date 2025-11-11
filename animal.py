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
    def __init__(self, name: str, species: str, age: int, diet: str, environment_type: str, category: str) -> None:
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__environment_type = environment_type
        self.__category = category
        self.__health_records = []

        self.set_name(name)
        self.set_species(species)
        self.set_age(age)
        self.set_diet(diet)
        self.set_environment_type(environment_type)

"""Getters, setters, and properties"""
    def get_name(self) -> str:
        return self.__name

    def set_name(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__name = value
        else:
            self.__name = "Unknown"

    name = property(get_name, set_name)

    def get_species(self) -> str:
        return self.__species

    def set_species(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__species = value
        else:
            self.__species = "Unknown"

    species = property(get_species, set_species)

    def get_age(self) -> int:
        return self.__age

    def set_age(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            self.__age = 0

    age = property(get_age, set_age)

    def get_diet(self) -> str:
        return self.__diet

    def set_diet(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__diet = value
        else:
            self.__diet = "Unknown"

    diet = property(get_diet, set_diet)

    def get_environment_type(self) -> str:
        return self.__environment_type

    def set_environment_type(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__environment_type = value.lower()
        else:
            self.__environment_type = "Unknown"

    environment_type = property(get_environment_type, set_environment_type)

    def get_category(self) -> str:
        return self.__category

    def set_category(self, value: str) -> None:
        valid_categories = ("mammal", "reptile", "bird", "other" )
        if isinstance(value, str) and value.lower() in valid_categories:
            self.__category = value.lower()
        else:
            self.__category = ("other")

    category = property(get_category, set_category)

