import tkinter as tk
from tkinter import messagebox
from game_controller import GameController

class GameUI:
    def __init__(self, root, game_controller):
        self.root = root
        self.game_controller = game_controller
        self.player = game_controller.player

        # Set up the main window with a 16:9 resolution and larger size
        self.root.title("Space Odyssey Game")
        self.root.geometry("1280x720")  # 16:9 aspect ratio at 720p resolution
        self.root.minsize(720, 720)  # Minimum resolution set to twice the width of the image box and its height
        self.root.maxsize(720, 720)  # Minimum resolution set to twice the width of the image box and its height

        # Create a frame to hold the event description and image placeholder side by side
        self.top_frame = tk.Frame(self.root)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

        # Configure root and top frame to adjust dynamically
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.top_frame.grid_columnconfigure(0, weight=3)
        self.top_frame.grid_columnconfigure(1, weight=0)

        # Add a text widget for event description (in the left part of the top frame)
        self.event_description = tk.Text(self.top_frame, wrap="word", height=10, font=("Helvetica", 12))
        self.event_description.grid(row=0, column=0, sticky="nsew", padx=10)
        self.event_description.insert(tk.END, "Event Log: Welcome to Space Odyssey. Your journey begins here.")

        # Create placeholder for an image in the right part of the top frame (fixed resolution)
        self.image_placeholder = tk.Frame(self.top_frame, width=300, height=200, bg="lightgrey")
        self.image_placeholder.grid(row=0, column=1, sticky="ne", padx=10)
        self.image_placeholder.grid_propagate(False)  # Prevent resizing to keep fixed dimensions

        # Create labels to display player stats
        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.grid(row=1, column=0, sticky="nw", padx=20, pady=20)

        # Update font size for player stats
        font_style = ("Helvetica", 14)

        self.offense_label = tk.Label(self.stats_frame, text=f"OFF    :", font=font_style, anchor="w", width=10)
        self.offense_label.grid(row=0, column=0, padx=10, sticky="w")
        self.offense_value = tk.Label(self.stats_frame, text=f"{self.player.offense}", font=font_style, anchor="e", width=5)
        self.offense_value.grid(row=0, column=1, padx=10, sticky="e")

        self.endurance_label = tk.Label(self.stats_frame, text=f"END    :", font=font_style, anchor="w", width=10)
        self.endurance_label.grid(row=1, column=0, padx=10, sticky="w")
        self.endurance_value = tk.Label(self.stats_frame, text=f"{self.player.endurance}", font=font_style, anchor="e", width=5)
        self.endurance_value.grid(row=1, column=1, padx=10, sticky="e")

        self.endurance_label = tk.Label(self.stats_frame, text=f"SHD    :", font=font_style, anchor="w", width=10)
        self.endurance_label.grid(row=2, column=0, padx=10, sticky="w")
        self.endurance_value = tk.Label(self.stats_frame, text=f"{self.player.shield}", font=font_style, anchor="e", width=5)
        self.endurance_value.grid(row=2, column=1, padx=10, sticky="e")

        self.charisma_label = tk.Label(self.stats_frame, text=f"CHA    :", font=font_style, anchor="w", width=10)
        self.charisma_label.grid(row=3, column=0, padx=10, sticky="w")
        self.charisma_value = tk.Label(self.stats_frame, text=f"{self.player.charisma}", font=font_style, anchor="e", width=5)
        self.charisma_value.grid(row=3, column=1, padx=10, sticky="e")

        self.psychia_label = tk.Label(self.stats_frame, text=f"PSY    :", font=font_style, anchor="w", width=10)
        self.psychia_label.grid(row=4, column=0, padx=10, sticky="w")
        self.psychia_value = tk.Label(self.stats_frame, text=f"{self.player.psychia}", font=font_style, anchor="e", width=5)
        self.psychia_value.grid(row=4, column=1, padx=10, sticky="e")

        # Create resource labels with better formatting
        self.resource_frame = tk.Frame(self.root)
        self.resource_frame.grid(row=2, column=0, sticky="nw", padx=20, pady=20)

        self.resources_label = tk.Label(self.resource_frame, text="Resources:", font=font_style)
        self.resources_label.pack(anchor="w")

        self.resources_detail_label = tk.Label(
            self.resource_frame,
            text="\n".join([f"{key}: {value}" for key, value in self.player.resources.items()]),
            justify="left",
            font=font_style
        )
        self.resources_detail_label.pack(anchor="w")

        # Action buttons with updated layout
        self.actions_frame = tk.Frame(self.root)
        self.actions_frame.grid(row=3, column=0, pady=40)

        button_font_style = ("Helvetica", 12)

        self.gather_resources_button = tk.Button(self.actions_frame, text="Gather Resources", command=self.gather_resources, font=button_font_style)
        self.gather_resources_button.grid(row=0, column=0, padx=15, pady=10)

        self.upgrade_ship_button = tk.Button(self.actions_frame, text="Upgrade Ship", command=self.upgrade_ship, font=button_font_style)
        self.upgrade_ship_button.grid(row=0, column=1, padx=15, pady=10)

        self.explore_ruins_button = tk.Button(self.actions_frame, text="Explore Ruins", command=self.explore_ruins, font=button_font_style)
        self.explore_ruins_button.grid(row=0, column=2, padx=15, pady=10)

        self.move_system_button = tk.Button(self.actions_frame, text="Move to Next Star System", command=self.move_to_next_star_system, font=button_font_style)
        self.move_system_button.grid(row=1, column=1, pady=10)

        self.trigger_battle_button = tk.Button(self.actions_frame, text="Trigger Battle", command=self.trigger_battle, font=button_font_style)
        self.trigger_battle_button.grid(row=2, column=1, pady=10)

    def update_event_description(self, message):
        # Clear previous message and update the text widget with the new event description
        self.event_description.delete(1.0, tk.END)
        self.event_description.insert(tk.END, message)

    def gather_resources(self):
        # Use GameController to gather resources
        self.game_controller.gather_resources(self.game_controller.star_systems[self.game_controller.current_star_system_index])
        # Update resources label after gathering
        self.resources_detail_label.config(text="\n".join([f"{key}: {value}" for key, value in self.player.resources.items()]))
        # Update event description
        self.update_event_description("You have gathered resources in the current star system.")
        messagebox.showinfo("Action", "Gathering resources completed.")

    def upgrade_ship(self):
        # Use GameController to upgrade the ship
        self.game_controller.upgrade_ship()
        # Update endurance label after upgrade
        self.endurance_value.config(text=f"{self.player.endurance}")
        # Update event description
        self.update_event_description("You have upgraded your ship. Its endurance has increased.")
        messagebox.showinfo("Action", "Upgrading ship completed.")

    def explore_ruins(self):
        # Use GameController to explore ruins
        self.game_controller.explore_ruins()
        # Update psychia label after exploration
        self.psychia_value.config(text=f"{self.player.psychia}")
        # Update event description
        self.update_event_description("You have explored the ancient ruins and gained new psychic powers.")
        messagebox.showinfo("Action", "Exploring ruins completed.")

    def move_to_next_star_system(self):
        # Use GameController to move to the next star system
        if self.game_controller.current_star_system_index < len(self.game_controller.star_systems) - 1:
            self.game_controller.current_star_system_index += 1
            self.update_event_description(f"Moving to the next star system: {self.game_controller.star_systems[self.game_controller.current_star_system_index].name}")
            messagebox.showinfo("Action", "Moving to the next star system...")
        else:
            self.update_event_description("Congratulations! You have found your home planet!")
            messagebox.showinfo("Action", "Congratulations! You have found your home planet!")



    # BATTLE FUNCTIONS
    def trigger_battle(self):
        # Create a modal battle window
        battle_window = tk.Toplevel(self.root)
        battle_window.title("Battle Window")
        battle_window.geometry("600x400")
        
        # Make the battle window modal
        battle_window.transient(self.root)  # Set the battle window in front of the main window
        battle_window.grab_set()  # Prevent interaction with the main window
        
        # Add battle-related UI elements
        battle_label = tk.Label(battle_window, text="You have entered a battle!", font=("Helvetica", 16))
        battle_label.pack(pady=20)

        attack_button = tk.Button(battle_window, text="Attack", command=lambda: self.attack(battle_window))
        attack_button.pack(pady=10)

        defend_button = tk.Button(battle_window, text="Defend", command=lambda: self.defend(battle_window))
        defend_button.pack(pady=10)

    def attack(self, battle_window):
        # Example logic for attacking
        # Update stats or provide battle outcome
        messagebox.showinfo("Battle", "You attacked the enemy!")
        self.end_battle(battle_window)

    def defend(self, battle_window):
        # Example logic for defending
        # Update stats or provide battle outcome
        messagebox.showinfo("Battle", "You defended yourself!")
        self.end_battle(battle_window)

    def end_battle(self, battle_window):
        # Close the battle window to end the battle
        battle_window.destroy()
        # Optionally update the event description or main game state
        self.update_event_description("The battle has concluded.")

# Example usage
if __name__ == "__main__":
    from models.player import Player
    from models.star_system import StarSystem

    # Create player, and star systems
    player = Player(race="Human")
    star_systems = [
        StarSystem(name="Alpha Centauri", difficulty_level=1),
        StarSystem(name="Betelgeuse", difficulty_level=2),
        StarSystem(name="Vega", difficulty_level=3)
    ]

    # Create GameController
    game_controller = GameController(player, star_systems)

    # Set up the Tkinter root window
    root = tk.Tk()  
    ui = GameUI(root, game_controller)
    root.mainloop()
