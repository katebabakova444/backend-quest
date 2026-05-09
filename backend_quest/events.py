from player import Player
from constants import TRAVEL, REST, STUDY, FIND_COFFEE
from helpers import apply_effects
import random

EVENTS = {
    TRAVEL: {
        "Istanbul": [{"description": "Your flight is delayed again."
                                     "You spend hours in the airport trying not to question every life decision.",
                      "effects":{"energy": -10, "money": -50 , "stress": 10}}],
        "Las Vegas": [{"description": "Las Vegas tries to distract you with lights, noise, and bad financial decisions."
                                      "You stay focused, barely.",
                       "effects":{"energy": -5, "money": -100, "stress": 10, "knowledge": 5}}],
    },
    REST: {
        "Denver": [{"description": "You finally sleep through the night.",
                  "effects":{"energy": 20, "stress": -15, "coffee": -5}}],
        "Santa Cruz": [{"description": "You sit near the ocean. Your nervous system stops acting like a broken alarm.",
                        "effects":{"energy": 15, "stress": -15}}],
    },
    STUDY: {
        "Chicago": [{"description": "You study Python after a long shift. It is painful, but the concepts finally start connecting.",
                     "effects":{"knowledge": 20, "energy": -10, "stress": 5, "coffee": -5}}],
        "San Jose": [{"description": "You explain your project out loud and finally understand what your code is doing.",
                      "effects":{"knowledge": 20, "energy": -5, "stress": -10}}]
    },
    FIND_COFFEE: {
        "Los Angeles": [{"description": "You find a beautiful coffee shop with laptop people everywhere. The latte costs too much, obviously.",
                         "effects":{"coffee": 15, "money": -75, "stress": -5, "knowledge": 5}}],
        "Santa Cruz": [{"description": "You find matcha, stable Wi-Fi, and a quite corner.",
                        "effects":{"coffee": 10, "stress": -10, "money": -50, "knowledge": 5}}],
    }
}

def trigger_events(action, location_name, player):
    if action in EVENTS and location_name in EVENTS[action]:
        if random.random() < 1.0:
            event = random.choice(EVENTS[action][location_name])
            if not event["effects"]:
                return
            print("\n--- RANDOM EVENT ---")
            print(event["description"])
            apply_effects(player, event["effects"])
