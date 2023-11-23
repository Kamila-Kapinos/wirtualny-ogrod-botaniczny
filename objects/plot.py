from .plant import Plant


class Plot:
    def __init__(self):
        self.contained_plant = None

    def place_plant(self, plant: Plant):
        if self.contained_plant is not None:
            raise ValueError("Plot is already occupied")
        self.contained_plant = plant

    def remove_plant(self):
        self.contained_plant = None
