import tkinter as tk
import datetime
import tkinter.ttk as ttk


# カレンダーを作成するフレームクラス
class mycalendar(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        # 初期化メソッド
        tk.Frame.__init__(self, master, cnf, **kw)
        # 現在の年月日を取得
        now = datetime.datetime.now()
        # 現在の年月日を属性に追加
        self.year = now.year
        self.month = now.month
        self.hinichi = now.day

        # frame_top部分の作成
        frame_top = tk.Frame(self)
        frame_top.pack(pady=100)
        self.previous_month = tk.Label(frame_top, text="<", font=("", 10))
        self.previous_month.bind("<1>", self.change_month)
        self.previous_month.pack(side="left", padx=10)
        self.label1 = tk.Label(frame_top, text="過去を見るな", font=("", 10))
        self.label1.bind("<1>", self.change_month)
        self.label1.pack(side="left", padx=10)
        self.current_year = tk.Label(frame_top, text=self.year, font=("", 10))
        self.current_year.pack(side="left")
        self.current_month = tk.Label(frame_top, text=self.month, font=("", 100))
        self.current_month.pack(side="left")
        self.label2 = tk.Label(frame_top, text="未来を見ろ", font=("", 20))
        self.label2.bind("<1>", self.change_month)
        self.label2.pack(side="left", padx=10)
        self.next_month = tk.Label(frame_top, text=">", font=("", 50))
        self.next_month.bind("<1>", self.change_month)
        self.next_month.pack(side="left", padx=10)

        # frame_week部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        button_mon = d_button(frame_week, text="Mon")
        button_mon.grid(column=0, row=0)
        button_tue = d_button(frame_week, text="Tue")
        button_tue.grid(column=1, row=0)
        button_wed = d_button(frame_week, text="Wed")
        button_wed.grid(column=2, row=0)
        button_thu = d_button(frame_week, text="Thu")
        button_thu.grid(column=3, row=0)
        button_fri = d_button(frame_week, text="Fri")
        button_fri.grid(column=4, row=0)
        button_sta = d_button(frame_week, text="Sat", fg="blue")
        button_sta.grid(column=5, row=0)
        button_san = d_button(frame_week, text="San", fg="red")
        button_san.grid(column=6, row=0)

        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year, self.month)

    def create_calendar(self, year, month):
        "指定した年(year),月(month)のカレンダーウィジェットを作成する"

        # ボタンがある場合には削除する（初期化）
        try:
            for key, item in self.day.items():
                item.destroy()
        except:
            pass

        # calendarモジュールのインスタンスを作成
        import calendar
        import datetime
        now = datetime.datetime.now()
        cal = calendar.Calendar()
        # 指定した年月のカレンダーをリストで返す
        days = cal.monthdayscalendar(year, month)

        # 日付ボタンを格納する変数をdict型で作成
        self.day = {}
        # for文を用いて、日付ボタンを生成
        for i in range(0, 42):
            c = i - (7 * int(i / 7))
            r = int(i / 7)
            try:
                # 過去のカレンダーと０の部分以外のボタンを作成
                if self.month == now.month and self.year == now.year:
                    if days[r][c] >= self.hinichi and days[r][c] != 0:
                        self.day[i] = d_button(self.frame_calendar, text=days[r][c], command=btn_callback)
                        self.day[i].grid(column=c, row=r)
                else:
                    if days[r][c] != 0 and (self.month > now.month or self.year > now.year):
                        self.day[i] = d_button(self.frame_calendar, text=days[r][c], command=btn_callback)
                        self.day[i].grid(column=c, row=r)


            except:
                """
                月によっては、i=41まで日付がないため、日付がないiのエラー回避が必要
                """
                break

    def change_month(self, event):
        import datetime
        now = datetime.datetime.now()

        # 押されたラベルを判定し、過去のものは非表示に去るように設定
        if self.year == now.year:
            if event.widget["text"] == "<" or event.widget["text"] == "過去を見るな":
                if self.month < now.month + 1:
                    self.month -= 1
                    self.hinichi = 100
                else:
                    self.month -= 1

            else:
                if self.month >= now.month - 1:
                    self.month += 1
                    self.hinichi = now.day
                else:
                    self.month += 1
                    self.hinichi = 100
        else:
            if event.widget["text"] == "<" or event.widget["text"] == "過去を見るな":
                self.month -= 1
            else:
                self.month += 1

        # 月が0、13になったときの処理
        if self.month == 0:
            self.year -= 1
            self.month = 12
        elif self.month == 13:
            self.year += 1
            self.month = 1
        # frame_topにある年と月のラベルを変更する
        self.current_year["text"] = self.year
        self.current_month["text"] = self.month
        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year, self.month)


# デフォルトのボタンクラス
class d_button(tk.Button):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Button.__init__(self, master, cnf, **kw)
        self.configure(font=("", 14), height=2, width=4, relief="flat")


def btn_callback():
    root2 = tk.Toplevel()
    root2.title(u"schedule")
    root2.geometry("500x300")
    root2.grab_set()
    # paramdialog = tk.StringVar()
    Static1 = tk.Label(root2, text=u"予定")
    Static1.pack(side="left",pady=50)
    # 予定を書き込む
    schedule1 = tk.Entry(root2, textvariable=tk.StringVar(), text=tk.StringVar())
    schedule1.pack(side="left")
    Static1 = tk.Label(root2, text=u"何時から何時まで？")
    Static1.pack(side="top")
    schedule2 = tk.Entry(root2, width=3, textvariable=tk.StringVar())
    schedule2.pack(side="top",padx=1)
    Static2 = tk.Label(root2, text=u":")
    Static2.pack(side="top",padx=1)
    schedule3 = tk.Entry(root2, width=3, textvariable=tk.StringVar())
    schedule3.pack()
    Static3 = tk.Label(root2, text=u"~")
    Static3.pack(side="top",padx=1)
    schedule3 = tk.Entry(root2, width=3, textvariable=tk.StringVar())
    schedule3.pack(side="top",padx=1)
    Static4 = tk.Label(root2, text=u":")
    Static4.pack(side="top",padx=1)
    schedule3 = tk.Entry(root2, width=3, textvariable=tk.StringVar())
    schedule3.pack(side="top",padx=1)

    def input_schedule():
        root2.destroy()

    def cancel():
        root2.destroy()

    inButton = ttk.Button(root2, text="input", command=input_schedule)
    disButton=ttk.Button(root2,text="キャンセル",command=cancel)
    inButton.pack(padx=0.2)
    disButton.pack(padx=0.2)

    root2.mainloop()


class yotei_ire():
    def __init__(self, yotei):
        self.scedule = yotei


# ルートフレームの定義
def calnder_hyouji():
    root = tk.Tk()
    root.title("Calendar app")
    mycal = mycalendar(root)
    mycal.pack()
    root.mainloop()


# main関数
if __name__ == '__main__':
    calnder_hyouji()
