import tkinter as tk
from PIL import Image, ImageTk


class TransparentGIFWindow(tk.Toplevel):
    def __init__(self, master, gif_path):
        super().__init__(master)
        # self.overrideredirect(True)
        self.attributes('-transparentcolor', 'white')  # 设置白色为透明
        self.gif = Image.open(gif_path)
        self.width, self.height = self.gif.size
        self.canvas = tk.Canvas(self, width=540,
                                height=540, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
\
        self.data = self.gif
        new_data = []
        for item in data:
            if item[3] == 0:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        self.gif.putdata(new_data)

        self.load_frames()

    def load_frames(self):
        self.frames = []
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(
                    self.gif.copy().convert('RGBA')))
                self.gif.seek(self.gif.tell() + 1)
        except EOFError:
            pass
        self.current_frame = 0
        self.canvas.delete('all')
        self.show_frame()

    def show_frame(self):
        self.canvas.create_image(
            0, 0, image=self.frames[self.current_frame], anchor='nw')
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        canvas.config(bg='systemTransparent')
        self.after(50, self.show_frame)  # 50ms 后更新下一帧


root = tk.Tk()
gif_window = TransparentGIFWindow(root, 'cat.gif')
# gif_window.pack()
root.mainloop()
