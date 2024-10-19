class Player:
    def __init__(self, race):
        self.race = race  # Player race (affects initial stats)
        self.offense = 5   # Starting offense value
        self.endurance = 10  # Starting endurance value
        self.shield = 2
        self.resources = {
            "Food": 3,  # Used to maintain crew members
            "Fuel": 3,  # Allows movement between star systems (must be managed well to ensure actions and travel)
            "Credits": 2,  # Currency used for trading and upgrades
            "Scraps": 2,  # Used for a variety of actions involving spaceship improvements and can be traded
            "Energy Cells": 1  # Used for powering certain equipment
        }
        self.size = 25
        self.crew_members = []
        self.fuel_efficiency = 3  # Actions per star system before event trigger
        self.charisma = 4   # Starting charisma
        self.psychia = 3    # Psychic power used for artifacts

    def add_resource(self, resource, amount):
        current_total = sum(self.resources.values())
        if current_total + amount <= self.max_resources:
            self.resources[resource] = min(self.resources.get(resource, 0) + amount, 7)
        else:
            print("Not enough space to add more resources.")

    def hire_crew_member(self, crew_member):
        self.crew_members.append(crew_member)


    def upgrade(self, attribute, value):
        if attribute == "offense":
            self.offense += value
        elif attribute == "endurance":
            self.endurance += value
        elif attribute == "shield":
            self.shield += value
        elif attribute == "size":
            self.size += value
        elif attribute == "fuel_efficiency":
            self.fuel_efficiency += value
        

    # Additional methods for managing stats, resources, etc.
