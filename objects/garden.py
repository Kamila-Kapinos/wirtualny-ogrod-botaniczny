from .plant import Plant
from .plot import Plot
from random import randint
import sys


class Garden:
    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.plots = [[Plot() for _ in range(n)] for _ in range(m)]
        self.sunny = False
        self.raining = False
        self.day_counter = 0

    def reproduce(self, x: int, y: int):
        if self.plots[x][y].check_reproduce_plant():  # roślina jest gotowa do reprodukcji
            available_plots = []
            # FUdaj dodaać funkcję która sprawdza czy są wolne miejsca obok
            if not self.plots[x + 1][y].contained_plant:
                available_plots.append((x + 1, y))
            pass
            # GET RANGE OF AVALIBLE PLOTS and get one random plot
            x, y = available_plots[randint(0, len(available_plots) - 1)]
            self.plots[x][y] = self.plots[x][y].add_plant(self.plots[x][y].contained_plant.get_dna())
        else:
            pass

    def add_plant(self, plant: Plant, x: int = 0, y: int = 0):
        self.plots[x][y].place_plant(plant)

    def remove_plant(self, x: int = 0, y: int = 0):
        self.plots[x][y].remove_plant()
        # maybe add a warning if user wants to remove a plant, so he doesn't do it by mistake

    def water(self, x: int = None, y: int = None):
        # water all plots by default or water a specific plot given x,y coordinates
        if x or y is None:
            for row in self.plots:
                for plot in row:
                    plot.water()
        else:
            self.plots[x][y].water()

    def harvest(self, x: int = None, y: int = None):
        # harvest all plots by default or harvest a specific plot given x,y coordinates
        if x or y is None:
            for row in self.plots:
                for plot in row:
                    plot.harvest()
        else:
            self.plots[x][y].harvest()

    def end_day(self):
        # Iterate over all plots in the garden
        for row in self.plots:
            for plot in row:
                if plot.contained_plant:
                    # Update each plant
                    plot.contained_plant.update(self.sunny, self.raining)
        # END OF ITERATION

        # ends day and calculates plant growth
        self._sunny_day()
        self._rainy_day()
        self.day_counter += 1

    def _sunny_day(self):
        # randomly choose if a day is sunny or not
        if randint(0, 7) >= 3:
            self.sunny = True
        else:
            self.sunny = False

    def _rainy_day(self):
        if randint(0, 7) >= 5:
            self.raining = True
        else:
            self.raining = False

    def show(self):
        n = len(self.plots[0])  # Assuming all rows have equal number of plots
        horizontal_separator = '+' + ('---+' * n)
        sys.stdout.write(horizontal_separator + '\n')
        for row in self.plots:
            sys.stdout.write('|')  # Start of row
            for plot in row:
                if plot.contained_plant:
                    sys.stdout.write(f" {plot.contained_plant.emoji} |")  # Plot with plant
                else:
                    sys.stdout.write(" 🟤 |")  # Empty plot
            sys.stdout.write('\n')
            sys.stdout.write(horizontal_separator + '\n')
        sys.stdout.flush()
