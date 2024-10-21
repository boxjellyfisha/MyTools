import kivy

kivy.require('2.3.0')

from kivy.properties import StringProperty, ListProperty, ObjectProperty, ReferenceListProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton

from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.logger import Logger

from cmd import xml2csv as xml2csv

from plyer import filechooser

class Xml2CsvScreen(MDScreen): 
	'''
	exercute the command:
	# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/xml2csv.py \
	# --language en,en,ch \
	# --xml /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml,/Users/kellyhong/Documents/tool/MyTools/en/try3.xml \
	# --output /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx
	# -s
	'''

	callback = None

	def __init__(self, *args, **kwargs):
		super(Xml2CsvScreen, self).__init__(*args, **kwargs)
		self.callback = Clock.create_trigger(self.exercute, 0.2)
	
	def transfor(self):
		if not self.callback:
			return
		self.callback()
	
	def exercute(self, *args):
		Logger.info("Hello, I got an event!" + str(args))
		languges, file_dir = self.ids.id_file_dir.get_selection_paths()
		is_csv = self.ids.id_is_csv.isChecked()
		export_dir = self.ids.id_export_dir.selections[0] + '/output_string' 
		export_dir += '.csv' if is_csv else '.xlsx'
		is_sorted = self.ids.id_is_sorted.isChecked()

		Logger.info("try..." + str(languges) + "; " + str(file_dir) + "; " + str(export_dir) + "; " + str(is_sorted))
		xml2csv.trans(lang_types = languges.split(","),
				file_xmls = file_dir.split(","), 
				output_file_path = export_dir, 
				is_sort = is_sorted)

class FilesSelector(MDBoxLayout):
	ui_button = ObjectProperty()
	ui_label = ObjectProperty()
	ui_content = ObjectProperty()
	
	title_name = StringProperty("hello")
	selections = ListProperty([])

	def __init__(self, **kwargs): 
		super(FilesSelector, self).__init__(**kwargs)
				
		self.orientation = "vertical"
		
		title = MDBoxLayout(orientation = "horizontal")
		title.size_hint = [0.8, 0.1]
		title.height = 56

		self.ui_label = MDLabel(text=self.title_name)

		self.ui_button = MDIconButton(icon = "plus")
		self.ui_button.bind(on_press=self.click_select)

		title.add_widget(self.ui_label)
		title.add_widget(self.ui_button)
		self.add_widget(title)	

	def click_select(self, arg):
		Clock.schedule_once(self.choose, 0.2)

	def choose(self, arg):
		'''
		Call plyer filechooser API to run a filechooser Activity.
		'''
		try:
			filechooser.open_file(on_selection=self.handle_selection, multiple=True)
		finally:
			Logger.info("close the file")

	def handle_selection(self, selection):
		'''
		Callback function for handling the selection response from Activity.
		'''
		if not selection: 
			return
		isSaved = False		
		for i in range(len(self.selections)):
			item = self.selections[i]
			Logger.info(item)
			if type(item) is dict and item["text"] in selection:
				isSaved = True
				break
		
		
		if not isSaved:
			for s in selection:
				self.selections.append({"text": s, 
									    "pressed": self.remove_selection, 
										"origin_lang":"en"})

	def remove_selection(self, *a):
		Logger.info(a)
		for i in range(len(self.selections)):
			item = self.selections[i]
			if type(item) is dict and item["text"] == a[1]:
				self.selections.remove(item)
				break				

	def on_title_name(self, *a, **k):
		self.ui_label.text = self.title_name
	
	def on_selections(self, *a, **k):
		'''
		Update TextInput.text after FileChoose.selection is changed
		via FileChoose.handle_selection.
		'''
		Logger.info(str(self.selections))

	def get_selection_paths(self):
		languges = ""
		file_dir = ""
		is_first = True
		for i in self.ui_content.children[0].children:
			if is_first:
				is_first = False
			else:
				languges = ',' + languges
				file_dir = ',' + file_dir
			languges = i.ui_text_field.text + languges
			file_dir = i.text + file_dir
		return languges, file_dir	

class Cell(MDBoxLayout):
	ui_text_field = ObjectProperty()
	text = StringProperty()
	origin_lang = StringProperty()
	pressed = ObjectProperty()

	def __init__(self,**kwargs):
		super().__init__(**kwargs)

	def on_origin_lang(self, *a, **ka):
		self.ids.id_language.text = self.origin_lang	

	def on_pressed(self, *a, **ka):
		self.ids.id_remove.bind(on_press = self.press_root)

	def press_root(self, *a):
		self.pressed(self, self.text)
	