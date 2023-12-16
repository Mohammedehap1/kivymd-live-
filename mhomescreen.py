import kivy.uix.floatlayout
import kivymd.app
import kivymd.uix.boxlayout
import kivymd.uix.fitimage
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button
import kivymd.uix.textfield
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
import threading 
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton , BaseButton , MDFlatButton
from kivy.core.window import Window
import datetime
from datetime import datetime
import calendar
from kivymd.uix.chip import MDChip
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDList , ThreeLineListItem,BaseListItem,ImageLeftWidget,OneLineAvatarListItem,ILeftBodyTouch
from kivymd.uix.widget import MDWidget
from kivymd.uix.imagelist import MDSmartTile
from kivy.uix.image import Image
from kivymd.uix.widget import Widget
from kivymd.uix.fitimage import FitImage


class secoencard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = (1,.8,0,1)
        self.pos_hint={'x':.32,'y':.1}
        self.radius = 12
        self.size_hint = (None,.27)
        self.padding = 4
        self.add_widget(MDLabel(text = 'sesson_num'))

class Md_Floatlayout(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = 0,0,0,0
        self.add_widget(Mimage(source = '1.jpg'))
        self.radius = 16
        self.add_widget(MDLabel(text='anime_name',pos_hint = {'x':.32,'y':.35}))
        self.add_widget(secoencard())
        self.add_widget(MDLabel(text='time_update',pos_hint = {'x':.76,'y':-.4}))

        

class Mimage (FitImage):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.pos_hint = {"x":0,'y':0}
        self.size_hint =[x/x*.3,1]
        self.radius = 12    
        
        
        


Window.size = (408,952)
(x,y) = Window.size

class smart(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text='lol'
        self.orientation = "horizontal"
        self.md_bg_color = .2,.2,.2,1
        self.col_instruction = 2
        self.size_hint = (1,1)
        self.radius = 16
        
        
        
        self.add_widget(Md_Floatlayout())

class M_List(MDList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = 0,2,0,0
        self.spacing = 10
        self.size_hint_x = 1
        for i in range(10):
            self.size_hint_y = i/5
            self.add_widget(smart())
        
        #self.add_widget(card())
        
        
        
        
        
        
        




#______________________________________

#_______________________________

class Scroll_View(ScrollView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.do_scroll_x: False
        self.do_scroll_y: True
        self.md_bg_color = 0,0,0,0
        self.size_hint_y = y/y*.9
        
        self.add_widget(M_List())
        
        
        

#_____________________________
class Top_App_Bar(MDTopAppBar): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = .2,.2,.2,1
        self.type = 'top'
        self.pos_hint= {'top':1}
        self.size_hint_y = y/y*.1
#______________________________
class Home_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color =0,0,0,.9
        self.add_widget(Scroll_View()) 
        self.add_widget(Top_App_Bar()) 
        
print(Window.size)
        
        
        
        