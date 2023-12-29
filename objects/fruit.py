from random import choice


class Fruit:
    def __init__(self, name='test'):
        self._color = None
        self._emoji = '🌸'

        self.__emojis_and_colors = {
            "🍎": "red", "🍌": "yellow", "🍇": "purple",
            "🍊": "orange", "🍓": "red", "🍉": "green-red", "🍍": "yellow-brown",
            "🥜": "brown", "🌰": "dark-brown", "🥥": "white-brown"
        }
        self._name = name
        self._is_ripe = False
        
    def update(self):
        self._emoji, self._color = choice(list(self.__emojis_and_colors.items()))

    def is_ripe(self):
        return self._is_ripe
