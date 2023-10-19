import random

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.speed = 3  # Initial speed of the ball
        self.hit_bottom = False

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self):
        pos = self.canvas.coords(self.id)
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = self.speed  # Reverse the Y direction
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle():
            self.y = -self.speed  # Reverse the Y direction
            self.speed += 1  # Increase the speed when hitting the paddle

        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x  # Reverse the X direction
