# ColorGrid 类 - 彩钉序列类
class ColorGrid:
    def __init__(self):
        self.pegs = []  # 彩钉列表
        self.noOfPegs = 0  # 彩钉数量

    def add_peg(self, peg):
        self.pegs.append(peg)  # 添加彩钉
        self.noOfPegs += 1  # 彩钉数量增加
