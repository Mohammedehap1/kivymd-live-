from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window




class MDlive(App,MDApp ):
    CLASSES = {
        "Home_Screen":"mhomescreen"  
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive':True})
    ]
    def build_app(self, First= False):
        return Factory.Home_Screen()  
MDlive().run()