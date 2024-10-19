import random

class StarSystem:
    def __init__(self, name, difficulty_level):
        self.name = name
        self.difficulty_level = difficulty_level
        self.resources_available = self.generate_resources()
        self.events = []

    def generate_resources(self):
        if self.difficulty_level == 1:
            return {
                "food": random.randint(3, 5),
                "fuel": random.randint(3, 5),
                "metal": random.randint(2, 3)
            }
        elif self.difficulty_level == 2 or self.difficulty_level not in [1, 2, 3]:
            return {
                "food": random.randint(1, 4),
                "fuel": random.randint(1, 4),
                "metal": random.randint(1, 2)
            }
        elif self.difficulty_level == 3:
            return {
                "food": random.randint(0, 2),
                "fuel": random.randint(0, 2),
                "metal": random.randint(0, 1)
            }

    def trigger_event(self):
        # Logic for triggering a random event
        event = random.choice(self.events) if self.events else None
        return event

    # Additional methods for managing star system events
