from .plant import Plant
from .fruit import Fruit


class Tree(Plant):
    def __init__(self, name: str, emoji: str = '🌳', reproduce_level: int = 15):
        super().__init__(name, emoji, reproduce_level)
        self._blooming = False  # tree can bloom and later bears fruit.
        self._bears_fruit = False
        self._leaves = False

    def _grow(self):
        super()._grow()

        # TODO: this is just a concept
        self._blooming = self._plant_level >= 10
        self._bears_fruit = self._plant_level >= 15
        self._leaves = self._plant_level >= 5

    def update(self, is_in_sunlight: bool, is_raining: bool):
        super().update(is_in_sunlight, is_raining)

        #  TODO: this is just a concept
        if self._blooming:
            self._bear_fruit()
        if self._bears_fruit:
            self._drop_leaves()
        if self._leaves:
            self._foliate()

    def _foliate(self):
        pass

    # Based on time
    def _drop_leaves(self):
        pass

    def harvest(self) -> Fruit:
        # TODO: add functionality to harvest fruit
        pass

    def _bear_fruit(self):
        # Create fruit class
        self._bears_fruit = Fruit()
        pass
