from kivy.config import Config
Config.set('graphics', 'width', '640') #横幅
Config.set('graphics', 'height', '480') #縦幅

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

# デフォルトに使用するフォントを変更する
resource_add_path('c:\Windows\Fonts')
LabelBase.register(DEFAULT_FONT, 'HGRGE.TTC')

resource_add_path('./image')

class ImageWidget(Widget):
    source = StringProperty('./image/000001.jpg')

    def __init(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.source='./image/000001.jpg'

    def buttonRandom(self):
        self.source= f'00000{randint(1,9)}.jpg'

class CatApp(App):
    def __init(self, **kwargs):
        super(CatApp, self).__init__(**kwargs)
        self.title = '好きな画像'

if __name__=='__main__':
    CatApp().run()