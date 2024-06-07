from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime
from kivy.graphics import Color, Rectangle

class TimeDisplay(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create a background color
        with self.canvas.before:
            Color(0, 0, 0.5, 1)  # RGBA for dark blue
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        # Initialize stopwatch variables
        self.stopwatch_started = False
        self.stopwatch_time = 0

        # Create the label for current time
        self.time_label = Label(font_size=50, markup=True)
        self.add_widget(self.time_label)

        # Create the label for the stopwatch
        self.stopwatch_label = Label(font_size=50, markup=True, text='00:00:00')
        self.add_widget(self.stopwatch_label)

        # Create a layout for the buttons
        button_layout = BoxLayout(size_hint_y=None, height=50)
        self.add_widget(button_layout)

        # Create buttons
        self.start_button = Button(text='Start')
        self.start_button.bind(on_press=self.start_stopwatch)
        button_layout.add_widget(self.start_button)

        self.stop_button = Button(text='Stop')
        self.stop_button.bind(on_press=self.stop_stopwatch)
        button_layout.add_widget(self.stop_button)

        self.reset_button = Button(text='Reset')
        self.reset_button.bind(on_press=self.reset_stopwatch)
        button_layout.add_widget(self.reset_button)

        # Schedule the update function to be called every second
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)

    def update_time(self, dt):
        # Get the current time
        now = datetime.now().strftime("%H:%M:%S")
        
        # Format the time string with color tags
        formatted_time = f"[color=00FF00]{now[:2]}[/color][color=FF0000]:[/color][color=00FF00]{now[3:5]}[/color][color=FF0000]:[/color][color=00FF00]{now[6:]}[/color]"
        
        # Update the label text
        self.time_label.text = formatted_time

        # Update stopwatch if started
        if self.stopwatch_started:
            self.stopwatch_time += 1
            minutes, seconds = divmod(self.stopwatch_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.stopwatch_label.text = f'{hours:02}:{minutes:02}:{seconds:02}'

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def start_stopwatch(self, instance):
        self.stopwatch_started = True

    def stop_stopwatch(self, instance):
        self.stopwatch_started = False

    def reset_stopwatch(self, instance):
        self.stopwatch_started = False
        self.stopwatch_time = 0
        self.stopwatch_label.text = '00:00:00'

class TimeApp(App):
    def build(self):
        return TimeDisplay()

if __name__ == '__main__':
    TimeApp().run()
