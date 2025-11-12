'''
File: staff.py
Description: A brief description of this Python module.
Author: Ellie Debian
ID: 110444485
Username: debey003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure

"""Represents a staff member working in the zoo"""
class Staff:
    def __init__(self, name: str, role: str) -> None:
        self.__name = name
        self.__role = role

        self.set_name(name)
        self.set_role(role)

    """Getters, setters, and properties"""
    def get_name(self) -> str:
        return self.__name

    def set_name(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__name = value
        else:
            self.__name = "Unknown"

    name = property(get_name, set_name)

    def get_role(self) -> str:
        return self.__role

    def set_role(self, value: str) -> None:
        valid_role = ("zookeeper", "veterinarian")
        if isinstance(value, str) and value.lower() in valid_roles:
            self.__role = value.lower()
        else:
            self.__role = "zookeeper"

    role = property(get_role, set_role)

    """Behaviours"""
    def feed_animal(self, animal: Animal) -> None:
        """Feed an animal if the staff member is a zookeeper"""
        if self.__role == "zookeeper":
            print(f"{self.__name} feeds {animal.name}. {animal.eat()}")
        else:
            print(f"{self.__name} is not assigned to feed animals.")

    def clean_enclosure(self, enclosure: Enclosure) -> None:
        """Clean an enclosure if the staff member is a zookeeper"""
        if self.__role == "zookeeper":
            enclosure.clean()
            print(f"{self.__name} cleaned {enclosure.name}.")
        else:
            print(f"{self.__name} is not assigned to clean enclosures.")


