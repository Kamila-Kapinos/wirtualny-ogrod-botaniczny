from .plant import Plant
from .fruit import Fruit


class Bush(Plant):
    def __init__(self, name: str, emoji: str = '😳'):
        super().__init__(name, emoji)
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
