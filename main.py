from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time

class MyBox(BoxLayout):    
    def callback_eat(self):
        with open('eatingbubu.txt','a') as f1:
           f1.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '    qiabubu~\n')

    def callback_done(self):
        with open('eatingbubu.txt','a') as f1:
           f1.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '    qiahaole.\n')

    def callback_tunai(self):
        with open('eatingbubu.txt','a') as f1:
           f1.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '    tunaile!\n')


class WidgetsApp(App):
    def build(self):
        return MyBox()

if __name__ == "__main__":
    print 1
    WidgetsApp().run()

