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

    #Creating the animals
    leo = Animal("Leo", "Lion", 5, "Carnivore", "Savannah", "mammal")
    shelly = Animal("Shelly", "Turtle", 40, "Herbivore", "Aquatic", "reptile")
    piper = Animal("Piper", "Parrot", 2, "Seeds", "Aviary", "bird")
    rocky = Animal("Rocky", "Crocodile", 25, "Carnivore", "Aquatic", "reptile")

    #Creating the enclosures
    lion_enclosure = Enclosure("Lion Den", "savannah", 2)
    turtle_enclosure = Enclosure("Turtle Pool", "aquatic", 3)
    aviary_enclosure = Enclosure("Bird Aviary", "aviary", 5)

    #Creating the staff
    zoe = Staff("Zoe", "zookeeper")
    victor = Staff("Victor", "veterinarian")

    #Assigning the animals to enclosures
    lion_enclosure.add_animal(leo)
    turtle_enclosure.add_animal(shelly)
    aviary_enclosure.add_animal(piper)
    turtle_enclosure.add_animal(rocky)

    #To display enclosure information
    print(lion_enclosure.get_status())
    print(turtle_enclosure.get_status())
    print(aviary_enclosure.get_status())

    print(lion_enclosure.get_status())
    print(turtle_enclosure.get_status())
    print(aviary_enclosure.get_status())

    #Zookeeper feeding the animals
    print("\n--- Feeding Animals ---")
    for animal in [leo, shelly, piper, rocky]:
        zoe.feed_animal(animal)

    #Zookeeper cleaning the enclosures
    print("\n--- Cleaning Enclosures ---")
    turtle_enclosure.soil(30)
    print(turtle_enclosure.get_status())
    zoe.clean_enclosure(turtle_enclosure)
    print(turtle_enclosure.get_status())

    #Veterinarian performs health check
    print("\n--- Health Check ---")
    victor.health_check(leo, "Minor leg scratch", "low")
    victor.health_check(piper, "Broken wing", "high")

    #To check treatment status
    print("\n--- Treatment Status ---")
    print(f"{leo.name} under treatment:", leo.is_under_treatment())
    leo.mark_recovered()
    print(f"{leo.name} under treatment:", leo.is_under_treatment())

    #To demonstrate animal sounds
    print("\n--- Animal Sounds ---")
    print(leo.make_sound())
    print(shelly.make_sound())
    print(piper.make_sound())
    print(rocky.make_sound())

    # Summary output
    print("\n--- Zoo Summary ---")
    print(lion_enclosure)
    print(turtle_enclosure)
    print(aviary_enclosure)

    print("\nSystem demonstration complete.")

if __name__ == "__main__":
    main()