class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        names = set()
        added_players = []
        for player in args:
            if player.name in names:
                raise Exception(f"Name {player.name} is already used!")
            names.add(player.name)
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return

        supply_type = sustenance_type.lower() + "s"
        if not getattr(self, supply_type):
            raise Exception(f"There are no {supply_type.lower()} supplies left!")

        supply = getattr(self, supply_type).pop()
        player.stamina = min(player.stamina + supply.energy, 100)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next((p for p in self.players if p.name == first_player_name), None)
        second_player = next((p for p in self.players if p.name == second_player_name), None)
        if not first_player or not second_player:
            return

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\nPlayer {second_player.name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        first_attack = first_player.stamina // 2
        second_attack = second_player.stamina // 2

        first_player.stamina = max(first_player.stamina - second_attack, 0)
        second_player.stamina = max(second_player.stamina - first_attack, 0)

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            player.stamina = max(player.stamina, 0)

        self.sustain_all("Food")
        self.sustain_all("Drink")

    def sustain_all(self, sustenance_type: str):
        players_to_sustain = [player for player in self.players if player.need_sustenance]
        if sustenance_type not in ["Food", "Drink"] or not players_to_sustain:
            return

        supply_type = sustenance_type.lower() + "s"
        if not getattr(self, supply_type):
            return

        for player in players_to_sustain:
            supply = getattr(self, supply_type).pop()
            player.stamina = min(player.stamina + supply.energy, 100)

    def __str__(self):
        player_info = "\n".join(str(player) for player in self.players)
        supply_info = "\n".join(supply.details() for supply in self.supplies)
        return f"{player_info}\n{supply_info}"
