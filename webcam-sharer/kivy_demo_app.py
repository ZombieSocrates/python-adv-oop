from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




class FirstScreen(Screen):

    def search_image(self):
        pass


class RootWidget(ScreenManager):

    pass



class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":


    Builder.load_file("kivy_demo_frontend.kv")
    MainApp().run()