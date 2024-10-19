class CrewMember:
    def __init__(self, name, skill, loyalty):
        self.name = name
        self.skill = skill  # Special skill (e.g., engineer, pilot)
        self.loyalty = loyalty  # Loyalty level (affected by charisma)

    def change_loyalty(self, amount):
        self.loyalty += amount

    # Additional methods for crew-related actions
