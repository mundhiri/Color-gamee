from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class ColorGame(App):
    def build(self):
        self.colors = ['Red', 'Blue', 'Green', 'Yellow']
        self.color_hex = {
            'red': [1, 0, 0, 1],
            'blue': [0, 0, 1, 1],
            'green': [0, 1, 0, 1],
            'yellow': [1, 1, 0, 1],
            'gray': [0.2, 0.2, 0.2, 1]
        }
        self.score = 0
        self.current_color = ""
        self.time_left = 100
        self.game_running = False

        
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

      
        self.score_label = Label(text="Score: 0", font_size='24sp', bold=True, size_hint_y=0.1)
        self.main_layout.add_widget(self.score_label)

        self.timer_label = Label(text="||||||||||||||||||||||||||||||", font_size='20sp', color=[0, 1, 0, 1], size_hint_y=0.05)
        self.main_layout.add_widget(self.timer_label)

       
        self.light_box = Button(text="START", font_size='28sp', bold=True, background_color=self.color_hex['gray'], background_normal='', size_hint_y=0.4)
        self.light_box.bind(on_press=self.start_game)
        self.main_layout.add_widget(self.light_box)

        self.grid = GridLayout(cols=2, spacing=15, size_hint_y=0.4)
        
        self.btn_red = Button(text="RED", font_size='18sp', bold=True, background_color=self.color_hex['red'], background_normal='')
        self.btn_red.bind(on_press=lambda x: self.check_color('Red'))
        
        self.btn_green = Button(text="GREEN", font_size='18sp', bold=True, background_color=self.color_hex['green'], background_normal='')
        self.btn_green.bind(on_press=lambda x: self.check_color('Green'))
        
        self.btn_blue = Button(text="BLUE", font_size='18sp', bold=True, background_color=self.color_hex['blue'], background_normal='')
        self.btn_blue.bind(on_press=lambda x: self.check_color('Blue'))
        
        self.btn_yellow = Button(text="YELLOW", font_size='18sp', bold=True, background_color=self.color_hex['yellow'], background_normal='', color=[0,0,0,1])
        self.btn_yellow.bind(on_press=lambda x: self.check_color('Yellow'))

        self.grid.add_widget(self.btn_red)
        self.grid.add_widget(self.btn_green)
        self.grid.add_widget(self.btn_blue)
        self.grid.add_widget(self.btn_yellow)
        
        self.main_layout.add_widget(self.grid)
        return self.main_layout

    def start_game(self, instance):
        if self.game_running: return
        self.score = 0
        self.time_left = 100
        self.game_running = True
        self.score_label.text = "Score: 0"
        self.light_box.text = ""
        self.next_light()
        Clock.schedule_interval(self.update_timer, 0.05)

    def next_light(self):
        self.current_color = random.choice(self.colors)
        self.light_box.background_color = self.color_hex[self.current_color.lower()]

    def check_color(self, pressed_color):
        if not self.game_running: return
        if pressed_color.lower() == self.current_color.lower():
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            self.time_left = 100 
            self.next_light()
        else:
            self.game_over()

    def update_timer(self, dt):
        if not self.game_running: return False
        speed = 1 + (self.score * 0.1)
        self.time_left -= speed

        bars = int(self.time_left / 3.3)
        self.timer_label.text = "|" * max(0, bars)
        
        if self.time_left <= 0:
            self.game_over()
            return False

    def game_over(self):
        self.game_running = False
        self.light_box.background_color = self.color_hex['gray']
        self.light_box.text = f"GAME OVER!\nFinal Score: {self.score}\n\n[RESTART]"

if __name__ == '__main__':
    ColorGame().run()
