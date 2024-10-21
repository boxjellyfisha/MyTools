import kivy


kivy.require('2.3.0') # replace with your current kivy version !
# check the kivy version > $pip3.12 list | grep -i "kivy"

from kivymd.app import MDApp
from kivy.logger import Logger

import gui.Menu as Menu
import gui.DrawerNavigation as NV

from gui.Xml2Csv import Xml2CsvScreen
from gui.StrTransfor import StrTransforScreen
from gui.GroupingToCategory import GroupingToCategoryScreen

from kivymd.uix.screen import MDScreen

import os
os.environ["SDL_MOUSE_FOCUS_CLICKTHROUGH"] = '1'

class StringToolsApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Menu.MenuScreen() 

    def on_start(self):
        '''Creates application screens.'''
        parent_menu = self.root
        navigation_rail = parent_menu.ids.navigator_id
        navigation_rail.switch_screen = parent_menu.switch_screen

        navigation_rail_items = navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            name_screen = widget.text

            screen = None
            if name_screen == Menu.PAGE_MENU:
                screen = Menu.HomeScreen(name=name_screen)
                screen.switch_screen = parent_menu.switch_screen
            elif name_screen == Menu.PAGE_STR_TRANSLATOR:
                screen = StrTransforScreen(name=name_screen)
            elif name_screen == Menu.PAGE_XML_CSV:
                screen = Xml2CsvScreen(name=name_screen)  
            elif name_screen == Menu.PAGE_GROUPING_CATEGORY:
                screen = GroupingToCategoryScreen(name=name_screen)      
            else :
                screen = MDScreen(
                    name=name_screen,
                    radius=[18, 0, 0, 0],
                )   
            self.root.ids.screen_manager.add_widget(screen)

        parent_menu.switch_screen(Menu.PAGE_MENU)    
        Logger.info(f"hello start {navigation_rail.get_active_item()}")

if __name__ == '__main__':
    StringToolsApp().run()

# Package the main app: https://kivy.org/doc/stable/guide/packaging-osx.html#packaging-osx-sdk

# Selection 1: with buildozer
# pip install git+http://github.com/kivy/buildozer 
# cd /to/where/I/Want/to/package buildozer init

# (optional) for using python in virture machine:
# pip freeze > requirements.txt

# creates beautiful command-line interfaces
# pip install docopt==0.6.2

# a full-fledged subprocess replacement for Python 3.8 - 3.11, PyPy that allows you to call any program as if it were a function:
# pip install sh

# buildozer osx debug

# set the global python version as same as packaged pyhton version
# brew update && brew install pyenv
# pyenv global 3.12

# Selection 2: with pyinstaller
# pyinstaller -y --clean --windowed --name touchtracer \
#   --exclude-module _tkinter \
#   --exclude-module Tkinter \
#   --exclude-module enchant \
#   --exclude-module twisted \
#   /Users/kellyhong/Documents/tool/MyTools/string/main.py