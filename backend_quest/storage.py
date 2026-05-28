import os
import json
from player import Player
SAVE_FILE = "save_data.json"

def save_player(player_state):
    with open(SAVE_FILE, "w") as file:
        json.dump(player_state, file, indent=4)
def load_player_state():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as file:
        return json.load(file)

if __name__ == "__main__":
    test_player = {
        "location": "Ukraine",
        "energy": 80,
        "coffee": 2,
        "knowledge": 10,
        "money": 50,
        "stress": 20,
        "days_without_coffee": 2
    }
    save_player(test_player)
    loaded_player = load_player_state()
    print(loaded_player)

