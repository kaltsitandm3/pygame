import json
import random
from typing import List, Tuple


class Game:
    def __init__(self) -> None:
        self.num_rounds: int = None
        self.num_pegs: int = None
        self.score: int = 0

        self.colors: List[str] = None
        self.random_colors: List[str] = None

        self.all_guesses: dict = {}

    def load(self, file_path: str) -> Tuple[List[str], int]:
        with open(file_path, "r") as file:
            settings = json.load(file)

        if settings["num_pegs"] > len(settings["colors"]):
            raise Exception()

        self.colors = settings["colors"]
        self.num_pegs = settings["num_pegs"]

        return self.colors, self.num_pegs

    def get_random_colors(self):
        self.random_colors = random.choices(self.colors, k=self.num_pegs)

        return self.random_colors

    def check(self, guesses: List[str]):
        correct_idx = []

        for i, (guess, target) in enumerate(zip(guesses, self.random_colors)):
            if guess.lower() == target.lower():
                self.score += len(self.random_colors)
                correct_idx.append(i + 1)

        return self.score, correct_idx
