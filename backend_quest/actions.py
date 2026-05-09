from player import Player
from locations import LOCATIONS
from helpers import apply_effects

def travel(player):
    print("--- ACTION ---")
    print("\nYou traveled to the next location.")
    travel_effects = {"energy": -10, "money": -100, "stress": -5}
    apply_effects(player, travel_effects)
    player.current_location_index += 1

def rest(player):
    print("--- ACTION ---")
    print("\nYou took time to rest.")
    rest_effects = {"energy": 20, "stress": -25, "coffee": -5}
    apply_effects(player, rest_effects)

def study(player):
    print("--- ACTION ---")
    print("\nYou studied Python.")
    study_effects = {"energy": -10, "stress": 5, "coffee": -10, "knowledge": 20}
    apply_effects(player, study_effects)

def find_coffee(player):
    print("\n--- ACTION ---")
    print("\nYou found coffee.")
    coffee_effects = {"money": -50, "coffee": 20}
    apply_effects(player, coffee_effects)
    player.turns_without_coffee = 0

