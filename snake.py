from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle
import random

class SnakeGame(GridLayout):
    snake = ListProperty([[0, 0]])
    food = ListProperty([2, 2])
    direction = ListProperty([1, 0])
    grid_size = 6

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = self.grid_size
        self.rows = self.grid_size
        self.labels = []
        self.init_game()

        for row in range(self.rows):
            row_labels = []
            for col in range(self.cols):
                label = Label(size_hint=(None, None), size=(50, 50))
                self.add_widget(label)
                row_labels.append(label)
            self.labels.append(row_labels)

        Clock.schedule_interval(self.update, 1 / 2.0)
        Window.bind(on_key_down=self.on_key_down)

    def init_game(self):
        self.snake = [[0, 0]]
        self.food = [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]
        self.direction = [1, 0]

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        print(f"Key pressed: {key}")  # Debugging: Print the key pressed
        if key == 273 and self.direction != [0, -1]:  # Up
            print("Direction: Up")  # Debugging: Print direction change
            self.direction = [0, 1]
        elif key == 274 and self.direction != [0, 1]:  # Down
            print("Direction: Down")  # Debugging: Print direction change
            self.direction = [0, -1]
        elif key == 276 and self.direction != [1, 0]:  # Left
            print("Direction: Left")  # Debugging: Print direction change
            self.direction = [-1, 0]
        elif key == 275 and self.direction != [-1, 0]:  # Right
            print("Direction: Right")  # Debugging: Print direction change
            self.direction = [1, 0]

    def update(self, dt):
        new_head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]

        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= self.grid_size or
            new_head[1] < 0 or new_head[1] >= self.grid_size):
            self.init_game()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]
        else:
            self.snake.pop()

        self.update_board()

    def update_board(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.labels[row][col].canvas.before.clear()
                if [col, row] == self.food:
                    with self.labels[row][col].canvas.before:
                        Color(1, 0, 0, 1)
                        Rectangle(size=self.labels[row][col].size, pos=self.labels[row][col].pos)
                elif [col, row] in self.snake:
                    with self.labels[row][col].canvas.before:
                        Color(0, 1, 0, 1)
                        Rectangle(size=self.labels[row][col].size, pos=self.labels[row][col].pos)

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
