import copy


class Plant:
    def __init__(self, name: str, emoji: str = '🌱',
                 water_frequency: int = 3, sunlight_exposure: int = 5,
                 reproduce_level: int = 5):
        self.ready_to_reproduce = False
        self._name = name
        self.emoji = str(emoji)  # in case emoji is not passed as a string
        self._plant_level = 1
        self.is_dead = False
        self._reproduce_level = reproduce_level
        self._reproduce_cooldown = 5
        self._care_requirements = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }
        self._care_record = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }

    def _requirements_checker(self):
        for key, value in self._care_requirements.items():
            survive = range(- (self._plant_level - 1), self._plant_level)  # if in this range don't grow but don't die
            if self._care_record[key] - self._care_requirements[key] in (-1, 0, 1):
                pass
            elif self._care_record[key] - self._care_requirements[key] in survive:
                print("Warning! Take care of your plant")
                return 0
            else:
                return -1
        return 1

    def _grow(self):
        self._plant_level += self._requirements_checker()

    def _wither(self):
        if self._plant_level < 0:
            self.is_dead = True

    # TODO: maybe rename this method and use it plot.py
    def reproduction(self) -> bool:
        # at this level plant is able to create new plants in adjacent plots
        self.ready_to_reproduce = self._plant_level >= self._reproduce_level
        return self.ready_to_reproduce

    def update(self, is_in_sunlight: bool, is_raining: bool):
        self._care_record["sunlight_exposure"] += is_in_sunlight 
        self._care_record["water_frequency"] += is_raining

        # Day decay
        self._care_record = {key: value - 1 for key, value in self._care_record.items()}

        self._grow()
        self.reproduction()
        self._wither()

    def water(self):
        self._care_record["water_frequency"] += 1

    def sunlight(self):
        self._care_record["sunlight_exposure"] += 1

    def harvest(self):
        # You cant harvest a plant, but this methods will be used in Tree and Bush.
        pass

    def get_offspring(self):
        self._reproduce_cooldown = 5

        # cooping the plant
        offspring = copy.deepcopy(self)
        # reset attr
        offspring._plant_level = 1
        offspring.ready_to_reproduce = False
        offspring._reproduce_cooldown = 5
        offspring._care_record = self._care_requirements

        # Optionally, introduce variations
        # For example, slight changes in water_frequency or sunlight_exposure
        # offspring.care_requirements['water_frequency'] += variation

        return offspring

    def get_status(self) -> dict:
        return {
            "name": self._name,
            "emoji": self.emoji,
            "level": self._plant_level,
            "requirements": self._care_requirements,
            "care_record": self._care_record,
        }
        # return f"{self._name} is a {self.__class__.__name__} at level {self._plant_level}."

    def __repr__(self):
        return (f"{self.emoji} {self._name}, l: {self._plant_level} w : {self._care_record['water_frequency']},"
                f" s : {self._care_record['sunlight_exposure']}")
