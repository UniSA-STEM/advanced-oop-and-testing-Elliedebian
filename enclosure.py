'''
File: enclosure.py
Description: Defines the Enclosure class for housing compatible animals within the zoo management system.
Author: ELlie Debian
ID: 110444485
Username: debey003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

"""Represents a single animal enclosure in the zoo"""
class Enclosure:
    def __init__(self, name:str, environment_type: str, size: int) -> None:
        self.__name = name
        self.__environment_type = environment_type
        self.__size = size
        self.__cleanliness = 100
        self.__animals = []

        self.set_name(name)
        self.set_environment(environment_type)
        self.set_size(size)

