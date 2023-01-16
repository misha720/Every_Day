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

Window.title = "Every Day"
Window.clearcolor = (0/255, 0/255, 0/255)

class View(BoxLayout):
	pass

class EveryDayApp(App):
	def __init__(self, ):
		super(EveryDayApp,self).__init__()
		self.load_kv("main.kv")

	def build(self):
		return View()

if __name__ == '__main__':
	EveryDayApp().run()