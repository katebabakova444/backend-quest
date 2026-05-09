from player import Player
from locations import LOCATIONS
from actions import travel, rest, study, find_coffee
from events import EVENTS, trigger_events
from constants import TRAVEL, REST, STUDY, FIND_COFFEE
from weather import get_weather, apply_weather_effects

def show_actions():
    print("\nWhat will you do?"
          "\n1. Travel"
          "\n2. Rest"
          "\n3. Study"
          "\n4. Find coffee")

def show_final_summary(player, total_locations):
    print("\n===== FINAL SUMMARY =====")
    print(f"Final status: {player.get_final_status(total_locations)}")
    print(f"\nCoffee: {player.coffee}")
    print(f"\nEnergy: {player.energy}")
    print(f"\nKnowledge: {player.knowledge}")
    print(f"\nMoney: {player.money}")
    print(f"\nStress: {player.stress}")
    print(f"\nTurns without coffee: {player.turns_without_coffee}")
    print(f"Final score: {player.calculate_score()}")
    print("=============================")

def apply_location_effects(player, location):
    for key, value in location["effects"].items():
        setattr(player, key, getattr(player, key) + value)
    player.clamp_stats()

def process_location(player, action, location):
        location_name = location["name"]
        trigger_events(action, location_name, player)

def update_coffee_turns(player, action):
    if action != FIND_COFFEE:
        player.turns_without_coffee += 1

def handle_player_choice(player, choice):
    if choice == "1":
        travel(player)
        return TRAVEL
    elif choice == "2":
        rest(player)
        return REST
    elif choice == "3":
        study(player)
        return STUDY
    elif choice == "4":
        find_coffee(player)
        return FIND_COFFEE
    else:
        return None

def check_game_end(player, total_locations):
    if not player.is_alive():
        show_final_summary(player, total_locations)
        return True
    if player.reached_final_destination(total_locations):
        if player.has_won(total_locations):
            print("\nYou reached the final location prepared. You won.")
        else:
            print("\nYou reached the final location, but you are not interview-ready yet.")
        show_final_summary(player, total_locations)
        return True
    return False

def play_game(player, total_locations):
    while True:
        if check_game_end(player, total_locations):
            break
        location = LOCATIONS[player.current_location_index]
        print(f"Your current location is {location["name"]}. {location["description"]}.")
        show_actions()

        choice = input("Enter your choice:")
        action = handle_player_choice(player, choice)

        if action is None:
            apply_invalid_input_penalty(player)
            show_stats(player)
            continue

        update_coffee_turns(player, action)
        current_location = LOCATIONS[player.current_location_index]
        process_location(player, action, current_location)

        if action == TRAVEL:
            apply_location_effects(player, current_location)
            weather = get_weather(current_location["name"])
            apply_weather_effects(player, weather)
        show_stats(player)

def show_stats(player):
    print("\n--- CURRENT STATS ---")
    print(f"\nCoffee: {player.coffee}"
          f"\nEnergy: {player.energy}"
          f"\nKnowledge: {player.knowledge}"
          f"\nMoney: {player.money}"
          f"\nStress: {player.stress}"
          f"\nTurns without coffee: {player.turns_without_coffee}")

def apply_invalid_input_penalty(player):
    print("Invalid choice. You wasted your time and got more stressed.")
    player.energy -= 5
    player.stress += 5
    player.turns_without_coffee += 1
    player.clamp_stats()


if __name__ == "__main__":
    total_locations = len(LOCATIONS)
    player = Player()
    play_game(player, total_locations)

