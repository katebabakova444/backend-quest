def apply_effects(player, effects):
    for key, value in effects.items():
        setattr(player, key, getattr(player, key) + value)
        if value > 0:
            print(f"{key.replace("_", " ").title()} + {value}")
        elif value < 0:
            print(f"{key.replace("_", " ").title()} {value}")
    player.clamp_stats()
