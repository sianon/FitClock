import tkinter as tk
from tkinter import ttk


class VideoPlayer(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        # 创建窗口
        # root = tk.Tk()
        self.geometry("400x100")
        # self.master = root
        # self.master.geometry("400x100")
        self.create_widgets()
        # self.pack()
        # self.master.mainloop()

    def create_widgets(self):
        # 创建播放/暂停按钮
        self.play_button = ttk.Button(self, text="Play")
        self.play_button.pack(side="left")

        # 创建进度条
        self.progressbar = ttk.Progressbar(
            self, orient="horizontal", length=200, mode="determinate")
        self.progressbar.pack(side="left", padx=10)

        # 创建音量控制条
        self.volume_scale = ttk.Scale(
            self, from_=0, to=100, orient="horizontal", length=100)
        self.volume_scale.pack(side="left", padx=10)


# root = tk.Tk()
# root.geometry("400x100")

# # 创建播放器
# player = VideoPlayer(master=root)

# 运行窗口
