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



class card(MDCard):
  pass

    
      
  




class Demo(MDApp):
    def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            Window.bind(on_keyboard=self.events)
            self.manager_open = False
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path,)
            self.file_manager.current_path=('/storage/emulated/0/Download/')
            self.s_file=None
            self.theme_cls.theme_style =("Dark")
            
            self.theme_cls.primary_palette = "BlueGray"
            self.home=MDScreenManager()
            self.menu= MDScreen(name='menu')
            self.q_data ={}
            self.down_but=None
            self.get_url = None
            self.qu = None
            self.down_hint =None
            self.tite = None
            self.thumbnail = None
            self.resolution = StringProperty('Loading')
            self.download_icon = StringProperty('download')
            self.length = StringProperty('Loading')
            self.file_size = StringProperty('Loading')
            self.download = BooleanProperty(False)
    
    
    def build(self):
         self.get_url=self.get_url= MDTextField(hint_text= 'enter your link',
            pos_hint=({'center_x': .4, 'center_y': .73}),
            size_hint_x=(.5),
            icon_right=('link'))
            
         se_but = MDIconButton(icon='magnify',
            pos_hint=({'center_x':.8,'center_y':.73}),
            on_release=self.t_s_link)
            
         self.t_bar=MDTopAppBar(
            title= 'Bytube',
            icon= 'youtube',
            left_action_items= [["menu", lambda x: x]],
            right_action_items=[['cog', self.go_settings]],
            size_hint_y=(.08),
            type= 'top',
            pos_hint={'x':0,'y':.93})

         
            
         self.down_but = MDFloatingActionButtonSpeedDial(icon='download',
         root_button_anim = True,
         )
         self.down_hint=MDProgressBar(pos_hint={'x':0,'y':.5},max=100,running_duration = 1)
         #card edit 
         self.card = MDCard(size_hint_x=.9,size_hint_y=.4,
         pos_hint={'center_x':.50,'y':.25},
         )
         
         self.online_img=AsyncImage(
         size_hint_y=.4,
         pos_hint={'center_y':.8})
         self.size_label = MDLabel(text ='shjdjfjfjfjd',
         size_hint_x=.6,size_hint_y =.1,
         pos_hint={'center_x':.1,'center_y':.4}
         
         )
        
         
         
         #settings screen 
         self.settings=MDScreen(name='settings')
         self.settings_list=TwoLineIconListItem(text='download save location',
         secondary_text=self.file_manager.current_path,
         pos_hint=({'x':0,'center_y':.90}),
         on_press = self.file_manager_open,
         
         
         )
         
         
         
         
         
         
         
         
         #add_widget
         self.home.add_widget(self.menu)
         self.menu.add_widget(self.get_url)
         self.menu.add_widget(self.down_but)
         self.menu.add_widget(self.t_bar)
         self.menu.add_widget(se_but)
         self.settings.add_widget(self.settings_list)
         self.menu.add_widget(self.down_hint)
         self.menu.add_widget(self.card)
         self.card.add_widget(self.online_img)
         self.card.add_widget(self.size_label)
         return self.home
         
         
         
    def func(self,*args):
          self.down_but.data=self.q_data
    def events(self, instance, keyboard, keycode, text, modifiers,*args,**kwargs):
         if keyboard in (1001, 27):
             if self.manager_open:
                 self.file_manager.back()
             if 'settings' in f'{self.home.current_screen}':
                 self.go_menu()
         return True
    #app func and style 
    
        
    def go_settings(self,*args):
         self.home.switch_to(self.settings,direction='left')
         self.menu.remove_widget(self.t_bar)
         self.t_bar.left_action_items=[['arrow-left',self.go_menu]]
         self.t_bar.right_action_items = []
         self.settings.add_widget(self.t_bar)
    
         
         
    def down(self,*args):
             self.menu.add_widget(MDLabel(text=f'{self.file_manager.current_path}'))
    def go_menu(self,*args):
         self.home.switch_to(self.menu,direction="right")
         self.settings.remove_widget(self.t_bar)
         self.t_bar.left_action_items= [["menu", lambda x: x]]
         self.t_bar.right_action_items=[['cog', self.go_settings]]
         self.menu.add_widget(self.t_bar)
       
    # file_manager func ,, done 💯
    def file_manager_open(self,*args):
        self.file_manager.show(self.file_manager.current_path)
    def select_path(self, path: str):
        self.exit_manager()
        toast(path)
        self.settings_list.secondary_text = self.file_manager.current_path
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def save_file(self,*args):
        try:
           sys.path.append('/storage/emulated/0/Bytube')
           import config
        except:
          os.mkdir('/storage/emulated/0/Bytube')
          cfg = open('/storage/emulated/0/Bytube/config','w+')
          cfg.close()
          sys.path.append('/storage/emulated/0/Bytube')
          import config
        
        
        return  None
        
        
        
        
        
        
        
        
        
        
        
        
        #pytube func 
    def get_data(self,*args):
            self.title = self.video.title
            self.thumbnail = str(self.video.thumbnail_url)
            self.online_img.source = self.thumbnail
            #self.length = str(datetime.timedelta(seconds=self.video.length))
            #self.file_size = size(self.video.streams.get_audio_only().filesize)
            self.size_label.text = self.file_size
        
    def progress_func(self, stream, chunk, bytes_remaining):
        value = round((1 - bytes_remaining / stream.filesize) * 100, 3)
        
        self.down_hint.value = value
        
        
        
    def s_link(self,*args):
         link_error = False
         self.url=self.get_url.text
         self.get_url.helper_text =''
         try:
             self.video=YouTube(self.url,on_progress_callback=self.progress_func)
         except:
             self.get_url.helper_text='invite link'
             link_error= True
         if link_error == False:
             self.get_lin_stream()
             self.get_data()
        
        
        
        
        
    def get_lin_stream(self,*args):
      text=f'{self.video.streams.filter(progressive=True)}'
      alist=text.split()
      res_list=[r[5:-1] for r in alist if r.startswith('res') ]
      if '144p' in res_list:
        self.q_data.update({'144p':['download','on_press',self.t_144p]})
        self.qu='144p'
      if '240' in res_list:
        self.q_data.update({'240p':['download','on_press',self.t_240p]})
        self.qu='240p'
      if '360p' in res_list:
        self.q_data.update({'360p':['download','on_press',self.t_360p]})
        self.qu = '360p'
      if '480p' in res_list:
        self.q_data.update({'480p':['download','on_press',self.t_480p]})
        self.qu= '480p'
      if '720p' in res_list:
        self.q_data.update({'720p':['download','on_press',self.t_720p]})
        self.qu= '720p'
      if '1080p' in res_list:
        self.q_data.update({'1080p':['download','on_press',self.down_1080p]})
        self.qu = '1080p'
      self.q_data.update({'music':['download','on_press',self.down_m]})
      self.func()
      
      
  #threading func
  
      
      
    def t_s_link(self,*arga):
      threading.Thread(target=self.s_link).start()
      
    def t_144p(self,*arga):
      threading.Thread(target=self.down_144p).start()
    def t_240p(self,*args):
      threading.Thread(target=self.down_240p).start()
    def t_360p(self,*args):
      threading.Thread(target=self.down_360p).start()
    def t_480p(self,*args):
      threading.Thread(target=self.down_480p).start()
    def t_720p(self,*args):
      threading.Thread(target=self.down_720p).start()
    def t_1080p(self,*args):
      threading.Thread(target=self.down_1080p).start()
    def t_m(self,*args):
      threading.Thread(target=self.down_m).start()
    
    
    def down_144p(self,*args):
      self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_240p(self,*args):
      self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_360p(self,*args):
      self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_480p(self,*args):
      self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_720p(self,*args):
      self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_1080p(self,*args):
     self.video.streams.filter(progressive=True,res=self.qu).order_by('resolution').desc().first().download(self.file_manager.current_path)
    def down_m(self,*args):
      self.video.streams.get_audio_only().download(output_path=self.file_manager.current_path)
      #os.rename(self.file_manager.current_path+self.video.title+'.mp4',self.file_manager.current_path+self.video.title+'.mp3')
if __name__=='__main__':
    Demo().run()
    
    
    
    