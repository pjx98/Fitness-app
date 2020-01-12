import kivy
kivy.require('1.11.1') # replace with your current kivy version !
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.core.window import Window
import time
from kivy.clock import Clock
from random import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from random import choice
from functools import partial
from kivy.graphics import Color, Ellipse, Rectangle
from plyer import vibrator
#:import rgba kivy.utils.get_color_from_hex

class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()





class FirstScreen(Screen):


    #some methods
    pass

class WorkoutScreen(Screen):
    pass


class SecondScreen(Screen):

    #some methods

    pass

class ThirdScreen(Screen):
    #some methods
    pass


class FourthScreen(Screen):
    #some methods

    pass





t = 120
check = 0


def my_callback(screen, dt):
    global t
    t -= 1
    if t == -1:
        t += 1
        vibrator.vibrate(10)
    screen.ids.timer.text = str(t)


class FifthScreen(Screen):
    def val0(self):
        global check
        if (check == 0):
            check = check + 1
            Clock.schedule_interval(partial(my_callback, self), 1)


class GymApp(App):

    def build(self):
        return MainScreen()



if __name__ == '__main__':
    GymApp().run()
