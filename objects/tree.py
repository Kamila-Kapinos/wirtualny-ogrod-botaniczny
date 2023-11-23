from .plant import Plant
from .fruit import Fruit


class Tree(Plant):
    def __init__(self, name: str, emoji: str = '🌳'):
        super().__init__(name, emoji)
        self.blooming = False  # tree can bloom and later bears fruit.
        self.bears_fruit = False
        self.leaves = False

    def foliate(self):
        pass

    def drop_leaves(self):
        pass

    def bear_fruit(self):
        # Create fruit class
        self.bears_fruit = Fruit()
        pass
