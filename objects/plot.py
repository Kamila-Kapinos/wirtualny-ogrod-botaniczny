from .plant import Plant


class Plot:
    def __init__(self):
        self._contained_plant = None

    def place_plant(self, plant: Plant):
        if self._contained_plant is not None:
            raise ValueError("Plot is already occupied")
        self._contained_plant = plant

    def remove_plant(self):
        if self._contained_plant is None:
            raise ValueError("Plot is empty")

        # method could return some information about the plant that was removed
        self._contained_plant = None

    def water_plant(self):
        if self._contained_plant is None:
            raise ValueError("Plot is empty")
        self._contained_plant.water()

    def harvest_plant(self):
        if self._contained_plant is None:
            raise ValueError("Plot is empty")
        self._contained_plant.harvest()

    def update(self, is_in_sunlight: bool, is_raining: bool):
        if self._contained_plant is None:
            pass
        self._contained_plant.update(is_in_sunlight, is_raining)

    def has_plant(self) -> bool:
        return self._contained_plant is not None

    def is_ready_to_reproduce(self) -> bool:
        if self._contained_plant is None:
            return False
        return self._contained_plant.ready_to_reproduce

    def get_plant_offspring(self) -> Plant:
        if self._contained_plant is None:
            raise ValueError("Plot is empty")
        return self._contained_plant.get_offspring()

    def __repr__(self):
        return f"Plot({self._contained_plant})"

    def __str__(self):
        return f"{self._contained_plant.emoji}"
