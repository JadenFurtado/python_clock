
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.text import FontContextManager as FCM
from kivy.uix.image import AsyncImage
from kivy.base import runTouchApp 
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

timezonelist = ['UTC','US/Pacific','Europe/Berlin']

Screen_list={1:'MenuScreen',2:'SettingsScreen'}

##############################################

def switch_function(a):
    pass

##############################################

class RootWidget(BoxLayout):
    pass

class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        prev = Button(size_hint =(.5, .2),  text ="previous")
        #prev.bind(on_press=switch_function(2))
        nexts = Button(size_hint =(.5, .2),pos=(400,0),text ="next")
        #nexts.bind(on_press=switch_function(1))
        self.add_widget(prev)
        self.add_widget(nexts)
        root=RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        self.now = datetime.now(timezone('US/Pacific'))
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text= "[b][color=ff3333]self.now.strftime('%H:%M:%S')[/color][/b]",font_size='50sp',markup=True)
        root.add_widget(self.my_label)
        c.add_widget(
            AsyncImage(
                source="c:/b.jpg",
                size_hint= (1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}))
        self.add_widget(root)
    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds = 1)
        self.my_label.text = "[b][color=ff3333]"+self.now.strftime('%H:%M:%S')+"[/color][/b]"

class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0, 147, 153, 0.6)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MenuButton():
    pass

class SettingsScreen(Screen):
    def __init__(self,**kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        prev = Button(size_hint =(.5, .2),  text ="previous")
        #prev.bind(on_press=switch_function(1))
        nexts = Button(size_hint =(.5, .2),pos=(400,0),text ="next") 
        #nexts.bind(on_press=switch_function(2))
        self.add_widget(prev)
        self.add_widget(nexts)
        root=RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        self.now = datetime.now(timezone('US/Pacific'))
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text= "[b][color=ff3333]self.now.strftime('%H:%M:%S')[/color][/b]",font_size='50sp',markup=True)
        root.add_widget(self.my_label)
        c.add_widget(
            AsyncImage(
                source="c:/b.jpg",
                size_hint= (1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}))
        self.add_widget(root)
    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds = 1)
        self.my_label.text = "[b][color=ff3333]"+self.now.strftime('%H:%M:%S')+"[/color][/b]"

class TestApp(App):
    
    
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    TestApp().run()