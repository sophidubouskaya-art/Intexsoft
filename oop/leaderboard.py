from .player import Player


class Leaderboard:
    # таблица рейтинга игроков

    def __init__(self):
        self.players = []

    def add_or_update(self, nick, score):
        for p in self.players:
            if p.nick == nick:
                p.score = score
                return
        self.players.append(Player(nick, score))

    def find_by_nick(self, nick):
        for p in self.players:
            if p.nick == nick:
                return p
        return None

    def top_k(self, k):
        # сортируем по убыванию очков
        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)
        return sorted_players[:k]

    def average_score(self):
        if not self.players:
            return 0
        total = sum(p.score for p in self.players)
        return total / len(self.players)

    def players_above(self, threshold):
        return [p for p in self.players if p.score >= threshold]

    def print_all(self):
        if not self.players:
            print("(пусто)")
            return
        for p in self.players:
            print(f"  {p}")
