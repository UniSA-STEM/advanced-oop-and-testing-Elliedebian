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

    """Getters, setters, and properties"""
    def get_name(self) -> str:
        return self.__name

    def set_name(self, value:str) -> None:
        if isinstance(value, str) and value:
            self.__name = value
        else:
            self.__name = "Unknown"

    name = property(get_name, set_name)

    def get_environment(self) -> str:
        return self.__environment_type

    def set_environment(self, value:str) -> None:
        if isinstance(value, str) and value:
            self.__environment_type = value.lower()
        else:
            self.__environment_type = "Unknown"

    environment = property(get_environment, set_environment)

    def get_size(self) -> int:
        return self.__size

    def set_size(self, value:int) -> None:
        if isinstance(value, int) and value > 0:
            self.__size = value
        else:
            self.__size = 1

    size = property(get_size, set_size)

    def get_cleanness(self) -> int:
        return self.__cleanliness

    cleanness = property(get_cleanness)

    def get_animals(self) -> list:
        return self.__animals

    animals = property(get_animals)

    """Behaviours"""
    def add_animal(self, animal:Animal) -> None:
        """Add an animal to the enclosure if compatible"""
        if not isinstance(animal, Animal):
            return
        if len(self.__animals) >= self.__size:
            return
        if animal.environment_type != self.__environment_type:
            return
        self.__animals.append(animal)

    def remove_animal(self, animal:Animal) -> None:
        """Remove an animal from the enclosure"""
        if animal in self.__animals:
            self.__animals.remove(animal)

    def clean(self) -> None:
        """Restore the cleanliness to 100"""
        self.__cleanliness = 100

    def soil(self, amount:int) -> None:
        """Reduce cleanliness by a given amount"""
        if isinstance(amount, int) and amount > 0:
            self.__cleanliness -= amount
        else:
            self.__cleanliness -= 10
        if self.__cleanliness < 0:
            self.__cleanliness = 0

    def get_status(self) -> str:
        """Get a simple status summary of the enclosure"""
        return (
            f"Enclosure '{self.__name}' "
            f" [{self.__environment_type}] - Cleanliness: {self.__cleanliness}%,"
            f" Animals: {len(self.__animals)}"
        )

    def list_animals(self) -> str:
        """Return a list of animals currently in the enclosure"""
        if not self.__animals:
            return "No animals in this enclosure"
        animal_names = ", ".join(animal.name for animal in self.__animals)
        return f"Animals: {animal_names}"

    def __str__(self) -> str:
        """Return a string representation of the enclosure"""
        return self.get_status()

