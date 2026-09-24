class Player:
    #один игрок: ник и очки

    def __init__(self, nick, score):
        self.nick = nick
        self.score = score

    def __repr__(self):
        return f"{self.nick}: {self.score}"


class Leaderboard:

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


if __name__ == "__main__":
    board = Leaderboard()

    board.add_or_update("Misha", 100)
    board.add_or_update("Bob", 250)
    board.add_or_update("Dasha", 180)
    board.add_or_update("David", 320)
    board.add_or_update("Sofiya", 650)

    print("Все игроки:")
    board.print_all()

    board.add_or_update("Bob", 400)
    print("\nПосле обновления Bob:")
    board.print_all()

    found = board.find_by_nick("Sofiya")
    print(f"\nНашли Sofiya: {found}")

    print("\nТоп-3:")
    for p in board.top_k(3):
        print(f"  {p}")

    print(f"\nСреднее число очков: {board.average_score():.2f}")

    print("\nИгроки с очками >= 200:")
    for p in board.players_above(200):
        print(f"  {p}")