
from backend_quest.player import Player
from backend_quest.actions import travel, rest, study, find_coffee
from backend_quest.constants import TRAVEL, REST, STUDY, FIND_COFFEE
from backend_quest.events import trigger_events
from backend_quest.weather import get_weather, apply_weather_effects
from backend_quest.helpers import apply_effects
from backend_quest.locations import LOCATIONS

class GameEngine:
    def __init__(self, player, locations, total_locations):
        self.player = player
        self.locations = locations
        self.total_locations = total_locations

    def get_current_location(self):
        if self.player.current_location_index <= len(self.locations):
            return self.locations[self.player.current_location_index]
        else:
            return None

    def is_game_over(self):
        if not self.player.is_alive():
            return True
        if self.player.reached_final_destination(self.total_locations):
            return True
        else:
            return False

    def get_game_status(self):
        return self.player.get_final_status(self.total_locations)

    def process_action(self, action):
        if action == TRAVEL:
            travel(self.player)
            return True
        elif action == REST:
            rest(self.player)
            return True
        elif action == STUDY:
            study(self.player)
            return True
        elif action == FIND_COFFEE:
            find_coffee(self.player)
            return True
        else:
            return False
    def update_coffee_turns(self, action):
        if action != FIND_COFFEE:
            self.player.turns_without_coffee += 1

    def process_events(self, action):
        current_location = self.get_current_location()
        if current_location is None:
            return
        location_name = current_location["name"]
        trigger_events(action, location_name, self.player)

    def apply_travel_effects(self, action):
        if action != TRAVEL:
            return
        current_location = self.get_current_location()
        if current_location is None:
            return
        apply_effects(self.player, current_location["effects"])
        location_name = current_location["name"]
        weather = get_weather(location_name)
        apply_weather_effects(self.player, weather)
        self.player.clamp_stats()

    def play_turn(self, action):
        if self.is_game_over():
            return {
                "success": False,
                "message": "Game is already over.",
                "action": action,
                "state": self.get_state()
            }
        action_processed = self.process_action(action)
        if not action_processed:
            self.apply_invalid_input_penalty()
            return {
                "success": False,
                "message": "Invalid action. Penalty applied.",
                "action": action,
                "state": self.get_state()
            }

        self.update_coffee_turns(action)
        self.process_events(action)
        self.apply_travel_effects(action)

        return {
            "success": True,
            "message": "Action processed successfully",
            "action": action,
            "state": self.get_state()
                }

    def apply_invalid_input_penalty(self):
        self.player.energy -= 5
        self.player.stress += 5
        self.player.turns_without_coffee += 1
        self.player.clamp_stats()

    def get_state(self):
        current_location = self.get_current_location()
        if current_location:
            current_location_name = current_location["name"]
        else:
            current_location_name = None
        return {
            "player": self.player.to_dict(),
            "location": current_location_name,
            "status": self.get_game_status(),
            "game_over": self.is_game_over()

        }

