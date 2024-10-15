import kivy
kivy.require('2.3.0')

from kivymd.uix.navigationrail import MDNavigationRail  
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.logger import Logger


from func.pages import PAGE_MENU, PAGE_STR_TRANSLATOR, PAGE_XML_CSV, PAGE_GROUPING_CATEGORY

class DrawerNavigation(MDNavigationRail):
    switch_screen = ObjectProperty()
    current_page = ""

    def __init__(self, **kwargs):
        super(DrawerNavigation, self).__init__(**kwargs)

    def get_item(self, page_name):
        items = self.get_items().copy()
        required_item = None
        for item in items:
            if item.text == page_name:
                required_item = item
                break
        Logger.info(f"get_item : {required_item.text if required_item else "none"}")
        return required_item


    def get_active_item(self):
        items = self.get_items().copy()
        active_item = None
        for item in items:
            if item.active:
                active_item = item
                break
        Logger.info(f"get_active_item : {active_item.text if active_item else "none"}")    
        return active_item
    
    def active_page(self, page_name):
        if self.current_page == page_name:
            return
        
        Logger.info("active_page" + page_name)

        active_item = self.get_active_item()  
        if active_item == None or active_item.text != page_name:
            required = self.get_item(page_name)
            self.set_active_item(required)

    def switch_item(self, page_name):
        if self.current_page == page_name:
            return
        current = self.get_item(page_name=page_name)
        if not current.active:
            return
        
        self.current_page = page_name
        Logger.info(f"switch_item {page_name}, {self.get_active_item().text if self.get_active_item() else "None"}, c= {self.current_page}")
        self.switch_screen(page_name)

class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()