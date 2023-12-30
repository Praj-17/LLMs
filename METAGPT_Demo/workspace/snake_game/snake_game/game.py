## game.py
import tkinter as tk
from snake import Snake
from food import Food
from leaderboard import Leaderboard

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas, "green")
        self.food = Food(self.canvas, "red")
        self.leaderboard = Leaderboard()
        self.score = 0
        self.game_over = False

    def start_game(self):
        self.root.after(100, self.update_game_state)
        self.root.mainloop()

    def update_game_state(self):
        if self.game_over:
            return
        self.snake.move()
        self.check_collision()  # Check for collisions after each move
        if self.snake.body_positions[0] == self.food.position:
            self.snake.eat(self.food.position)
            self.food.generate_food()
            self.score += 1
            self.leaderboard.update_leaderboard("Player", self.score)
        self.root.after(100, self.update_game_state)

    def end_game(self):
        self.game_over = True
        self.leaderboard.display_leaderboard()
        self.root.destroy()

    def check_collision(self):
        head_x_position, head_y_position = self.snake.body_positions[0]
        if (head_x_position < 0 or head_y_position < 0 or 
            head_x_position >= 500 or head_y_position >= 500 or
            (head_x_position, head_y_position) in self.snake.body_positions[1:]):
            self.end_game()
