import copy


class Plant:
    def __init__(self, name: str, emoji: str = '🌱',
                 water_frequency: int = 3, sunlight_exposure: int = 5):
        self.ready_to_reproduce = False
        self.name = name
        self.emoji = str(emoji)  # in case emoji is not passed as a string
        self.plant_level = 1
        self.is_dead = False
        self.reproduce_cooldown = 5
        self.care_requirements = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }
        self.care_record = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }

    def requirements_checker(self):
        for key, value in self.care_requirements.items():
            survive = range(- self.plant_level - 1, self.plant_level)  # if in this range don't grow but don't die
            if self.care_record[key] - self.care_requirements[key] in (-1, 0, 1):
                pass
            elif self.care_record[key] - self.care_requirements[key] in survive:
                print("Warning! Take care of your plant")
                return 0
            else:
                return -1
        return 1

    def grow(self):
        if self.requirements_checker():
            self.plant_level += 1
        else:
            self.plant_level -= 1

    def wither(self):
        if self.plant_level < 0:
            self.is_dead = True

    def reproduction(self):
        # at this level plant is able to create new plants in adjacent plots
        if self.plant_level == 5:
            self.ready_to_reproduce = True
        else:
            self.ready_to_reproduce = False

    def reproduce(self):
        self.reproduce_cooldown = 5

    def update(self, is_in_sunlight: bool, is_raining: bool):
        self.care_record["sunlight_exposure"] += is_in_sunlight
        self.care_record["water_frequency"] += is_raining

        # Day decay
        self.care_record = {key: value - 1 for key, value in self.care_record.items()}

        self.grow()
        self.reproduction()

    def water(self):
        self.care_record["water_frequency"] += 1

    def status(self):
        return f"{self.name} is a {self.__class__.__name__} at level {self.plant_level}."

    def harvest(self):
        # You cant harvest a plant, but this methods will be used in Tree and Bush.
        pass

    def get_offspring(self):
        offspring = copy.deepcopy(self)
        # reset attr
        offspring.plant_level = 1
        offspring.ready_to_reproduce = False
        offspring.reproduce_cooldown = 5
        offspring.care_record = self.care_requirements

        # Optionally, introduce variations
        # For example, slight changes in water_frequency or sunlight_exposure
        # offspring.care_requirements['water_frequency'] += variation

        return offspring

    def __repr__(self):
        return (f"{self.emoji} {self.name}, l: {self.plant_level} w : {self.care_record['water_frequency']},"
                f" s : {self.care_record['sunlight_exposure']}")
