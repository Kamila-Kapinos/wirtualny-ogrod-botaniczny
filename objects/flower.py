from .plant import Plant
from random import choice


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.__colors = {"🌸": "white-pink", "🌼": "yellow", "🌻": "yellow", "🌺": "pomegranate-pink", "🌹": "red",
                         "🌷": "pink", "🪻": "purple"}
        self.emoji, self._color = choice(list(self.__colors.items()))