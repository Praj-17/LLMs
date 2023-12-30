## snake.py
import tkinter as tk

class Snake:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.body_size = 10
        self.body_positions = [(100, 100), (90, 100), (80, 100)]
        self.body = []
        for position in self.body_positions:
            body_part = canvas.create_rectangle(position[0], position[1], 
                                                position[0]+self.body_size, position[1]+self.body_size, 
                                                fill=self.color)
            self.body.append(body_part)
        self.direction = "Right"
        self.bind_movement()

    def bind_movement(self):
        self.canvas.bind_all("<KeyPress-Up>", self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_down)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def turn_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"

    def turn_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"

    def turn_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"

    def turn_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"

    def move(self):
        head_x_position, head_y_position = self.body_positions[0]
        if self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - self.body_size)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + self.body_size)
        elif self.direction == "Left":
            new_head_position = (head_x_position - self.body_size, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + self.body_size, head_y_position)
        self.body_positions = [new_head_position] + self.body_positions[:-1]
        for part, position in zip(self.body, self.body_positions):
            self.canvas.coords(part, position[0], position[1], 
                               position[0]+self.body_size, position[1]+self.body_size)

    def eat(self, food_position):
        self.body_positions = [food_position] + self.body_positions
        new_body_part = self.canvas.create_rectangle(food_position[0], food_position[1], 
                                                     food_position[0]+self.body_size, food_position[1]+self.body_size, 
                                                     fill=self.color)
        self.body.insert(0, new_body_part)
