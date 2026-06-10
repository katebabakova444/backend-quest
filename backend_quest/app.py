"""
Future Flask entry point.
Planned endpoints:
- GET /state
- POST /action
- POST /reset

The Flask API will use GameEngine as the core game logic layer.
"""

from flask import Flask, jsonify, request
from engine import GameEngine
from player import Player
from locations import LOCATIONS

app = Flask(__name__)
player = Player()
game = GameEngine(player, LOCATIONS, len(LOCATIONS))

@app.get("/state")
def get_state():
    return jsonify(game.player.to_dict()), 200



if __name__ == "__main__":
    app.run(debug=True)

