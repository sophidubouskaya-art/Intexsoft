def add_or_update(players, nick, score):
    for p in players:
        if p["nick"] == nick:
            p["score"] = score
            return
    players.append({"nick": nick, "score": score}) 


def find_by_nick(players, nick):
    for p in players:
        if p["nick"] == nick:
            return p
    return None


def top_k(players, k):
    # сортируем по убыванию очков
    sorted_players = sorted(players, key=lambda p: p["score"], reverse=True)
    return sorted_players[:k]


def average_score(players):
    if not players:
        return 0
    total = sum(p["score"] for p in players)
    return total / len(players)


def players_above(players, threshold):
    return [p for p in players if p["score"] >= threshold]


def print_players(players):
    if not players:
        print("(пусто)")
    for p in players:
        print(f"  {p['nick']}: {p['score']}")


if __name__ == "__main__":
    rating = []

    add_or_update(rating, "Misha", 100)
    add_or_update(rating, "Bob", 250)
    add_or_update(rating, "Dasha", 180)
    add_or_update(rating, "David", 320)
    add_or_update(rating, "Sofiya", 650)

    print("Все игроки:")
    print_players(rating)

    add_or_update(rating, "Bob", 400)
    print("\nПосле обновления Bob:")
    print_players(rating)

    found = find_by_nick(rating, "Sofiya")
    print(f"\nНашли Sofiya: {found}")

    print("\nТоп-3:")
    print_players(top_k(rating, 3))

    print(f"\nСреднее число очков: {average_score(rating):.2f}")


    print("\nИгроки с очками >= 200:")
    print_players(players_above(rating, 200))