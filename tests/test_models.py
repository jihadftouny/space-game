from models.player import Player
from models.ship import Ship
from models.star_system import StarSystem
from models.crew_member import CrewMember

# Create Player
player = Player(race="Human")
print(player.resources)

# Create Ship
ship = Ship()
print(f"Ship size: {ship.size}, offense: {ship.offense}")

# Create StarSystem
star_system = StarSystem(name="Alpha Centauri", difficulty_level=2)
print(star_system.resources_available)

# Create CrewMember
crew_member = CrewMember(name="Jack", skill="Engineer", loyalty=5)
print(f"Crew Member: {crew_member.name}, Skill: {crew_member.skill}")
