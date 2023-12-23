import json
from typing import Tuple, Union


class Game:
    def __init__(self) -> None:
        self.color_count = None
        self.colors = None

    def load_settings(self, file_path: str) -> Tuple[Union[int, list], Union[int, list]]:
        if not file_path.endswith(".json"):
            raise Exception()

        with open(file_path, "r") as file:
            colors = json.load(file)

        self.color_count = colors.get("color_count", 0)
        self.colors = colors.get("colors", [])

        if not self.color_count or not self.colors:
            raise Exception()

        if self.color_count > len(self.colors):
            raise Exception()

        return self.color_count, self.colors
