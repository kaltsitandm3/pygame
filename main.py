from fuckgame import Game, Round

if __name__ == "__main__":
    g = Game()
    r = Round()
    color_count, colors = g.load_settings("game_settings.json")

    print(f"color_count: {color_count}\ncolors: {colors}")

    while True:
        try:
            r.max_rounds = int(input("Please enter the number of rounds you would to play >>> "))

            if r.max_rounds > 0:
                break

        except Exception:
            pass

    random_colors = r.get_random_colors(color_count, colors)

    for round in range(r.max_rounds):
        pass
