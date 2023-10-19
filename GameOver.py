from tkinter import Tk, Label, Button

class GameOver:
    def __init__(self, master):
        self.master = master
        self.master.title("Гра завершена")
        self.master.attributes('-topmost', True)
        self.label = Label(self.master, text="Гра завершена!", font=("Helvetica", 24))
        self.label.pack(pady=50)

        self.button = Button(self.master, text="Вихід", command=self.master.quit, font=("Helvetica", 16))
        self.button.config(bg="green", fg="red", height=2, width=10)
        self.button.pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    game_over_screen = GameOver(root)
    root.mainloop()
