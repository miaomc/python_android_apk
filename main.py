from kivy.app import App
from kivy.uix.accordion import Accordion
import time


class MyBox(Accordion):
    record_file = 'eatingbubu.txt'
    
    def callback_refresh(self):
        try:
            with open(self.record_file, 'r') as f1:
                lines = f1.readlines()
            self.ids['my_list'].item_strings = lines
        except Exception, msg:
            self.ids['my_list'].item_strings = [str(msg)]

    def callback(self, status):
        try:
            with open(self.record_file, 'a') as f1:
                f1.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ ' , %s\n\n'%status)
        except Exception,msg:
            self.ids['btn_tn'].text = str(msg)

class WidgetsApp(App):
    def build(self):
        with open('eatingbubu.txt', 'a') as f1:
            f1.write(time.strftime("\n %Y-%m-%d %H:%M:%S", time.localtime())+ ' start from here. \n\n')
        return MyBox()

if __name__ == "__main__":
    WidgetsApp().run()
