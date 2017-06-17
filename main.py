from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.storage.jsonstore import JsonStore


    
class CustomWidget(Widget):
    pass

class CustomFloatLayout(FloatLayout):
    def getlevel(self):
        store = JsonStore('mystore.json')
        if store.exists('p1'):
            return store.get('p1')['level']
        else:
            return '0'
    
    def dosomething(self):
        store = JsonStore('mystore.json')
        self.ids.lbl.text = str(int(self.ids.lbl.text)+1)
        store['p1'] = {'level':self.ids.lbl.text}
        print store['p1']['level']

class MyApp(App):
    def on_pause(self,*args):
        return True
    def build(self):
        return CustomFloatLayout()

if __name__ == '__main__':
    MyApp().run()
