#!/usr/bin/env  python
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
import sys
import time
   
class P_Timmer(GridLayout):
    def __init__(self,**kwargs):
        super(P_Timmer,self).__init__(**kwargs)
        self.cols=2
        self.rows=3
        self.fresh_label=Label(text="Seconds")
        self.add_widget(self.fresh_label)
        self.p_seconds=TextInput(text="",multiline=False)
        self.add_widget(self.p_seconds)
        self.p_button1= Button(text="Start", on_press=self.on_start)
        self.add_widget(self.p_button1)
        self.p_button2= Button(text="Exit", on_press=self.p_exit)
        self.add_widget(self.p_button2)
        self.p_seconds.bind(on_text_validate=self.on_enter)

    def on_start(self,instance):
        self.text=self.p_seconds.text
        clock_test=Clock.schedule_interval(self.update_time, 1)
    def update_time(self,nap):
        self.fresh_label.text=str(self.text)
        new_test=int(self.text)
        if new_test <=0:
            self.p_sound()
            contentb = Button(text='Job Done!')
            popup = Popup(title="Pydes Timer",content=contentb,auto_dismiss=False)
            contentb.bind(on_press=popup.dismiss)
            popup.bind(on_dismiss=self.p_exit)
            popup.open()
        else:
            new_test=int(self.text)-1
            self.text=str(new_test)
            return  new_test
    def on_enter(self,instance):
        print 'User press enter in',instance
        print 'User input',instance.text
    def p_exit(self,isinstance):
        print 'Exit App'
        sys.exit()
    def p_sound(self):
        sound = SoundLoader.load('ring.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
class TimerApp(App):
    def build(self):
        return P_Timmer()

if __name__ == "__main__":
    TimerApp().run()
