import  os
import  threading
import datetime
import sys
from kivy.core.window import Window
from kivymd.app import  MDApp
from  kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButtonSpeedDial,MDIconButton 
from kivymd.uix.toolbar import MDTopAppBar
from  kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager 
from kivymd.toast import toast
from kivymd.uix.list import TwoLineIconListItem
from kivy.properties import ObjectProperty
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty, BooleanProperty, ObjectProperty
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget

from mhomescreen import Home_Screen
class MyApp(MDScreenManager):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(Home_Screen()) 
        

        print(self.current_screen) 
         

        
    


        
        
        