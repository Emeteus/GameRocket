from tkinter import Button, CENTER, messagebox

class EventHandler:
    def __init__(self, tk):
        self.is_active = False
        self.tk = tk

        self.start_button = Button(tk, text="Start", command=self.start_game, height=2, width=40, bg="green", fg="red")
        self.start_button.pack()
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.tk.bind('<Escape>', lambda event=None: self.quit_game())

    def start_game(self):
        self.is_active = True
        self.start_button.destroy()

    def quit_game(self):
        if self.is_active:
            self.is_active = False
            self.start_button = Button(self.tk, text="Start", command=self.start_game, height=2, width=40, bg="green", fg="red")
            self.start_button.pack()
            self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            result = messagebox.askquestion("Выход", "Вы уверены, что хотите выйти?")
            if result == "Да":
                self.tk.quit()
