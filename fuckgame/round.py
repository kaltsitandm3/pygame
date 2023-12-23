import random


class Round:
    def __init__(self) -> None:
        self.max_rounds = None
        self.random_colors = None

    def get_random_colors(self, color_count: int, colors: list) -> list:
        self.random_colors = random.choices(colors, k=color_count)

        return self.random_colors
