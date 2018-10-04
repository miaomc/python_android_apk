from kivy.app import App
from kivy.uix.accordion import Accordion
import time
from kivy.core.clipboard import Clipboard


class MyBox(Accordion):
    record_file = 'eatingbubu.txt'
    
    def callback_refresh(self):
        try:
            with open(self.record_file, 'r') as f1:
                lines = f1.readlines()
            lines.reverse()
            self.ids['my_list'].item_strings = ['\n']+lines
        except Exception, msg:
            self.ids['my_list'].item_strings = [str(msg)]

    def callback(self, status):
        try:
            with open(self.record_file, 'a') as f1:
                f1.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ ' , %s\n\n'%status)
        except Exception,msg:
            self.ids['btn_tn'].text = str(msg)

    def callback_copy(self):
        with open(self.record_file, 'r') as f1:
            tmp = f1.read()
        Clipboard.copy(tmp)

class WidgetsApp(App):
    def build(self):
        with open('eatingbubu.txt', 'a') as f1:
            f1.write('\n\n')
        return MyBox()

if __name__ == "__main__":
    WidgetsApp().run()

