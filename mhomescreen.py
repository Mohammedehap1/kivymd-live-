from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty
import threading 
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivy.core.window import Window
import datetime
from datetime import datetime
import calendar


Window.size = (350,700)
class MTextButton(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_text_color= "Custom"
        self.text_color= 0, 0, 1, 1





class Mlabel(MDLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_text_color= 'Custom'
        self.text = str(calendar.monthrange(datetime.now().year, datetime.now().month)[1])
        self.pos_hint = {'x':0,'y':.39}
        self.halign = 'center'
        




class top(MDTopAppBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        x = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.title= str(datetime.now().year) +"\\"+str(datetime.now().month)+'\\'+str(datetime.now().day)+'\\'+x[int(datetime.today().weekday())]
        self.type = 'top'
        self.anchor_title = 'center'
        self.pos_hint= {'top':1}
        self.left_action_items= [['menu',lambda x : x]]
        self.md_bg_color = (0.43, .035, .007)
        
        
        
        
    


class MCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_x = '.5'
        self.size_hint_y = '.5'
        self.md_bg_color ='black'
        


class Home_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(top())
        #self.add_widget(MCard())
        self.md_bg_color =.8,.8,.8,1
        self.add_widget(Mlabel())
        self.add_widget(MTextButton())
        
        
        
        