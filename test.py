from fuckgame import Game

if __name__ == "__main__":
    g = Game()

    colors, num_pegs = g.load("settings.json")
    print(f"所有颜色: {colors}\n彩钉数量: {num_pegs}")

    while True:
        try:
            g.num_rounds = int(input("请输入猜测轮数: "))

            if not g.num_rounds > 0:
                continue

            break
        except Exception:
            pass

    random_colors = g.get_random_colors()
    print(random_colors)
    g.guesses = {}
    g.score = 0

    for i, round in enumerate(range(g.num_rounds)):
        guesses = []

        print(f"第{i + 1}轮")

        for j, peg in enumerate(range(g.num_pegs)):
            while True:
                guess = input(f"请猜测第{j + 1}个颜色: ")

                if guess.lower() not in [color.lower() for color in g.colors]:
                    continue

                guesses.append(guess)
                break

        score, correct_idx = g.check(guesses)
        print(f"猜对了第{correct_idx}个\n当前总分: {g.score}")

        g.guesses[f"round[{i + 1}]"] = guesses

    print(random_colors)
