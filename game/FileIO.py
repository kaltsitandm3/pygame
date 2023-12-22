class FileIO:
    def __init__(self, filename):
        self.filename = filename

    def read_settings(self):
        settings = {}
        try:
            with open(self.color.txt, "r") as file:
                lines = file.readlines()
                settings["peg_count"] = int(lines[0].strip())  # 彩钉数量
                settings["colors"] = [color.strip() for color in lines[1:]]  # 彩钉颜色选项
        except FileNotFoundError:
            print(f"文件 '{self.filename}' 未找到。")

        return settings
