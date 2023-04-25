import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # 设置窗口形状和透明度
        self.overrideredirect(True)
        self.attributes('-transparentcolor', 'white')  # 设置白色为透明

        # 加载GIF动画
        self.gif = Image.open('cat-unscreen.gif')
        # self.frames = [ImageTk.PhotoImage(self.gif.copy().convert('RGBA'))
        #                for img in ImageSequence.Iterator(self.gif)]
        self.frames = []

        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(
                    self.gif.copy().convert('RGBA')))
                self.gif.seek(self.gif.tell() + 1)
        except EOFError:
            pass

        self.current_frame = 0

        # 创建Canvas并绘制动画
        self.canvas = tk.Canvas(
            self, width=640, height=640, highlightthickness=0)
        self.canvas.delete('all')
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.frames[0], anchor='nw')

        # 开始播放动画
        self.PlayAnimation(0)

    def PlayAnimation(self, frame_idx):
        self.canvas.itemconfig(1, image=self.frames[frame_idx])
        self.after(45, self.PlayAnimation, (frame_idx+1) % len(self.frames))


if __name__ == '__main__':
    app = MyWindow()
    app.mainloop()
