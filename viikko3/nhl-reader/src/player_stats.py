from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players_of_nationality = list(filter(lambda x: x.nationality == nationality, all_players))
        players_sorted = []

        for player in sorted(players_of_nationality, key=lambda x: (x.score), reverse=True):
            players_sorted.append(player)
        
        return players_sorted
