from .plant import Plant
from .plot import Plot


class Garden:
    def __init__(self, n: int, m: int):
        self.plots = [[Plot() for _ in range(n)] for _ in range(m)]
        self.sunny = False
        self.raining = False

    def add_plant(self, plant: Plant, x: int = 0, y: int = 0):
        self.plots[x][y].place_plant(plant)

    def remove_plant(self, x: int = 0, y: int = 0):
        self.plots[x][y].remove_plant()
        # maybe add a warning if user wants to remove a plant, so he doesn't do it by mistake

    def about(self):
        # loop over plots and if value is not 0 print the plot with its position and plant.
        pass

    def water(self, x: int, y: int):
        # water all plots by default or water a specific plot given x,y coordinates
        pass

    def harvest(self, x: int, y: int):
        # harvest all plots by default or harvest a specific plot given x,y coordinates
        pass

    def end_day(self):
        # ends day and calculates plant growth

        self._sunny_day()
        self._rainy_day()
        pass

    def _sunny_day(self):
        # randomly choose if a day is sunny or not
        pass

    def _rainy_day(self):
        # randomly choose if a day is rainy or not
        pass
