from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class IpotekaApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Ipoteka!",halign='center')

IpotekaApp().run()