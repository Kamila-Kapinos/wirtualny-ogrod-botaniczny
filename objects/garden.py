from .plant import Plant
from .plot import Plot
from random import choice, randint
import sys


class Garden:
    def __init__(self, n: int, m: int):
        self._n, self._m = n, m
        self._plots = [[Plot() for _ in range(n)] for _ in range(m)]
        self._sunny = False
        self._raining = False
        self._day_counter = 0

    def _reproduce(self, x: int, y: int):
        if not self._plots[x][y].has_plant() or not self._plots[x][y].is_ready_to_reproduce():
            return  # No plant to reproduce or not ready

        # Directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        available_plots = []

        # Check available adjacent plots
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if new_x and new_y are within the garden boundaries
            if 0 <= new_x < self._m and 0 <= new_y < self._n:
                if not self._plots[new_x][new_y].has_plant():
                    available_plots.append((new_x, new_y))

        if not available_plots:
            # maybe set this plot to not reproduce for a few days
            return  # No available plots for reproduction

        # Randomly select an available plot
        selected_plot_x, selected_plot_y = choice(available_plots)
        self._plots[selected_plot_x][selected_plot_y].place_plant(
            self._plots[x][y].get_plant_offspring()
        )

    def add_plant(self, plant: Plant, x: int = 0, y: int = 0):
        self._plots[x][y].place_plant(plant)

    def remove_plant(self, x: int = 0, y: int = 0):
        self._plots[x][y].remove_plant()
        # maybe add a warning if user wants to remove a plant, so he doesn't do it by mistake

    def water_plant(self, x: int = None, y: int = None):
        # water all plots by default or water a specific plot given x,y coordinates
        if x or y is None:
            for row in self._plots:
                for plot in row:
                    plot.water_plant()
        else:
            self._plots[y][x].water_plant()

    def harvest_plant(self, x: int = None, y: int = None) -> list:
        # harvest all plots by default or harvest a specific plot given x,y coordinates
        
        harvested = []
        if y is None or x is None:
            for row in self._plots:
                for plot in row:
                    harvest = plot.harvest_plant()
                    if harvest:
                        for fruit in harvest:
                            harvested.append(fruit)
        else:
            self._plots[y][x].harvest_plant()
        return harvested

    def end_day(self):
        # Iterate over all plots in the garden
        for y, row in enumerate(self._plots):
            for x, plot in enumerate(row):
                if plot.has_plant():
                    # Update each plant
                    plot.update(self._sunny, self._raining)
                    # self.harvest_plant(x, y)
                    self._reproduce(x, y)
                    # Check if plant is dead if so remove it
                    print(plot.is_dead())
                    if plot.is_dead(): 
                        print(f"Plant at ({y},{x}) has died")
                        self.remove_plant(y,x)
        # END OF ITERATION

        # Calculations for the next day
        self._sunny_day()
        self._rainy_day()
        self._day_counter += 1

    def _sunny_day(self):
        # randomly choose if a day is sunny or not
        if randint(0, 7) >= 3:
            self._sunny = True
        else:
            self._sunny = False

    def _rainy_day(self):
        if randint(0, 7) >= 5:
            self._raining = True
        else:
            self._raining = False

    def show(self):
        # TODO: add weather status
        
        weather_status = "Weather: "
        if self._sunny and self._raining:
            weather_status += "🌦️"  # Sun shower
        elif self._sunny:
            weather_status += "☀️"   # Sunny
        elif self._raining:
            weather_status += "🌧️"   # Raining
        else:
            weather_status += "☁️"   # Neutral weather

        sys.stdout.write(weather_status + '\n')
        n = len(self._plots[0])  # Assuming all rows have equal number of plots
        horizontal_separator = '+' + ('----+' * n)
        sys.stdout.write(horizontal_separator + '\n')
        for row in self._plots:
            sys.stdout.write('|')  # Start of row
            for plot in row:
                if plot.has_plant():
                    sys.stdout.write(f" {plot} |")  # Plot with plant
                else:
                    sys.stdout.write(" 🟫 |")  # Empty plot
            sys.stdout.write('\n')
            sys.stdout.write(horizontal_separator + '\n')
        sys.stdout.flush()

    def status(self) -> list:
        status = []
        for x, row in enumerate(self._plots):
            for y, plot in enumerate(row):
                if plot.has_plant():
                    plot_status = plot.get_plant_status()
                    plot_status['coordinates'] = (x, y)
                    status.append(plot_status)
        return status

    def __repr__(self):
        return f"Garden(Day:{self._day_counter} {self._n}, {self._m})"
