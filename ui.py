import tkinter as tk
from tkinter import messagebox
from game_controller import GameController

class GameUI:
    def __init__(self, root, game_controller):
        self.root = root
        self.game_controller = game_controller
        self.player = game_controller.player

        # Set up the main window
        self.root.title("Space Odyssey Game")
        self.root.geometry("1280x720")
        self.root.minsize(720, 720)
        self.root.maxsize(720, 720)

        # Create a frame for event description and image placeholder
        self.top_frame = tk.Frame(self.root)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=3)
        self.top_frame.grid_columnconfigure(1, weight=0)

        # Add a text widget for event description
        self.event_description = tk.Text(self.top_frame, wrap="word", height=10, font=("Helvetica", 12))
        self.event_description.grid(row=0, column=0, sticky="nsew", padx=10)
        self.event_description.insert(tk.END, "Event Log: Welcome to Space Odyssey. Your journey begins here.")

        # Create placeholder for an image in the right part
        self.image_placeholder = tk.Frame(self.top_frame, width=300, height=200, bg="lightgrey")
        self.image_placeholder.grid(row=0, column=1, sticky="ne", padx=10)
        self.image_placeholder.grid_propagate(False)

        # Create labels to display player stats
        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.grid(row=1, column=0, sticky="nw", padx=20, pady=20)
        font_style = ("Helvetica", 14)
        self.create_stat_labels(font_style)

        # Resource labels
        self.create_resource_labels(font_style)

        # Action buttons
        self.create_action_buttons()

    def create_stat_labels(self, font_style):
        stats = [("OFF", self.player.offense), ("END", self.player.endurance), ("SHD", self.player.shield),
                 ("CHA", self.player.charisma), ("PSY", self.player.psychia)]
        for i, (stat, value) in enumerate(stats):
            label = tk.Label(self.stats_frame, text=f"{stat}    :", font=font_style, anchor="w", width=10)
            label.grid(row=i, column=0, padx=10, sticky="w")
            value_label = tk.Label(self.stats_frame, text=f"{value}", font=font_style, anchor="e", width=5)
            value_label.grid(row=i, column=1, padx=10, sticky="e")

    def create_resource_labels(self, font_style):
        self.resource_frame = tk.Frame(self.root)
        self.resource_frame.grid(row=2, column=0, sticky="nw", padx=20, pady=20)
        self.resources_label = tk.Label(self.resource_frame, text="Resources:", font=font_style)
        self.resources_label.pack(anchor="w")
        self.resources_detail_label = tk.Label(self.resource_frame,
                                               text="\n".join([f"{key}: {value}" for key, value in self.player.resources.items()]),
                                               justify="left", font=font_style)
        self.resources_detail_label.pack(anchor="w")

    def create_action_buttons(self):
        button_font_style = ("Helvetica", 12)
        self.actions_frame = tk.Frame(self.root)
        self.actions_frame.grid(row=3, column=0, pady=40)

        actions = [("Gather Resources", self.gather_resources),
                   ("Upgrade Ship", self.upgrade_ship),
                   ("Explore Ruins", self.explore_ruins),
                   ("Move to Next Star System", self.move_to_next_star_system),
                   ("Trigger Battle", self.trigger_battle)]

        for i, (text, command) in enumerate(actions):
            row = i // 3
            col = i % 3
            button = tk.Button(self.actions_frame, text=text, command=command, font=button_font_style)
            button.grid(row=row, column=col, padx=15, pady=10)

    def update_event_description(self, message):
        self.event_description.delete(1.0, tk.END)
        self.event_description.insert(tk.END, message)

    def gather_resources(self):
        self.game_controller.gather_resources()
        self.update_resource_display()
        self.update_event_description("You have gathered resources in the current star system.")
        messagebox.showinfo("Action", "Gathering resources completed.")

    def upgrade_ship(self):
        self.game_controller.upgrade_ship()
        self.update_stat_display()
        self.update_event_description("You have upgraded your ship. Its endurance has increased.")
        messagebox.showinfo("Action", "Upgrading ship completed.")

    def explore_ruins(self):
        self.game_controller.explore_ruins()
        self.update_stat_display()
        self.update_event_description("You have explored the ancient ruins and gained new psychic powers.")
        messagebox.showinfo("Action", "Exploring ruins completed.")

    def move_to_next_star_system(self):
        success, message = self.game_controller.move_to_next_star_system()
        self.update_event_description(message)
        messagebox.showinfo("Action", message)

    def trigger_battle(self):
        battle_window = tk.Toplevel(self.root)
        battle_window.title("Battle Window")
        battle_window.geometry("600x400")
        battle_window.transient(self.root)
        battle_window.grab_set()
        battle_label = tk.Label(battle_window, text="You have entered a battle!", font=("Helvetica", 16))
        battle_label.pack(pady=20)

        attack_button = tk.Button(battle_window, text="Attack", command=lambda: self.attack(battle_window))
        attack_button.pack(pady=10)

        defend_button = tk.Button(battle_window, text="Defend", command=lambda: self.defend(battle_window))
        defend_button.pack(pady=10)

    def attack(self, battle_window):
        messagebox.showinfo("Battle", "You attacked the enemy!")
        self.end_battle(battle_window)

    def defend(self, battle_window):
        messagebox.showinfo("Battle", "You defended yourself!")
        self.end_battle(battle_window)

    def end_battle(self, battle_window):
        battle_window.destroy()
        self.update_event_description("The battle has concluded.")

    def update_resource_display(self):
        self.resources_detail_label.config(text="\n".join([f"{key}: {value}" for key, value in self.player.resources.items()]))

    def update_stat_display(self):
        stats = [self.player.offense, self.player.endurance, self.player.shield, self.player.charisma, self.player.psychia]
        for i, value in enumerate(stats):
            label = self.stats_frame.grid_slaves(row=i, column=1)[0]
            label.config(text=f"{value}")

# Example usage
if __name__ == "__main__":
    from models.player import Player
    from models.star_system import StarSystem

    player = Player(race="Human")
    star_systems = [StarSystem(name="Alpha Centauri", difficulty_level=1),
                    StarSystem(name="Betelgeuse", difficulty_level=2),
                    StarSystem(name="Vega", difficulty_level=3)]

    game_controller = GameController(player, star_systems)  # Assuming None for ship for simplicity
    root = tk.Tk()
    ui = GameUI(root, game_controller)
    root.mainloop()
