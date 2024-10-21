import kivy
kivy.require('2.3.0')

from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton
from kivymd.uix.button import MDButtonText
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.logger import Logger

from cmd import str_translator as strTranslator
from gui.snackbar_hint import Snackbar

from plyer import filechooser

class StrTransforScreen(MDScreen): 
	'''
	exercute the command:
	/usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/strTranslator.py \
	--input /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx \
	--output /Users/kellyhong/Documents/tool/MyTools/en \
	-c
	-s
	'''

	callback = None
	hint = Snackbar()

	def __init__(self, *args, **kwargs):
		super(StrTransforScreen, self).__init__(*args, **kwargs)
		self.callback = Clock.create_trigger(self.exercute, 0.2)
	
	def transfor(self):
		if not self.callback:
			return
		self.callback()
	
	def exercute(self, *args):
		Logger.info("Hello, I got an event!" + str(args))
		file_dir = self.ids.id_file_dir.selections[0]
		export_dir = self.ids.id_export_dir.selections[0]
		is_category_sliced = self.ids.id_is_category_sliced.isChecked()
		is_sorted = self.ids.id_is_sorted.isChecked()

		Logger.info(f"try...{str(file_dir)}, {str(export_dir)}, {is_category_sliced}, {is_sorted}")
		try:
			strTranslator.trans(file_dir=file_dir, export_dir= export_dir, 
								is_category_sliced= is_category_sliced, is_sort= is_sorted)
			self.hint.show(content="File generating is success!", output = export_dir)
		except Exception as e:
			Logger.error(e)
			self.hint.show(content="Failed by: " + str(e))

class SmallButton(MDButton):
	ui_text = ObjectProperty()
	label = StringProperty("Select")

	def __init__(self, **kwargs): # initialized this class when the class instantiated
		super(SmallButton, self).__init__(**kwargs)
		self.font_style = "Label"
		self.radius = 20
		self.theme_width = "Custom"
		self.height = "40dp"
		self.width = "120dp"

		self.ui_text = MDButtonText(text=self.label,
									pos_hint= {"center_x": .5, "center_y": .5})
		self.add_widget(self.ui_text)
		Logger.info("label_add_widget" + self.label)

	
	def on_label(self, *a, **k):
		self.remove_widget(self.ui_text)
		self.ui_text = MDButtonText(text=self.label,
									pos_hint= {"center_x": .5, "center_y": .5})
		Logger.info("on_label" + self.label)
		self.add_widget(self.ui_text)

class FileSelector(MDBoxLayout):
	ui_button = ObjectProperty()
	ui_label = ObjectProperty()
	ui_content = ObjectProperty()
	
	title_name = StringProperty("hello")
	selections = ListProperty([])

	def __init__(self, **kwargs): 
		super(FileSelector, self).__init__(**kwargs)
				
		self.orientation = "vertical"
		
		title = MDBoxLayout(orientation = "horizontal")
		title.size_hint = [0.8, 0.1]
		title.height = 56

		self.ui_label = MDLabel(text=self.title_name)
		self.ui_button = SmallButton(pos_hint = {"center_y": .5})
		self.ui_button.bind(on_press=self.click_select)

		title.add_widget(self.ui_label)
		title.add_widget(self.ui_button)
		self.add_widget(title)

		content = str(self.selections)
		self.ui_content = MDLabel(text=content, 
						  pos_hint = {"center_y": .5},
						  size_hint = [0.8, 1],
						  role="medium")
		
		self.add_widget(self.ui_content)


	def click_select(self, arg):
		Clock.schedule_once(self.choose, 0.2)

	def choose(self, arg):
		'''
		Call plyer filechooser API to run a filechooser Activity.
		'''
		try:
			filechooser.open_file(on_selection=self.handle_selection)
		finally:
			Logger.info("close the file")

	def handle_selection(self, selection):
		'''
		Callback function for handling the selection response from Activity.
		'''
		if not selection: 
			return
		self.selections = selection
		Logger.info(f"select file {self.selections}")

	def on_title_name(self, *a, **k):
		self.ui_label.text = self.title_name
	
	def on_selections(self, *a, **k):
		'''
		Update TextInput.text after FileChoose.selection is changed
		via FileChoose.handle_selection.
		'''
		# App.get_running_app().root.ids.result.text = str(self.selection)
		self.ui_content.text = self.selections[0]


class DirSelector(FileSelector):
	def __init__(self, **kwargs): 
		super(DirSelector, self).__init__(**kwargs)

		self.ui_button.unbind(on_press = self.click_select)
		self.ui_button.bind(on_press = self.click_select_dir)

	def click_select_dir(self, arg):
		Clock.schedule_once(self.chooseDir, 0.2)
	
	def chooseDir(self, arg):
		'''
		Call plyer filechooser API to run a filechooser Activity.
		'''
		try:
			filechooser.choose_dir(on_selection=self.handle_selection)
		finally:
			Logger.info("close the dir")

class CheckItem(MDBoxLayout):
	text = StringProperty()
	group = StringProperty()

	def isChecked(self):
		return self.ids.id_check_box.active