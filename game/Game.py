import FileIO
import Input
import Rounds
import Validation


# Game 类 - 游戏类
class Game:
    def __init__(self):
        self.rounds = Rounds(4, 5)  # 用 4 个彩钉每轮，总共 5 轮初始化游戏
        self.file_io = FileIO()
        self.input_handler = Input()
        self.validation = Validation()

    def welcome_screen(self):
        # 显示欢迎界面并从 color.txt 读取设置使用 FileIO
        pass

    def start_game(self):
        # 初始化游戏设置并开始游戏循环
        pass

    def game_loop(self):
        # 主游戏循环，处理轮次、玩家猜测以及检查正确顺序
        pass

    def end_game(self):
        # 显示最终得分、正确的顺序，并使用 FileIO 将结果写入 outcome.txt
        pass
