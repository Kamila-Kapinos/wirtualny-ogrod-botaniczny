from .plant import Plant
from .fruit import Fruit


class Tree(Plant):
    def __init__(self, name: str, emoji: str = '🌳', reproduce_level: int = 15, max_fruits: int = 15):
        super().__init__(name, emoji, reproduce_level)
        self._blooming = False  # tree can bloom and later bears fruit.
        self._fruit_bearing = False
        self._leaves = False
        self._max_fruits = max_fruits
        self._fruit_list = []

    def _grow(self):
        super()._grow()

        # TODO: this is just a concept
        self._blooming = self._plant_level >= 10
        self._fruit_bearing = self._plant_level >= 15
        self._leaves = self._plant_level >= 5

    def update(self, is_in_sunlight: bool, is_raining: bool):
        super().update(is_in_sunlight, is_raining)

        #  TODO: this is just a concept
        if self._blooming:
            self._bloom()
        if self._fruit_bearing:
            # changes flower to fruit
            pass
        # Just droping leaves idk what for
        if self._leaves:
            self._foliate()

    def _foliate(self):
        pass

    # Based on time
    def _drop_leaves(self):
        pass

    def harvest(self) -> list:
        harvested = []
        for index, fruit in enumerate(self._fruit_list):
            if fruit.is_ripe():
                harvested.append(self._fruit_list.pop(index))
        return harvested

    def _bloom(self) -> None:
        # Create flower class
        if len(self._fruit_list) < self._max_fruits:
            self._fruit_list.append(Fruit())

    def _fruitful(self) -> None:
        # Create fruit class
        for fruit in self._fruit_list:
            fruit.update()
