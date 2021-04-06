from kivy.app import App
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.text import FontContextManager as FCM
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.dropdown import DropDown
import pytz
from pytz import timezone
# The Button is a Label with associated actions 
# that are triggered when the button is pressed 
# (or released after a click / touch) 
from kivy.uix.button import Button 
# another way used to run kivy app  
from kivy.base import runTouchApp 
#####################################
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
timezonelist = ['UTC','US/Pacific','Europe/Berlin']
for zone in timezonelist:

    now_time = datetime.now(timezone(zone))
    print (now_time.strftime(fmt))
###########################################
# create a dropdown with 10 buttons 
dropdown = DropDown() 
for index in range(10): 
  
    # Adding button in drop down list 
    btn = Button(text ='Value % d' % index, size_hint_y = None, height = 40) 

    # binding the button to show the text when selected 
    btn.bind(on_release = lambda btn: dropdown.select(btn.text)) 
    # then add the button inside the dropdown 
    dropdown.add_widget(btn) 
# create a big main button 
mainbutton = Button(text ='timezone', size_hint =(None, None), pos =(200,200)) 

# show the dropdown menu when the main button is released 
# note: all the bind() calls pass the instance of the caller  
# (here, the mainbutton instance) as the first argument of the callback 
# (here, dropdown.open.). 
mainbutton.bind(on_release = dropdown.open) 
  
# one last thing, listen for the selection in the  
# dropdown list and assign the data to the button text. 
dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x)) 
###################add button##################

#####################################
class RootWidget(BoxLayout):
    pass

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

class MyApp(App):
    types=3
    def build(self):
        root=RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        b=Button(text="new")
        b.bind(on_press=self.callback)
        root.add_widget(b)
        self.now = datetime.now()
        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text= "[size=60][b][color=ff3333]"+datetime.now(timezone(timezonelist[0])).strftime('%H:%M:%S')+"[/color][/b][/size]",markup=True)
        root.add_widget(self.my_label)
        root.add_widget(mainbutton)
        c.add_widget(
            AsyncImage(
                source="c:/b.jpg",
                size_hint= (1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}))
        return root  # The label is the only widget in the interface
    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now_time = datetime.now(timezone(timezonelist[0])) + timedelta(seconds = 1)
        self.my_label.text = "[size=60][b][color=ff3333]"+self.now_time.strftime('%H:%M:%S')+"[/color][/b][/size]"
    def callback(self,event):
        if self.types==3:
            self.call
            print(timezonelist[0])
        elif self.types==4:
            print(timezonelist[1])
    def call(self,event):
        print("1")

MyApp().run()
