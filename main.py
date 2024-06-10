import random
import math
import logging
from typing import List, Type, Tuple, Dict
from tabulate import tabulate

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Animal classes and properties
class Animal:
    def __init__(self, x: int, y: int, gender: str):
        self.x = x
        self.y = y
        self.gender = gender

    def move(self, unit: int):
        dx, dy = random.randint(-unit, unit), random.randint(-unit, unit)
        self.x = max(0, min(500, self.x + dx))
        self.y = max(0, min(500, self.y + dy))

class Sheep(Animal):
    unit = 2

class Cow(Animal):
    unit = 2

class Chicken(Animal):
    unit = 1
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'female')

class Wolf(Animal):
    unit = 3

class Rooster(Animal):
    unit = 1
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'male')

class Lion(Animal):
    unit = 4

class Hunter(Animal):
    unit = 1

def random_position() -> Tuple[int, int]:
    return random.randint(0, 500), random.randint(0, 500)

def random_gender() -> str:
    return random.choice(['male', 'female'])

def create_animals() -> dict:
    animals = {
        'sheep': [Sheep(*random_position(), 'male' if i < 15 else 'female') for i in range(30)],
        'cow': [Cow(*random_position(), 'male' if i < 5 else 'female') for i in range(10)],
        'chicken': [Chicken(*random_position()) for _ in range(10)],
        'wolf': [Wolf(*random_position(), 'male' if i < 5 else 'female') for i in range(10)],
        'rooster': [Rooster(*random_position()) for _ in range(10)],
        'lion': [Lion(*random_position(), 'male' if i < 4 else 'female') for i in range(8)],
        'hunter': [Hunter(*random_position(), random_gender()) for _ in range(1)]
    }
    return animals
def distance(animal1: Animal, animal2: Animal) -> float:
    return math.sqrt((animal1.x - animal2.x) ** 2 + (animal1.y - animal2.y) ** 2)

def hunting(animals: dict, hunter_type: str, prey_types: List[str], distance_limit: int):
    prey = []
    for hunter in animals[hunter_type]:
        for prey_type in prey_types:
            for animal in animals[prey_type]:
                if distance(hunter, animal) <= distance_limit:
                    prey.append(animal)
                    logging.info(f"{hunter_type.capitalize()} ({hunter.gender}) hunted: {prey_type.capitalize()} ({animal.gender})")
    for animal in prey:
        for prey_type in prey_types:
            if animal in animals[prey_type]:
                animals[prey_type].remove(animal)

def reproduction(animals: dict, species: str, distance_limit: int):
    new_animals = []
    males = [a for a in animals[species] if a.gender == 'male']
    females = [a for a in animals[species] if a.gender == 'female']
    for male in males:
        for female in females:
            if distance(male, female) <= distance_limit:
                new_gender = random_gender()
                new_animal = type(male)(*random_position(), new_gender)
                new_animals.append(new_animal)
                logging.info(f"{species.capitalize()} mated - New {new_gender} born")
    animals[species].extend(new_animals)

def log_animal_status(animals):
    animal_table = []
    for species, species_animals in animals.items():
        if species in ['chicken', 'rooster', 'hunter']:
            animal_table.append([species.capitalize(), len(species_animals)])
        else:
            male_count = sum(1 for a in species_animals if a.gender == 'male')
            female_count = len(species_animals) - male_count
            animal_table.append([species.capitalize(), len(species_animals), male_count, female_count])
    headers = ['Species', 'Total'] if all(species in ['chicken', 'rooster', 'hunter'] for species in animals) else ['Species', 'Total', 'Male', 'Female']
    print(tabulate(animal_table, headers=headers, tablefmt='grid'))


# Running the simulation
def simulate(animals: dict, step_count: int = 1000):

    for step in range(step_count):
        for species, species_animals in animals.items():
            for animal in species_animals:
                animal.move(animal.unit)

        hunting(animals, 'wolf', ['sheep', 'chicken', 'rooster'], 4)
        hunting(animals, 'lion', ['cow', 'sheep'], 5)
        hunting(animals, 'hunter', ['sheep', 'cow', 'chicken', 'wolf', 'rooster', 'lion'], 8)

        reproduction(animals, 'sheep', 3)
        reproduction(animals, 'cow', 3)
        reproduction(animals, 'chicken', 3)
        reproduction(animals, 'wolf', 3)
        reproduction(animals, 'rooster', 3)
        reproduction(animals, 'lion', 3)

        if (step + 1) % 1000 == 0 or step == 0:   # We can increase the number of steps in this part
            logging.info(f"{step + 1} steps completed. Total number of animals: {sum(len(a) for a in animals.values())}")
            log_animal_status(animals)

    logging.info("Simulation Completed.")


if __name__ == "__main__":
    logging.info("Simulation Starting...")
    animals = create_animals()
    simulate(animals)