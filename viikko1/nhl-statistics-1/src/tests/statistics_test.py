import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko")
    
    def test_search_does_not_find_non_existant_player(self):
        player = self.statistics.search("Pörrö")
        self.assertIsNone(player)

    def test_players_of_team_are_returned(self):
        players = self.statistics.team("EDM")
        self.assertEqual(
            list(map(lambda x: x.name, players)), 
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_top_scorers_are_returned(self):
        topScorers = self.statistics.top_scorers(3)
        self.assertEqual(
            list(map(lambda x: x.name, topScorers)), 
            ["Gretzky", "Lemieux", "Yzerman" ]
        )