def get_weather(location_name):
    if location_name == "Istanbul":
        return "rainy"
    elif location_name == "Chicago":
        return "cold"
    elif location_name == "Denver":
        return "foggy"
    elif location_name == "Las Vegas":
        return "hot"
    elif location_name == "Los Angeles":
        return "sunny"
    elif location_name == "Santa Cruz":
        return "stormy"
    elif location_name == "Palo Alto":
        return "sunny"
    elif location_name == "San Jose":
        return "hot"
    elif location_name == "San Francisco":
        return "foggy"
    else:
        return "sunny"
def apply_weather_effects(player, weather):
    weather_data = [{"name": "sunny", "effects": {"energy": 5, "stress": -5},
               "description": "Sunny weather gives you a small energy boost."},
               {"name": "rainy", "effects": {"energy": -5, "stress": 5},
               "description": "Rain makes everything slower and more annoying."},
               {"name": "cold", "effects": {"energy": -5, "coffee": -5},
               "description": "Cold weather makes coffee feel less optional"},
               {"name": "hot", "effects": {"energy": -10, "stress": 5},
                "description": "The heat drains your energy"},
               {"name": "foggy", "effects": {"knowledge": -5, "stress": 5},
                "description": "Fog makes it harder to focus"},
               {"name": "stormy", "effects": {"energy": -15, "stress": 10},
                "description": "A storm hits and makes the road harder."}]

    for i in weather_data:
        if i["name"] == weather:
            for key, value in i["effects"].items():
              setattr(player, key, getattr(player, key) + value)
            print("\n--- WEATHER ---")
            print(f"Weather: {i["name"]}")
            print(i["description"])
            player.clamp_stats()
            return
    print("Unknown weather")