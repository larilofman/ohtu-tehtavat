import datetime
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    nationality = "FIN"

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    print(f"Players from {nationality} {datetime.date.today().strftime('%d.%m.%Y')}:\n")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
