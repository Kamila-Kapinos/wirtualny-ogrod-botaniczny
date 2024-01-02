from .plant import Plant
from .fruit import Fruit


class Bush(Plant):
    def __init__(self, name: str, emoji: str = '🥦', reproduce_level: int = 10, max_fruits: int = 15):
        super().__init__(name, emoji, reproduce_level)
        self._max_fruits = max_fruits
        self._blooming = False  # tree can bloom and later bears fruit.
        self._fruitful = False
        self._leaves = False
        self._fruit_list = []

    def _foliate(self):
        pass

    def _drop_leaves(self):
        pass

    def update(self, is_in_sunlight: bool, is_raining: bool):
        super().update(is_in_sunlight, is_raining)

        # TODO: this is just a concept
        self._blooming = self._plant_level >= 10
        self._fruitful = self._plant_level >= 15
        self._leaves = self._plant_level >= 5

        if self._blooming:
            self._bloom()
        if self._fruitful:
            # grows flower to fruit
            self._fruit_bearing()

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

    def _fruit_bearing(self) -> None:
        # Create fruit class
        for fruit in self._fruit_list:
            fruit.update()
