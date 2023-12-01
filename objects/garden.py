from .plant import Plant
from .plot import Plot
from random import choice, randint
import sys


class Garden:
    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.plots = [[Plot() for _ in range(n)] for _ in range(m)]
        self.sunny = False
        self.raining = False
        self.day_counter = 0

    def reproduce(self, x: int, y: int):
        if not self.plots[x][y].contained_plant or not self.plots[x][y].contained_plant.ready_to_reproduce:
            return  # No plant to reproduce or not ready

        # Directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        available_plots = []

        # Check available adjacent plots
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if new_x and new_y are within the garden boundaries
            if 0 <= new_x < self.m and 0 <= new_y < self.n:
                if not self.plots[new_x][new_y].contained_plant:
                    available_plots.append((new_x, new_y))

        if not available_plots:
            return  # No available plots for reproduction

        # Randomly select an available plot
        selected_plot_x, selected_plot_y = choice(available_plots)
        self.plots[selected_plot_x][selected_plot_y].place_plant(
            self.plots[x][y].contained_plant.get_offspring()
        )

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
            self.plots[y][x].water()

    def harvest(self, x: int = None, y: int = None):
        # harvest all plots by default or harvest a specific plot given x,y coordinates
        if y is None or x is None:
            for row in self.plots:
                for plot in row:
                    plot.harvest()
        else:
            self.plots[y][x].harvest()

    def end_day(self):
        # Iterate over all plots in the garden
        for y, row in enumerate(self.plots):
            for x, plot in enumerate(row):
                if plot.contained_plant:
                    # Update each plant
                    plot.contained_plant.update(self.sunny, self.raining)
                    self.harvest(x, y)
                    self.reproduce(x, y)
        # END OF ITERATION

        # ends day calculations for the next day
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

    def __repr__(self):
        return f"Garden(Day:{self.day_counter} {self.n}, {self.m})"
