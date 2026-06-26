import os
import json
from backend_quest.player import Player
SAVE_FILE = "save_data.json"

def save_player(player_state):
    with open(SAVE_FILE, "w") as file:
        json.dump(player_state, file, indent=4)
def load_player_state():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as file:
        return json.load(file)


