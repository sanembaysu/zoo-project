## **Zoo Project**

**Overview**

This code simulates a zoo containing different animals (sheep, cow, chicken, rooster, wolf, lion) and a hunter. Each animal and hunter can move within the area at a determined unit level. Each animal can hunt and hunt within a certain unit proximity. The simulation uses a grid with coordinates ranging from 0 to 500 on both axes.

**Key Components of the Simulation**
1. Animal Movement: Each animal species has a defined movement ability, expressed as a number of units it can move in any direction.
2. Reproduction: Animals can reproduce if a male and female of the same species are within a certain distance.
3. Hunting: Predators can hunt prey species if they come within a certain distance.

**Classes and Important Functions**
- `Animal`: Base class with attributes for position, gender, and movement functionality.
- `Sheep`, `Cow`, `Chicken`, `Wolf`, `Rooster`, `Lion`, `Hunter`: Subclasses for each animal type, each with specific movement units. Chickens, Roosters and Hunter have fixed genders.
- `random_position()`: Generates random coordinates within the grid.
- `random_gender()`: Randomly assigns a gender to newly created animals.
- `create_animals()`: Initializes the animal populations with random positions and genders.
- `distance()`: Calculates the Euclidean distance between two animals.
- `hunting()`: Manages the hunting interactions between predators and their prey.
- `reproduction()`: Manages the reproduction process based on proximity and gender of animals.
- `log_animal_status()`: Prints the status of each species in a tabulated format.

**Simulation Process**
1. Initialization: Setting up initial animal populations with random positions and genders.
2. Movement: Animals move based on their defined movement abilities.
3. Interaction Phases: Involves hunting interactions between predators and prey, followed by reproduction processes.
4. Logging: Reports the ecosystem status periodically, including animal populations and specific events like hunting and births.

**Outputs**
The simulation generates outputs through logging and tabulated printing, including:
- Initial and periodic summaries of animal populations.
- Events such as hunting interactions and births within the zoo.
