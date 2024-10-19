class GameController:
    def __init__(self, player, ship, star_systems):
        self.player = player  # Player object
        self.ship = ship  # Ship object
        self.star_systems = star_systems  # List of StarSystem objects
        self.current_star_system_index = 0
        self.event_manager = EventManager()

    def start_game(self):
        while self.current_star_system_index < len(self.star_systems):
            current_star_system = self.star_systems[self.current_star_system_index]
            print(f"Entering star system: {current_star_system.name}")
            self.play_star_system(current_star_system)
            self.current_star_system_index += 1
            self.trigger_event()

        print("Congratulations! You have found your home planet!")

    def play_star_system(self, star_system):
        actions_taken = 0
        while actions_taken < 3:
            print("Choose an action: 1) Gather Resources, 2) Upgrade Ship, 3) Explore Ruins")
            action = int(input("Enter action (1-3): "))
            if action == 1:
                self.gather_resources(star_system)
            elif action == 2:
                self.upgrade_ship()
            elif action == 3:
                self.explore_ruins()
            else:
                print("Invalid action. Please choose again.")
                continue
            actions_taken += 1

    def gather_resources(self, star_system):
        for resource, amount in star_system.resources_available.items():
            self.player.add_resource(resource, amount)
        print("Resources gathered successfully.")

    def upgrade_ship(self):
        print("Upgrading ship...")
        # Placeholder: Add logic to upgrade ship

    def explore_ruins(self):
        print("Exploring ancient ruins...")
        # Placeholder: Add logic to explore ruins

    def trigger_event(self):
        event = self.event_manager.trigger_random_event()
        if event:
            print(f"Event Triggered: {event['description']}")
            # Placeholder: Handle the effects of the event

# Event Manager
import random

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

    def ship_damage(self, ship):
        ship.endurance -= 2

    def trade_food_for_fuel(self, player):
        if player.resources.get("food", 0) > 0:
            player.resources["food"] -= 1
            player.add_resource("fuel", 1)
        else:
            print("No food available to trade.")