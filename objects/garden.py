from .plant import Plant
from .plot import Plot


class Garden:
    def __init__(self, n: int, m: int):
        self.plots = [[Plot() for _ in range(n)] for _ in range(m)]

    def add_plant(self, plant: Plant, x: int = 0, y: int = 0):
        self.plots[x][y].place_plant(plant)
    def remove_plant(self, x: int = 0, y: int = 0):
        self.plots[x][y].remove_plant()

    def about(self):
        # loop over plots and if value is not 0 print the plot with its position and plant.
        pass
