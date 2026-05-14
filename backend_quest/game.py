from player import Player
from locations import LOCATIONS
from constants import TRAVEL, REST, STUDY, FIND_COFFEE
from weather import get_weather, apply_weather_effects
from engine import GameEngine


def show_actions():
    print("\nWhat will you do?"
          "\n1. Travel"
          "\n2. Rest"
          "\n3. Study"
          "\n4. Find coffee")

def show_final_summary(engine):
    player = engine.player

    print("\n===== FINAL SUMMARY =====")
    print(f"Final status: {engine.get_game_status()}")
    print(f"\nCoffee: {player.coffee}")
    print(f"\nEnergy: {player.energy}")
    print(f"\nKnowledge: {player.knowledge}")
    print(f"\nMoney: {player.money}")
    print(f"\nStress: {player.stress}")
    print(f"\nTurns without coffee: {player.turns_without_coffee}")
    print(f"Final score: {player.calculate_score()}")
    print("=============================")
def show_current_location(engine):
    location = engine.get_current_location()
    if location is None:
        return
    print(f"Your current location is {location["name"]}. {location["description"]}.")

def handle_player_choice(choice):
    if choice == "1":
        return TRAVEL
    elif choice == "2":
        return REST
    elif choice == "3":
        return STUDY
    elif choice == "4":
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

def play_game(engine):
    while True:
        if engine.is_game_over():
            show_final_summary(engine)
            break
        show_current_location(engine)
        show_actions()

        choice = input("Enter your choice:")
        action = handle_player_choice(choice)

        if action is None:
            print("\nInvalid choice. You wasted your time and got more stressed.")
            engine.apply_invalid_input_penalty()
            show_stats(engine.player)
            continue

        turn_result = engine.play_turn(action)
        if not turn_result:
            print("\nAction could not be processed.")
            show_stats(engine.player)
            continue

        show_stats(engine.player)

def show_stats(player):
    print("\n--- CURRENT STATS ---")
    print(f"\nCoffee: {player.coffee}"
          f"\nEnergy: {player.energy}"
          f"\nKnowledge: {player.knowledge}"
          f"\nMoney: {player.money}"
          f"\nStress: {player.stress}"
          f"\nTurns without coffee: {player.turns_without_coffee}")


if __name__ == "__main__":
    player = Player()
    engine = GameEngine(player, LOCATIONS, len(LOCATIONS))
    play_game(engine)

