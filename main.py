from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        orientation: "vertical"
        MDTopAppBar:
            title: "EEE-MIU"
            md_bg_color: app.theme_cls.accent_color
            elevation: 2
            
    MDTextField:
        hint_text: "Search Here"
        helper_text: "EEE-Day"
        mode: "round"
        max_text_length: 15
        pos_hint:{'center_x':0.5, 'center_y': 0.8}
        helper_text_mode: "on_focus"
        
    MDRoundFlatButton:
        text: "Search"
        text_color: "white"
        md_bg_color: app.theme_cls.accent_color
        pos_hint:{'center_x':0.5, 'center_y': 0.7}   
        
    Image:
        id: "routine"
        size_hint_x: 0.7
        size_hint_y: 0.7
        pos_hint:{'center_x':0.5, 'center_y': 0.4} 
        source: "img.png"
        
                
    MDRaisedButton :
        id: 'Class_btn'
        text: 'Class'
        pos_hint:{'center_x':0.3, 'center_y': 0.1} 
        md_bg_color: app.theme_cls.accent_color
        elevation: 2
        
    
    MDRaisedButton:
        id: 'Subject_btn'
        text: 'Subject'
        pos_hint:{'center_x':0.7, 'center_y': 0.1} 
        md_bg_color: app.theme_cls.accent_color
        elevation: 2
        

'''


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvscreen = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvscreen)
        return screen

myapp = MainApp()

myapp.run()
