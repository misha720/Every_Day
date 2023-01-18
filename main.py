'''
	Мур Мяу кодировка v2.0
	Графическое окружение
'''

#	KIVY
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 840)
Config.set('graphics', 'height', 640)

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.recycleview import RecycleView

Window.title = "Every Day"
Window.clearcolor = (0/255, 0/255, 0/255)

class PlansScreen(Screen):
	def __init__(self, **kwargs):
		super(PlansScreen,self).__init__(**kwargs)
		self.rv.data = [{'text': str(x)} for x in range(100)]

class TodayScreen(Screen):
	pass

class EveryDayApp(App):
	def __init__(self, **kwargs):
		super(EveryDayApp,self).__init__(**kwargs)
		self.load_kv("main.kv")

	def build(self):
		self.sm = ScreenManager(transition=NoTransition())

		self.sm.add_widget(TodayScreen(name="today"))
		self.sm.add_widget(PlansScreen(name="plans"))

		return self.sm

if __name__ == '__main__':
	EveryDayApp().run()