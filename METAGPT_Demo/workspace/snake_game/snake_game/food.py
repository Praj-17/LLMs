## food.py
import tkinter as tk
import random

class Food:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.body_size = 10
        self.position = self.generate_food()

    def generate_food(self):
        max_x = int(self.canvas.cget('width')) // self.body_size
        max_y = int(self.canvas.cget('height')) // self.body_size

        food_x = random.randint(1, max_x - 1) * self.body_size
        food_y = random.randint(1, max_y - 1) * self.body_size
        self.position = (food_x, food_y)

        self.food = self.canvas.create_rectangle(food_x, food_y, 
                                                 food_x + self.body_size, food_y + self.body_size, 
                                                 fill=self.color)
        return self.position
