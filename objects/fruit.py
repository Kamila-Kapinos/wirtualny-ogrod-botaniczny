from random import choice


class Fruit:
    def __init__(self, name='test'):
        self.__emojis_and_colors = {
            "🍎": "red", "🍌": "yellow", "🍇": "purple",
            "🍊": "orange", "🍓": "red", "🍉": "green-red", "🍍": "yellow-brown",
            "🥜": "brown", "🌰": "dark-brown", "🥥": "white-brown"
        }
        self._name = name
        self._is_edible = True
        self._emoji, self._color = choice(list(self.__emojis_and_colors.items()))
        self.status = "growing"  # growing / ready / rotten

    def update(self):
        pass
