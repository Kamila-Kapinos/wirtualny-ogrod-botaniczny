from .plant import Plant
from .fruit import Fruit


class Tree(Plant):
    def __init__(self, name: str, emoji: str = '🌳', reproduce_level: int = 15, max_fruits: int = 15):
        super().__init__(name, emoji, reproduce_level)
        self._blooming = False  # tree can bloom and later bears fruit.
        self._fruitful = False
        self._leaves = False
        self._max_fruits = max_fruits
        self._fruit_list = [Fruit().update(),Fruit().update(),Fruit()]

    def _grow(self):
        super()._grow()

        # TODO: this is just a concept
        self._blooming = self._plant_level >= 10
        self._fruit_bearing = self._plant_level >= 15
        if self._plant_level >= 5 and not self._leaves:
            self._foliate()

    def update(self, is_in_sunlight: bool, is_raining: bool):
        super().update(is_in_sunlight, is_raining)

        #  TODO: this is just a concept
        if self._blooming:
            self._bloom()
        if self._fruitful:
            # grows flower to fruit
            self._fruit_bearing()
        # Just dropping leaves idk what for
        if self._leaves:
            self._foliate()

    def _foliate(self) -> None:
        self._leaves = True

    # Based on time
    def _drop_leaves(self) -> None:
        self._leaves = False

    def harvest(self) -> list:
        harvested = []
        # Iterate over a copy of the list
        for fruit in self._fruit_list[:]:
            if fruit.is_ripe():
                harvested.append(fruit)
                self._fruit_list.remove(fruit)  # Remove the fruit from the original list
        # print harvested fruits
        return harvested

    
    def _bloom(self) -> None:
        # Create flower class
        if len(self._fruit_list) < self._max_fruits:
            self._fruit_list.append(Fruit())

    def _fruit_bearing(self) -> None:
        # Create fruit class
        for fruit in self._fruit_list:
            fruit.update()

    def get_status(self):
        status = super().get_status()
        status['fruitful'] = self._fruitful
        status['blooming'] = self._blooming
        status['leaves'] = self._leaves
        status['fruit_list'] = self._fruit_list
        return status
    
