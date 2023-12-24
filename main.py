from fuckgame import Game

if __name__ == "__main__":
    g = Game()
    colors, num_pegs = g.load("settings.json")

    print(f"所有颜色: {colors}\n彩钉数量: {num_pegs}", end="\n\n")

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

    for i, round in enumerate(range(g.num_rounds)):
        guesses = []

        print(f"\n第{i + 1}轮")

        for j, peg in enumerate(range(num_pegs)):
            while True:
                guess = input(f"请猜测第{j + 1}个颜色: ")

                if guess.lower() not in [color.lower() for color in colors]:
                    print("颜色不存在！")
                    continue

                guesses.append(guess)
                break

        score, correct_idx = g.check(guesses)

        g.all_guesses[f"round[{i + 1}]"] = guesses

        if len(correct_idx) == num_pegs:
            for _ in range(g.num_rounds - i - 1):
                for j in range(1, num_pegs + 1):
                    score += j

            print(f"\n全部猜对了！\n最终分数: {score}")
            break
        elif i + 1 == g.num_rounds:
            print(f"\n猜对了第{correct_idx}个！\n最终分数: {score}")
        else:
            print(f"\n猜对了第{correct_idx}个！\n当前分数: {score}")

    print(f"\n正确颜色为: {random_colors}")

    print("\n猜测记录: ")

    for key, value in g.all_guesses.items():
        print(f"{key}: {value}")
