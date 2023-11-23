class Plant:
    def __init__(self, name: str, emoji: str = '🌱'):
        self.name = name
        self.emoji = emoji
        self.plant_level = 0
        self.care_requirements = {
            "water_frequency": 0,
            "sunlight_requirements": 0,
        }
        self.is_watered = False
        self.is_in_sunlight = False

        def grow(self):
            if list(self.care_requirements.values()) == [1, 1]:
                self.plant_level += 1

        def wither(self):
            if list(self.care_requirements.values()) == [-1, 1]:
                pass  # remove plant form plot

        def day_summary(self):
            # TODO - add a day summary to the garden class
            if self.is_watered == True:
                self.care_requirements["water_frequency"] += 1
            else:
                pass
            if self.is_in_sunlight == True:
                self.care_requirements["sunlight_requirements"] += 1
            else:
                pass

        def reproduction(self):
            # at this level plant is able to create new plants in adjacent plots
            if self.plant_level == 5:
                pass

        def sunlight(self):
            self.is_in_sunlight = True

        def water(self):
            self.is_watered = True

        def status(self):
            return f"{self.name} is a {self.__class__.__name__} at level {self.plant_level}."
