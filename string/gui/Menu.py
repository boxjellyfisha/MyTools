import kivy
kivy.require('2.3.0')

# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ColorProperty
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from .pages import PAGE_MENU,PAGE_STR_TRANSLATOR,PAGE_XML_CSV,PAGE_GROUPING_CATEGORY

class MenuScreen(FloatLayout): # inherent FloatLayout
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    navigator = ObjectProperty()
    label_wid = ObjectProperty() # declare the member variables

    def switch_screen(self, page_name):
        self.label_wid.text = 'Run ' + page_name
        self.navigator.active_page(page_name)
        self.ids.screen_manager.current = page_name

    def __init__(self, **kwargs): # initialized this class when the class instantiated
        super(MenuScreen, self).__init__(**kwargs)

        # dynamic create UI in pyhton...
        # self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text='password'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)


class HomeScreen(MDScreen): 
    switch_screen = None

    def __init__(self, **kwargs): # initialized this class when the class instantiated
        super(HomeScreen, self).__init__(**kwargs)

    def do_str_translator(self):
        self.switch_screen(PAGE_STR_TRANSLATOR)

    def do_xml2csv(self):
        self.switch_screen(PAGE_XML_CSV)

    def do_grouping_to_category(self):
        self.switch_screen(PAGE_GROUPING_CATEGORY)
