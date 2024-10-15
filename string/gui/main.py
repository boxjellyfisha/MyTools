import kivy
kivy.require('2.3.0') # replace with your current kivy version !
# check the kivy version > $pip3.12 list | grep -i "kivy"

from kivymd.app import MDApp
from kivy.logger import Logger

import func.Menu as Menu
import func.DrawerNavigation as NV


from kivymd.uix.screen import MDScreen

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
                screen = Menu.HomeScreen(
                    name=name_screen,
                    radius=[18, 0, 0, 0],
                )
                screen.switch_screen = parent_menu.switch_screen
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