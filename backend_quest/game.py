from backend_quest.storage import load_player_state
from backend_quest.player import Player
from backend_quest.locations import LOCATIONS
from backend_quest.constants import TRAVEL, REST, STUDY, FIND_COFFEE, SAVE_AND_QUIT
from backend_quest.engine import GameEngine
from backend_quest.storage import save_player, load_player_state

def show_actions():
    print("\nWhat will you do?"
          "\n1. Travel"
          "\n2. Rest"
          "\n3. Study"
          "\n4. Find coffee"
          "\n0. Quit and save")

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
    elif choice == "0":
        return SAVE_AND_QUIT
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
        save_player(engine.player.to_dict())

        if action == SAVE_AND_QUIT:
            save_player(engine.player.to_dict())
            print("Game saved. See you next time.")
            break

        if action is None:
            turn_result = engine.play_turn(None)
            print(f"\n{turn_result["message"]}")
            engine.apply_invalid_input_penalty()
            show_stats(engine.player)
            continue

        turn_result = engine.play_turn(action)
        if not turn_result["success"]:
            print(f"\n{turn_result["message"]}")
            show_stats(engine.player)
            continue
        save_player(engine.player.to_dict())
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
    saved_state = load_player_state()
    player = Player()
    if saved_state is not None:
        player.load_from_dict(saved_state)
        print("Saved game loaded.")
    else:
        print("New game started.")
    engine = GameEngine(player, LOCATIONS, len(LOCATIONS))
    play_game(engine)
