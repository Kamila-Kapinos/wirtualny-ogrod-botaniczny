class Plant:
    def __init__(self, name: str, emoji: str = '🌱'):
        self.name = name
        self.emoji = emoji
        self.plant_level = 0
        self.care_requirements = {
            "water_frequency": 0,
            "sunlight_requirements": 0,
        }
        self.is_watered = False
        self.is_in_sunlight = False
