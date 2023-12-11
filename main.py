from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window
from mscreenmanager import MyApp


class MDlive(App,MDApp ):
    CLASSES = {
        "Home_Screen":"mhomescreen"  
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive':True})
    ]
    def build_app(self, First= False):
        print('lodsadasdaal')
        return Factory.Home_Screen()  
MDlive().run()