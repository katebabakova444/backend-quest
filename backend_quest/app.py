from flask import Flask, jsonify, request
from backend_quest.engine import GameEngine
from backend_quest.player import Player
from backend_quest.locations import LOCATIONS

app = Flask(__name__)
player = Player()
game = GameEngine(player, LOCATIONS, len(LOCATIONS))

@app.get("/state")
def get_state():
    return jsonify(game.player.to_dict()), 200

@app.route("/reset", methods=["POST"])
def reset():
    global player
    global game
    player = Player()
    game = GameEngine(player, LOCATIONS, len(LOCATIONS))

    return jsonify({"message": "Game reset",
                    "state": game.player.to_dict()
                    }), 200
@app.route("/action", methods=["POST"])
def post_action():
    data = request.get_json()
    if not data:
        return jsonify({"error": "request body is required"}), 400
    action = data.get("action")
    if not action:
        return jsonify({"error": "action is required"}), 400
    game.process_action(action)
    return jsonify({"action": action,
                    "state": game.player.to_dict()}), 200


if __name__ == "__main__":
    app.run(debug=True, port=6000)

