import kivy

kivy.require('2.3.0')

from kivy.properties import StringProperty, ListProperty, ObjectProperty, ReferenceListProperty
from kivymd.uix.screen import MDScreen

from kivy.clock import Clock
from kivy.logger import Logger

from cmd import grouping_to_category as group
from gui.snackbar_hint import Snackbar

class GroupingToCategoryScreen(MDScreen): 
	'''
	exercute the command:
	# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/groupingToCategory.py \
	# --source /Users/kellyhong/Documents/workspace/android_vms/app/src/main/res/values/strings.xml \
	# --output /Users/kellyhong/Documents/tool/MyTools/en/vms_2024_20_14.xlsx \
	# --rules /Users/kellyhong/Documents/workspace/android_modula/library/ui/src/main/res/values/strings.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/errors_setting.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/errors.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/event_type_strings.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/notification_strings.xml
	# -s
	# -o
	'''

	callback = None
	hint = Snackbar()

	def __init__(self, *args, **kwargs):
		super(GroupingToCategoryScreen, self).__init__(*args, **kwargs)
		self.callback = Clock.create_trigger(self.exercute, 0.2)
	
	def transfor(self):
		if not self.callback:
			return
		self.callback()
	
	def exercute(self, *args):
		file_dir = self.ids.id_file_dir.selections[0]
		languges, rules = self.ids.id_rule_files.get_selection_paths()
		is_csv = self.ids.id_is_csv.isChecked()
		is_show_old = self.ids.id_is_show_old.isChecked()
		export_dir = self.ids.id_export_dir.selections[0] + '/output_grouping' 
		export_dir += '.csv' if is_csv else '.xlsx'
		is_sorted = self.ids.id_is_sorted.isChecked()

		Logger.info("try..." + str(file_dir) + "; " + str(rules) + "; " + str(export_dir) + "; " + str(is_sorted) + str(is_show_old))
		try:
			group.trans(sorce_file_path = file_dir, 
			   output_file_path= export_dir, 
			   rules=rules.split(","), 
			   is_sort_by_alphabet=is_sorted, 
			   is_show_old_value=is_show_old)
			self.hint.show(content="File generating is success!", output = export_dir)
		except Exception as e:
			Logger.error(e)
			self.hint.show(content="Failed by: " + str(e))
	