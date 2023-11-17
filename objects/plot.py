class Plot:
    def __init__(self):
        self.contains = None

    def place_plant(self, plant):
        if self.contains is not None:
            raise ValueError("Plot is already occupied")
        self.contains = plant

    def remove_plant(self):
        self.contains = None

    def cotaints_plant(self):
        return self.contains is not None
