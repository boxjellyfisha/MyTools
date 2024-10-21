import kivy
kivy.require('2.3.0')

from kivy.metrics import dp
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.snackbar import MDSnackbarSupportingText
from kivymd.uix.snackbar import MDSnackbarButtonContainer, MDSnackbarActionButton, MDSnackbarActionButtonText, MDSnackbarCloseButton

import subprocess

class Snackbar:
    output = None

    def show(self, content = "This is a snackbar!", output = None):
        self.output = output
        container = MDSnackbarButtonContainer(
                        MDSnackbarActionButton(
                            MDSnackbarActionButtonText(text="Open"),
                            on_press= self.open_file
                        ),
                        pos_hint={"center_y": 0.5}
                    ) if output else MDSnackbarButtonContainer()
        
        MDSnackbar(
            MDSnackbarSupportingText(text=content),
            container,
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def open_file(self, *a):
        if type(self.output) == str:
            subprocess.call(['open', self.output])