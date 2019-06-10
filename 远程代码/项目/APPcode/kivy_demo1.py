#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路

from kivy.app import App
from kivy.uix.button import Button

class HelloApp(App):
    def b(self):
        return Button(text='hello,kivy')
if __name__ == '__main__':
    HelloApp().run()