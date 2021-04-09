from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        getattr(self, player_name).add_score()

    def leading_player(self):
        leading = self.player1 if self.player1.score > self.player2.score else self.player2 
        return leading
           
    def get_score_representation(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def advantage(self):
        return f"Advantage {self.leading_player().name}"

    def won(self):
        return f"Win for {self.leading_player().name}"

    def tie(self):
        tied_score = self.player1.score
        if tied_score > 3:
            return "Deuce"   
        else:
            return f"{self.get_score_representation(tied_score)}-All"
    
    def running(self):
        return f"{self.get_score_representation(self.player1.score)}-{self.get_score_representation(self.player2.score)}"

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self.tie()
        elif self.leading_player().score >= 4:
            difference = abs(self.player1.score - self.player2.score)
            if difference > 1:
                return self.won()
            else:
                return self.advantage()
        else:
            return self.running()
            

