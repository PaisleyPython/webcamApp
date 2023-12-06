# Boiler plate code (the code that we will always need when starting writing with a package type)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer

Builder.load_file('frontend.kv')

# =====================================================================================================


class CameraScreen(Screen):
    # A requirement from kivi
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    # A requirement from kivi
    pass


# ==================================================================================================
# Boiler plate code continue:-

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

# Boiler plate code end:-
# ==================================================================================================
