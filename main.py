# Boiler plate code (the code that we will always need when starting writing with a package type)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer
import webbrowser
import time

Builder.load_file('files/frontend.kv')

# =======================================
# By default the texture of camera is equal to the last frame


class CameraScreen(Screen):
    # A requirement from kivy
    def start(self):
        """Starts camera and changes button text"""
        self.ids.camera.play = True
        self.ids.camera.opacity = 1
        self.ids.start_stop.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera.texture

    def stop(self):
        """Stops camera and changes button text"""
        self.ids.camera.play = False
        self.ids.camera.opacity = 0
        self.ids.start_stop.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current date/time and captures
        and saves to the image folder. """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"App-4-Webcam-Photo-Sharer/images/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"
        # Accessing the source attribute of image widget
        self.manager.current_screen.ids.img.source = self.filepath

# self.ids gives access to the class where the code is written
# self.manager.current_screen.ids will give access to the widgets
# of the current screen.


class ImageScreen(Screen):
    # A requirement from kivi
    link_message = "Create link first!"

    def create_link(self):
        """ Create a link path for the captured image"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy link to the clipboard available for pasting"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Open link into the web browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


#
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
