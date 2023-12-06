from .plant import Plant
from .fruit import Fruit


class Bush(Plant):
    def __init__(self, name: str, emoji: str = '😳', reproduce_level: int = 10):
        super().__init__(name, emoji, reproduce_level)
        self._blooming = False  # tree can bloom and later bears fruit.
        self._bears_fruit = False
        self._leaves = False

    def _foliate(self):
        pass

    def _drop_leaves(self):
        pass

    def harvest(self) -> Fruit:
        # TODO: add functionality to harvest fruit
        pass

    def _bear_fruit(self):
        # Create fruit class
        self._bears_fruit = Fruit()
        pass
