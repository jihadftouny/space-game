import tkinter as tk
from tkinter import messagebox
from game_controller import GameController

class GameUI(tk.Tk):
    def __init__(self, game_controller):
        super().__init__()
        self.game_controller = game_controller
        self.title("Space Odyssey Game")
        self.geometry("800x600")

        # Container to hold multiple screens
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        # Create all the screens and add them to the container
        for F in (MainGameScreen, PlayerActionsScreen, ResourceStatsScreen, EventScreen, CombatScreen):
            frame = F(self.container, self, game_controller)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainGameScreen)

    def show_frame(self, cont):
        """Bring the requested frame to the front."""
        frame = self.frames[cont]
        frame.tkraise()

# Define Main Game Screen
class MainGameScreen(tk.Frame):
    def __init__(self, parent, controller, game_controller):
        super().__init__(parent)
        self.controller = controller
        self.game_controller = game_controller

        # Example elements in the main screen
        label = tk.Label(self, text="Main Game Screen")
        label.pack(pady=10, padx=10)

        action_button = tk.Button(self, text="Go to Player Actions",
                                  command=lambda: controller.show_frame(PlayerActionsScreen))
        action_button.pack()

# Define Player Actions Screen
class PlayerActionsScreen(tk.Frame):
    def __init__(self, parent, controller, game_controller):
        super().__init__(parent)
        self.controller = controller
        self.game_controller = game_controller

        # Example elements in the player actions screen
        label = tk.Label(self, text="Player Actions Screen")
        label.pack(pady=10, padx=10)

        gather_resources_button = tk.Button(self, text="Gather Resources", command=self.gather_resources)
        gather_resources_button.pack(pady=5)

        upgrade_ship_button = tk.Button(self, text="Upgrade Ship", command=self.upgrade_ship)
        upgrade_ship_button.pack(pady=5)

        explore_ruins_button = tk.Button(self, text="Explore Ruins", command=self.explore_ruins)
        explore_ruins_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Main Screen",
                                command=lambda: controller.show_frame(MainGameScreen))
        back_button.pack(pady=10)

    def gather_resources(self):
        # Use GameController to gather resources
        self.game_controller.gather_resources(self.game_controller.star_systems[self.game_controller.current_star_system_index])
        messagebox.showinfo("Action", "Gathering resources completed.")

    def upgrade_ship(self):
        # Use GameController to upgrade the ship
        self.game_controller.upgrade_ship()
        messagebox.showinfo("Action", "Upgrading ship completed.")

    def explore_ruins(self):
        # Use GameController to explore ruins
        self.game_controller.explore_ruins()
        messagebox.showinfo("Action", "Exploring ruins completed.")

# Define Resource Stats Screen
class ResourceStatsScreen(tk.Frame):
    def __init__(self, parent, controller, game_controller):
        super().__init__(parent)
        label = tk.Label(self, text="Resource Stats Screen")
        label.pack(pady=10, padx=10)

# Define Event Screen
class EventScreen(tk.Frame):
    def __init__(self, parent, controller, game_controller):
        super().__init__(parent)
        label = tk.Label(self, text="Event Screen")
        label.pack(pady=10, padx=10)

# Define Combat Screen
class CombatScreen(tk.Frame):
    def __init__(self, parent, controller, game_controller):
        super().__init__(parent)
        label = tk.Label(self, text="Combat Screen")
        label.pack(pady=10, padx=10)

# Example Usage
if __name__ == "__main__":
    from models.player import Player
    from models.star_system import StarSystem

    # Create player, ship, and star systems
    player = Player(race="Human")
    star_systems = [
        StarSystem(name="Alpha Centauri", difficulty_level=1),
        StarSystem(name="Betelgeuse", difficulty_level=2),
        StarSystem(name="Vega", difficulty_level=3)
    ]

    # Create GameController
    game_controller = GameController(player, star_systems)

    # Create the game UI
    app = GameUI(game_controller)
    app.mainloop()
