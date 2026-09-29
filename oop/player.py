class Player:
    # один игрок: ник и очки

    def __init__(self, nick, score):
        self.nick = nick
        self.score = score

    def __repr__(self):
        return f"{self.nick}: {self.score}"
