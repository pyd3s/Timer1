#!/usr/bin/env  python
from kivy.app import App 
from kivy.core.window import Window 
from kivy.clock import Clock 
from time import strftime
from kivy.utils import get_color_from_hex
class ClockApp(App):
    def update_time(self, nap):
            self.root.ids.time.text = strftime('%H:%M:%S')
    def on_start(self):
            Clock.schedule_interval(self.update_time, 1)
if __name__ == "__main__":
    Window.clearcolor=get_color_from_hex('#101216')
    ClockApp().run()
