from tkinter import *
import time
import json
from Ball import Ball
from Paddle import Paddle
from EventHandling import EventHandler
from GameOver import GameOver

tk = Tk()
tk.title("Гра JUMP!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
event_handler = EventHandler(tk)

score = 0
score_display = canvas.create_text(50, 20, text=f"Рахунок: {score}", fill="black", font=("Helvetica", 12), anchor="nw")

best_score = 0

def load_best_score():
    global best_score
    try:
        with open("game_results.json", "r") as json_file:
            results = [json.loads(line) for line in json_file if line.strip()]
            if results:
                best_score = max(results, key=lambda x: x.get("score", 0))["score"]
    except (FileNotFoundError, json.JSONDecodeError):
        pass

load_best_score()

def increase_score():
    global score
    score += 1
    canvas.itemconfig(score_display, text=f"Рахунок: {score}")

def update_best_score():
    global best_score
    canvas.itemconfig(best_score_display, text=f"Найкращий Рахунок: {best_score}")

best_score_display = canvas.create_text(450, 20, text=f"Найкращий Рахунок: {best_score}", fill="black", font=("Helvetica", 12), anchor="ne")

while not event_handler.is_active:
    tk.update()

while True:
    if not event_handler.is_active:
        break

    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()

        if ball.hit_paddle():
            increase_score()

    else:
        game_over_root = Tk()
        game_over_screen = GameOver(game_over_root)
        game_over_root.mainloop()

        result = {"score": score}
        with open("game_results.json", "a") as json_file:
            json.dump(result, json_file)
            json_file.write("\n")

        update_best_score()

        break

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

def load_high_scores():
    try:
        with open("game_results.json", "r") as json_file:
            results = [json.loads(line) for line in json_file if line.strip()]
            high_scores = [result["score"] for result in results]
            high_scores.sort(reverse=True)
            top_scores = high_scores[:10]

            high_score_text = "Топ-рекорди:\n"
            for i, score in enumerate(top_scores, 1):
                high_score_text += f"{i}. {score}\n"

            high_score_display = canvas.create_text(450, 60, text=high_score_text, fill="black", font=("Helvetica", 12), anchor="ne")
    except (FileNotFoundError, json.JSONDecodeError):
        pass

load_high_scores()



tk.mainloop()
