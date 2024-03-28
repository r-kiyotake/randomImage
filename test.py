from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('c:\Windows\Fonts')
LabelBase.register(DEFAULT_FONT, 'HGRGY.TTC')

class TestApp(App): #Appの継承
    pass

if __name__=='__main__':
    TestApp().run()