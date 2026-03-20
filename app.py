import tkinter as tk
import api, webbrowser
from tkcalendar import Calendar
from utils import generate_random_token, generate_random_graph_id

TITLE_FONT = ("Arial", 20, "bold")
SUBTITLE_FONT = ("Arial", 9)
LABEL_FONT = ("Arial", 11, "bold")
HINT_FONT = ("Arial", 8)
ENTRY_FONT = ("Arial", 11)
BUTTON_FONT = ("Arial", 10, "bold")
SMALL_FONT = ("Arial", 9)
STATUS_FONT = ("Arial", 9)

BG = "#f7f3ee"
SURFACE = "#ede8e0"
TEXT = "#2b2b2b"
MUTED = "#8a8070"
BTN_PRIMARY = "#5c4a32"
BTN_SECONDARY = "#7a9e7e"
BTN_DANGER = "#b85c5c"
WHITE = "#ffffff"

class HabitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("600x700")
        # self.root.resizable(False, False)

        self.token = None
        self.username = None
        self.graph_id = None
        self.signup_screen()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def signup_screen(self):
        self.clear()
        self.root.configure(bg=BG)

        tk.Label(self.root, text="Create Account", font=TITLE_FONT,
                 bg=BG, fg=TEXT).pack(pady=(25, 3))
        tk.Label(self.root, text="start tracking your habit",
                 font=SUBTITLE_FONT, bg=BG, fg=MUTED).pack()

        form = tk.Frame(self.root, bg=SURFACE)
        form.pack(padx=30, pady=18, fill="x")

        tk.Label(form, text="Username", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(12, 2))
        tk.Label(form, text="lowercase letters and numbers only",
                 font=HINT_FONT, bg=SURFACE, fg=MUTED).pack(anchor="w", padx=12)
        self.uname_var = tk.StringVar()
        tk.Entry(form, textvariable=self.uname_var, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 10), fill="x")

        tk.Label(form, text="Habit name", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(6, 2))
        self.habit_var = tk.StringVar()
        tk.Entry(form, textvariable=self.habit_var, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 10), fill="x")

        tk.Label(form, text="Unit", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(6, 2))
        tk.Label(form, text="e.g. km, hours, pages",
                 font=HINT_FONT, bg=SURFACE, fg=MUTED).pack(anchor="w", padx=12)
        self.unit_var = tk.StringVar(value="hours")
        tk.Entry(form, textvariable=self.unit_var, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 14), fill="x")

        self.signup_status = tk.Label(self.root, text="", font=STATUS_FONT,
                                      bg=BG, fg=BTN_DANGER)
        self.signup_status.pack()

        tk.Button(self.root, text="Create Account",
                  command=self.create_account,
                  bg=BTN_PRIMARY, fg=WHITE,
                  font=BUTTON_FONT, relief="flat",
                  padx=18, pady=8, cursor="hand2").pack(pady=12)

        tk.Label(self.root, text="already have an account?",
                 font=SMALL_FONT, bg=BG, fg=MUTED).pack()
        tk.Button(self.root, text="Login",
                  command=self.login_screen,
                  bg=SURFACE, fg=BTN_PRIMARY,
                  font=SMALL_FONT, relief="flat",
                  padx=10, pady=4, cursor="hand2").pack(pady=4)

    def login_screen(self):
        self.clear()
        self.root.configure(bg=BG)

        tk.Label(self.root, text="LOGIN", font=TITLE_FONT,
                 bg=BG, fg=TEXT).pack(pady=(25, 3))
        tk.Label(self.root, text="Welcome back",
                 font=SUBTITLE_FONT, bg=BG, fg=MUTED).pack()

        form = tk.Frame(self.root, bg=SURFACE)
        form.pack(padx=30, pady=18, fill="x")

        tk.Label(form, text="Username", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(12, 2))

        self.login_uname_var = tk.StringVar()
        tk.Entry(form, textvariable=self.login_uname_var, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 10), fill="x")

        tk.Label(form, text="Token", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(6, 2))
        self.login_token = tk.StringVar()
        tk.Entry(form, textvariable=self.login_token, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 10), fill="x")

        tk.Label(form, text="Graph ID", font=LABEL_FONT,
                 bg=SURFACE, fg=TEXT).pack(anchor="w", padx=12, pady=(6, 2))

        self.login_graph_id = tk.StringVar()
        tk.Entry(form, textvariable=self.login_graph_id, bg=WHITE, fg=TEXT,
                 font=ENTRY_FONT, relief="solid", bd=1).pack(padx=12, pady=(3, 14), fill="x")

        self.login_status = tk.Label(self.root, text="", font=STATUS_FONT,
                                      bg=BG, fg=BTN_DANGER)
        self.login_status.pack()

        tk.Button(self.root, text="Login",
                  command=self.do_login,
                  bg=BTN_PRIMARY, fg=WHITE,
                  font=BUTTON_FONT, relief="flat",
                  padx=18, pady=8, cursor="hand2").pack(pady=12)

        tk.Button(self.root, text="Back",
                  command=self.signup_screen,
                  bg=SURFACE, fg=BTN_PRIMARY,
                  font=SMALL_FONT, relief="flat",
                  padx=10, pady=4, cursor="hand2").pack(pady=4)

    def do_login(self):
        u = self.login_uname_var.get().strip()
        t = self.login_token.get().strip()
        g = self.login_graph_id.get().strip()
        if not u or not t or not g:
            self.login_status.config(text="fill all fields!!")
            return
        self.username = u
        self.token = t
        self.graph_id = g
        self.tracker_screen()

    def create_account(self):
        u = self.uname_var.get().strip().lower()
        name = self.habit_var.get().strip()
        unit = self.unit_var.get().strip()
        if not u or not name or not unit:
            self.signup_status.config(text="fill all fields")
            return

        tok = generate_random_token()
        gid = generate_random_graph_id()

        res1 = api.create_user_account(u, tok)
        if not res1.get("isSuccess"):
            self.signup_status.config(text=res1.get("message"))
            return
        res2 = api.create_graph(u, tok, gid, name, unit)
        if not res2.get("isSuccess"):
            self.signup_status.config(text=res2.get("message"))
            return
        self.username = u
        self.token = tok
        self.graph_id = gid
        self.creds_screen()

    def tracker_screen(self):
        self.clear()
        self.root.configure(bg=BG)

        tk.Label(self.root, text="Log Habit", font=TITLE_FONT, bg=BG, fg=TEXT).pack(pady=(20, 3))

        info_frame = tk.Frame(self.root, bg=SURFACE)
        info_frame.pack(padx=30, pady=(0, 10), fill="x")

        tk.Label(self.root, text="Kindly copy the Username, Token and Graph ID to login again",
                 font=HINT_FONT, fg=BTN_DANGER, bg=BG).pack(pady=(0, 5))

        for label, value in [("Username", self.username), ("Token", self.token), ("Graph ID", self.graph_id)]:
            row = tk.Frame(info_frame, bg=SURFACE)
            row.pack(padx=12, pady=4, fill="x")
            tk.Label(row, text=label + ":", font=SMALL_FONT,
                     bg=SURFACE, fg=MUTED, width=10, anchor="w").pack(side="left")
            var = tk.StringVar(value=value)
            tk.Entry(row, textvariable=var, font=SMALL_FONT,
                     bg=SURFACE, fg=TEXT, relief="flat", bd=0,
                     readonlybackground=SURFACE,
                     state="readonly").pack(side="left", fill="x", expand=True)

        self.cal = Calendar(self.root, selectmode="day", date_pattern="yyyyMMdd", font=("Arial", 9))
        self.cal.pack(pady=10)

        tk.Label(self.root, text="Quantity", font=LABEL_FONT, bg=BG, fg=TEXT).pack()
        self.qty_var = tk.StringVar(value="0")
        tk.Entry(self.root, textvariable=self.qty_var, font=ENTRY_FONT,
                 bg=WHITE, fg=TEXT, relief="solid", bd=1,
                 justify="center", width=10).pack(pady=5)

        btn_row = tk.Frame(self.root, bg=BG)
        btn_row.pack(pady=12)

        tk.Button(btn_row, text="Add", command=self.add_pixel,
                  bg=BTN_PRIMARY, fg=WHITE, font=BUTTON_FONT,
                  relief="flat", padx=18, pady=8,
                  cursor="hand2").pack(side="left", padx=5)

        tk.Button(btn_row, text="Update", command=self.update_pixel,
                  bg=BTN_SECONDARY, fg=WHITE, font=BUTTON_FONT,
                  relief="flat", padx=18, pady=8,
                  cursor="hand2").pack(side="left", padx=5)

        tk.Button(btn_row, text="Delete", command=self.delete_pixel,
                  bg=BTN_DANGER, fg=WHITE, font=BUTTON_FONT,
                  relief="flat", padx=18, pady=8,
                  cursor="hand2").pack(side="left", padx=5)

        # view graph at bottom
        tk.Button(self.root, text="View My Graph",
                  command=self.open_graph,
                  bg=SURFACE, fg=BTN_PRIMARY,
                  font=BUTTON_FONT, relief="flat",
                  padx=18, pady=8, cursor="hand2").pack(pady=10)

        # status message
        self.tracker_status = tk.Label(self.root, text="", font=STATUS_FONT,
                                       bg=BG, fg=BTN_DANGER)
        self.tracker_status.pack()

    def open_graph(self):
        webbrowser.open(f"https://pixe.la/v1/users/{self.username}/graphs/{self.graph_id}.html")

    def add_pixel(self):
        date = self.cal.get_date()
        qty = self.qty_var.get().strip()
        res = api.add_pixel(self.username, self.token, self.graph_id, date, qty)
        if res.get("isSuccess"):
            self.tracker_status.config(text=f"added {qty} for {date}", fg=BTN_SECONDARY)
        else:
            self.tracker_status.config(text=res.get("message"), fg=BTN_DANGER)

    def update_pixel(self):
        date = self.cal.get_date()
        qty = self.qty_var.get().strip()
        res = api.update_pixel(self.username, self.token, self.graph_id, date, qty)
        if res.get("isSuccess"):
            self.tracker_status.config(text=f"updated {date} to {qty}", fg=BTN_SECONDARY)
        else:
            self.tracker_status.config(text=res.get("message"), fg=BTN_DANGER)

    def delete_pixel(self):
        date = self.cal.get_date()
        res = api.delete_pixel(self.username, self.token, self.graph_id, date)
        if res.get("isSuccess"):
            self.tracker_status.config(text=f"deleted {date}", fg=BTN_SECONDARY)
        else:
            self.tracker_status.config(text=res.get("message"), fg=BTN_DANGER)

    def creds_screen(self):
        self.clear()
        self.root.configure(bg=BG)

        tk.Label(self.root, text="Account Created!", font=TITLE_FONT,
                 bg=BG, fg=TEXT).pack(pady=(25, 3))
        tk.Label(self.root, text="save these details before continuing",
                 font=HINT_FONT, bg=BG, fg=BTN_DANGER).pack()

        info_frame = tk.Frame(self.root, bg=SURFACE)
        info_frame.pack(padx=30, pady=15, fill="x")

        for label, value in [("Username", self.username), ("Token", self.token), ("Graph ID", self.graph_id)]:
            row = tk.Frame(info_frame, bg=SURFACE)
            row.pack(padx=12, pady=6, fill="x")
            tk.Label(row, text=label + ":", font=LABEL_FONT,
                     bg=SURFACE, fg=MUTED, width=10, anchor="w").pack(side="left")
            var = tk.StringVar(value=value)
            tk.Entry(row, textvariable=var, font=ENTRY_FONT,
                     bg=WHITE, fg=TEXT, relief="solid", bd=1,
                     readonlybackground=WHITE,
                     state="readonly").pack(side="left", fill="x", expand=True)

        tk.Label(self.root, text="screenshot or copy these — you cant recover them later",
                 font=HINT_FONT, bg=BG, fg=BTN_DANGER).pack(pady=5)

        tk.Button(self.root, text="Continue to Tracker",
                  command=self.tracker_screen,
                  bg=BTN_PRIMARY, fg=WHITE,
                  font=BUTTON_FONT, relief="flat",
                  padx=18, pady=8, cursor="hand2").pack(pady=15)