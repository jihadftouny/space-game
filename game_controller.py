import random

class GameController:
    def __init__(self, player, star_systems):
        self.player = player
        self.star_systems = star_systems
        self.current_star_system_index = 0
        self.event_manager = EventManager()

    def gather_resources(self):
        current_star_system = self.star_systems[self.current_star_system_index]
        for resource, amount in current_star_system.resources_available.items():
            self.player.add_resource(resource, amount)
        return "Resources gathered successfully."

    def upgrade_ship(self):
        self.player.endurance += 1

    def explore_ruins(self):
        self.player.psychia += 1

    def move_to_next_star_system(self):
        if self.current_star_system_index < len(self.star_systems) - 1:
            self.current_star_system_index += 1
            return True, f"Moving to the next star system: {self.star_systems[self.current_star_system_index].name}"
        else:
            return False, "Congratulations! You have found your home planet!"

    def trigger_event(self):
        event = self.event_manager.trigger_random_event()
        if event:
            event['effect'](self.player)
            return f"Event Triggered: {event['description']}"
        return None

class EventManager:
    def __init__(self):
        self.events = [
            {"type": "beneficial", "description": "You found extra fuel!", "effect": self.extra_fuel},
            {"type": "harmful", "description": "Your ship took damage from an asteroid field!", "effect": self.ship_damage},
            {"type": "mixed", "description": "You traded food for fuel.", "effect": self.trade_food_for_fuel}
        ]

    def trigger_random_event(self):
        if self.events:
            return random.choice(self.events)
        return None

    def extra_fuel(self, player):
        player.add_resource("fuel", 2)

    def ship_damage(self, player):
        player.endurance -= 2

    def trade_food_for_fuel(self, player):
        if player.resources.get("food", 0) > 0:
            player.resources["food"] -= 1
            player.add_resource("fuel", 1)
        else:
            print("No food available to trade.")
