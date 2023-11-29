from .plant import Plant


class Plot:
    def __init__(self):
        self.contained_plant = None

    def place_plant(self, plant: Plant):
        if self.contained_plant is not None:
            raise ValueError("Plot is already occupied")
        self.contained_plant = plant

    def remove_plant(self):
        if self.contained_plant is None:
            raise ValueError("Plot is empty")
        
        # method could return some information about the plant that was removed
        self.contained_plant = None

    def water(self):
        if self.contained_plant is None:
            raise ValueError("Plot is empty")
        self.contained_plant.water()

    def harvest(self):
        if self.contained_plant is None:
            raise ValueError("Plot is empty")
        self.contained_plant.harvest()