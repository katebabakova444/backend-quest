class Player:
    def __init__(self):
        self.name = "Kateryna"
        self.energy = 100
        self.coffee = 50
        self.knowledge = 10
        self.money = 3000
        self.stress = 0
        self.turns_without_coffee = 0
        self.current_location_index = 0

    def show_stats(self):
        print(f"Energy: {self.energy}/100")
        print(f"Coffee: {self.coffee}")
        print(f"Knowledge: {self.knowledge}/100")
        print(f"Money: {self.money}")
        print(f"Stress: {self.stress}/100")
    def is_alive(self):
        if self.energy <= 0:
            print("\nYou burned out. Game over.")
            return False
        if self.stress >= 100:
            print("\nTotal burnout. Game over.")
            return False
        if self.money <= 0:
            print("\nYou ran out of money. Game over.")
            return False
        if self.turns_without_coffee >= 4:
            print("\nNo coffee for 4 turns. You cannot function. Game over.")
            return False
        return True

    def clamp_stats(self):
        if self.money < 0:
            self.money = 0
        if self.energy < 0:
            self.energy = 0
        if self.stress < 0:
            self.stress = 0
        if self.knowledge < 0:
            self.knowledge = 0
        if self.coffee < 0:
            self.coffee = 0

    def has_won(self, total_locations):
        return self.current_location_index >= total_locations - 1 and self.knowledge >= 100

    def reached_final_destination(self, total_locations):
        return self.current_location_index >= total_locations - 1

    def calculate_score(self):
        score = (
            self.knowledge * 3
            + self.energy
            + self.coffee
            + self.money // 10
            - self.stress * 2
        )
        if score < 0:
            return 0
        return score
    def get_final_status(self, total_locations):
        if self.energy <= 0:
            return "Burned Out"
        if self.money <= 0 :
            return "Broke But Learning"
        if self.stress >= 200:
            return "Stress Collapse"
        if self.has_won(total_locations):
            return "Interview Ready"
        if self.reached_final_destination(total_locations):
            return "Reached Final Location, But Not Ready"
        if self.turns_without_coffee >= 4:
            return "Coffee Crush"
        return "Still On Trail"

    def to_dict(self):
        return {
            "energy": self.energy,
            "coffee": self.coffee,
            "knowledge": self.knowledge,
            "money": self.money,
            "stress": self.stress,
            "turns_without_coffee": self.turns_without_coffee,
            "current_location_index": self.current_location_index
        }
    def load_from_dict(self, data):
        self.energy = data["energy"]
        self.coffee = data["coffee"]
        self.knowledge = data["knowledge"]
        self.money = data["money"]
        self.stress = data["stress"]
        self.turns_without_coffee = data["turns_without_coffee"]
        self.current_location_index = data["current_location_index"]





