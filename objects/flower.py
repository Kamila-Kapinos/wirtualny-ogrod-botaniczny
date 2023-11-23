from .plant import Plant


class Flower(Plant):
    def __init__(self, name: str, emoji: str = '🌻'):
        super().__init__(name, emoji)
