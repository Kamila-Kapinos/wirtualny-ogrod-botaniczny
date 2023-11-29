class Plant:
    def __init__(self, name: str, emoji: str = '🌱',
                 water_frequency: int = 3, sunlight_exposure: int = 5):
        self.ready_to_reproduce = False
        self.name = name
        self.emoji = emoji
        self.plant_level = 0
        self.care_requirements = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }
        self.care_record = {
            "water_frequency": water_frequency,
            "sunlight_exposure": sunlight_exposure,
        }
        self.is_watered = False
        self.is_in_sunlight = False
        self.reproduce_cooldown = 5

    def requirements_checker(self):
        flag = True
        for key, value in self.care_requirements.items():
            if self.care_record[key] - self.care_requirements[key] in (-1, 0, 1):
                pass
            else:
                print("Warning! Take care of your plant")
                flag = False
                break
        return flag

    def grow(self):
        if self.requirements_checker():  # jesli wymagania spełnione albo nie.
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

    def update(self, is_in_sunlight: bool, is_watered: bool):
        self.is_in_sunlight = is_in_sunlight
        self.is_watered = is_watered

        self.grow()
        self.reproduction()

    def status(self):
        return f"{self.name} is a {self.__class__.__name__} at level {self.plant_level}."
