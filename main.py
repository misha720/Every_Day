'''
	Мур Мяу кодировка v2.0
	Графическое окружение
'''

''' 
	COLORS:
		(0/255, 0/255, 0/255, 1) - Background
		(63/255, 63/255, 63/255, 1) - Ponel

		(135/255, 194/255, 133/255, 1) - Green
		(153/255, 219/255, 150/255, 1) - Duble Green

		(135/255, 194/255, 133/255, 1) - Red

		(79/255, 56/255, 146/255, 1) - Purple
		(108/255, 73/255, 211/255, 1) - Duble Purple
		(183/255, 162/255, 245/255, 1) - TextInput Purple
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

		self.ctrl_add_tast = 0
		self.input_add_task.opacity = 0
		self.input_add_task.size = (0,0)

		self.rv.data = [{'text': "Купить мише жижу"}]

	def add_new_task(self):
		if self.ctrl_add_tast == 0:
			self.add_task.text = "Отмена"
			self.add_task.background_color = (219/255, 74/255, 74/255)
			self.input_add_task.opacity = 1
			self.input_add_task.size = (395,175)

			self.ctrl_add_tast = 1

		elif self.ctrl_add_tast == 1:
			self.add_task.text = "Добавить"
			self.add_task.background_color = (135/255, 194/255, 133/255)
			self.input_add_task.opacity = 0
			self.input_add_task.size = (0,0)

			self.ctrl_add_tast = 0

	def add_input_task(self):
		title = self.add_input_title_task.text
		keys = self.add_input_keys_task.text

		self.rv.data.append( {'text':title} )

		self.add_input_title_task.text = ""
		self.add_input_keys_task.text = ""

		self.add_task.text = "Добавить"
		self.add_task.background_color = (135/255, 194/255, 133/255)
		self.input_add_task.opacity = 0
		self.input_add_task.size = (0,0)

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