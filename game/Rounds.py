import ColorGrid


# Rounds 类 - 游戏轮次类
class Rounds:
    def __init__(self, max_pegs_per_round, max_rounds):
        self.maxPegsPerRound = max_pegs_per_round  # 每轮最大彩钉数
        self.maxRounds = max_rounds  # 最大游戏轮次
        self.allColorGrid = ColorGrid()  # 所有可用彩钉颜色的 ColorGrid 对象
        self.computerColorGrid = ColorGrid()  # 计算机生成的彩钉序列的 ColorGrid 对象
        self.roundGuesses = []  # 保存玩家每轮的猜测记录列表
