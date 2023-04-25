import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tktimepicker import timepicker
from datetime import datetime
from player import VideoPlayer


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("hello")
        root = self.master
        root.configure(padx=20, pady=20)
        root.geometry("400x171")
        self.master.geometry('+{}+{}'.format(200, 200))
        root.overrideredirect(True)
        self.lab_act = ttk.Label(root, text="健康动作:")
        self.lab_act.grid(column=0, row=0, pady=6)

        self.comb_act = ttk.Combobox(root)
        self.comb_act['values'] = ("起来走走", '喝杯咖啡')
        self.comb_act.current(0)
        self.comb_act.config(width=10)
        self.comb_act.grid(column=1, row=0, pady=6)

        self.label2 = ttk.Label(root, text='指定时间:')
        self.label2.grid(column=0, row=1, pady=6)
        self.ledit = ttk.Entry(root)
        self.ledit.config(width=10)
        self.ledit.grid(column=1, row=1, pady=6)

        self.btn_date = ttk.Button(root, text="日期选择")
        self.btn_date.bind('<1>', self.ShowCalendar)
        self.btn_date.grid(column=2, row=1, pady=6)

        self.btn_time = ttk.Button(root, text="时分秒的选择")
        self.btn_time.bind('<1>', self.ShowTime)
        self.btn_time.grid(column=3, row=1, pady=6)

        self.lab_repeat = ttk.Label(root, text="是否重复:")
        self.lab_repeat.grid(column=0, row=2, pady=6)
        self.check_btn = ttk.Checkbutton(root, text='checkbox')
        self.check_btn.grid(column=1, row=2, pady=6)

        self.comb_repeat = ttk.Combobox(root)
        self.comb_repeat['values'] = ("每天", '工作日', '周末', '自定义')
        self.comb_repeat.current(0)
        self.comb_repeat.config(width=10)
        self.comb_repeat.grid(column=2, row=2, pady=6)

        self.btn_do_plan = ttk.Button(root, text="执行计划")
        self.btn_do_plan.bind('<1>', self.DoPlan)
        self.btn_do_plan.grid(column=0, row=3, pady=6, columnspan=4)
        self.master.columnconfigure(3, weight=1)

        self.x = 0
        self.y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.is_dragging_window = False

        self.master.bind("<ButtonPress-1>", self.start_drag_window)
        self.master.bind("<B1-Motion>", self.drag_window)
        self.master.bind("<ButtonRelease-1>", self.stop_drag_window)

    def run(self):
        self.master.mainloop()

    def DoPlan(self, event):
        pl = VideoPlayer()

    def ShowTime(self, event):
        top = tk.Toplevel(self.master)
        analog_win = timepicker.AnalogPicker(top)

        # 设置默认值
        now = datetime.now().time()
        analog_win.setHours(now.hour)
        analog_win.setMinutes(now.minute)
        # self.timepicker.selection_get()
        analog_win.pack()

    def ShowCalendar(self, event):
        top = tk.Toplevel(self.master)
        cal = DateEntry(top)
        cal.pack(padx=10, pady=10)

        def SelectDate():
            self.btn.configure(
                text=cal.selection_get().strftime('%Y-%m-%d'))
            top.destroy()
        # ttk.Button(top, text='Select', command=SelectDate()).pack(pady=5)
        top.grab_set()

        # top.mainloop()

    def start_drag_window(self, event):
        """开始拖动窗口"""
        self.x = self.master.winfo_x()
        self.y = self.master.winfo_y()
        self.mouse_x = event.x
        self.mouse_y = event.y
        self.is_dragging_window = True

    def drag_window(self, event):
        """拖动窗口"""
        if self.is_dragging_window:
            delta_x = event.x - self.mouse_x
            delta_y = event.y - self.mouse_y
            self.master.geometry(f"+{self.x + delta_x}+{self.y + delta_y}")

    def stop_drag_window(self, event):
        """停止拖动窗口"""
        self.is_dragging_window = False


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    app.run()
