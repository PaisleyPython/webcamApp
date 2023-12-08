# Boiler plate code (the code that we will always need when starting writing with a package type)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
import time

Builder.load_file('files/frontend.kv')

# =======================================
# By default the texture of camera is equal to the last frame


class CameraScreen(Screen):
    # A requirement from kivy
    def start(self):
        self.ids.camera.play = True
        self.ids.start_stop.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.start_stop.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f"images/{current_time}.png"
        self.ids.camera.export_to_png(filepath)
        self.manager.current = "image_screen"


class ImageScreen(Screen):
    # A requirement from kivi
    pass

# =====================================
# Boiler plate code continue:-


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

# Boiler plate code end:-
# ======================================
