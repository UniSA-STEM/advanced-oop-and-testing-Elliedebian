[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_geRERRo)

This program models a simple zoo management system using object-oriented programming principles.
It allows staff members to manage animals, enclosures, and health records within the zoo.
The system demonstrates:
- animal.py
- enclosure.py
- staff.py
- main.py

The animal.py file defines the Animal class.
Each animal has a name, species, age, diet, environment, and category.
The key features include:
- Private attributes for all animal data.
- Property methods for controlled access.
- Health record tracking.
- Category-based behaviour.

The enclosure.py files defines the Enclosure class which is used to group compatible animals.
the key features include:
- Private attributes for name, environment type, size, cleanliness, and animals.
- Data validation for environment and capacity.
- Methods to add and remove animals safely.
- Cleaning and soiling functions to manage enclosure hygiene.

The staff.py file defines the Staff class representing zookepers and veterinarians.
The key features include:
- Private attributes for name and role.
- Data validation for accepted roles.
- Zookeepers can feed animals and clean enclosures.
- Veterinarians can perform health checks and record treatments.

The main.py file acts as starting point of the program.
It is in charge of creating animals, enclosures, and staff. 
It demonstrates the interactions between the three.
The key actions are:
- Assigning animals to enclosures.
- Feeding animals and cleaning enclosures.
- Performing health checks and making recoveries.
- Printing status summaries and animal sounds.
