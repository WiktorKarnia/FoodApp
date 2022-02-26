from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import spoonacular as sp
import config
api = sp.API(config.api_key)


class FirstWindow(Screen):
    pass

class SecondWindow(Screen): 
    def changer(self, *args):
       self.manager.current = 'first'
    
    def dish_search(self,food_type):
        self.clear_widgets()
        self.go_back_btn = Button(
                            text="Go back",
                            font_size=32,
                            pos_hint={'center_x':0.5},
                            size_hint=(0.5,0.5),
                            background_color= '#c77dff'
                            )
        
        self.go_back_btn.bind(on_release=self.changer)
        self.add_widget(self.go_back_btn)
        try:
            response = api.search_recipes_complex(food_type)
            data = response.json()
            print(data)
            self.response = Label(
                            text = data['title'][1],
                            font_size= 18,
                            color= '#00FFCE'
                            )
            self.add_widget(self.response)
            self.jpg_response = data['image'][0]
            self.add_widget(Image(source=self.jpg_response)) #idk why it won't work ;-; but at least wine works for now 
        except Exception:
            self.response = Label(
                            text = "Something went wrong, please try again.",
                            font_size= 18,
                            color= '#00FFCE'
                            )
            self.add_widget(self.response)
    
class ThirdWindow(Screen):
    def changer(self, *args):
        self.manager.current = 'first'
    
    def wine_description(self, wine_name):
        self.clear_widgets()
        self.go_back_btn = Button(
                            text="Go back",
                            font_size=32,
                            pos_hint={'center_x':0.5},
                            size_hint=(1,0.5),
                            background_color= '#c77dff'
                            )
        
        self.go_back_btn.bind(on_release=self.changer)
        self.add_widget(self.go_back_btn)
        try:
            response = api.get_wine_description(wine_name)
            data = response.json()
            print(data['wineDescription'])
            self.response = Label(
                            text = data['wineDescription'],
                            font_size= 18,
                            color= '#00FFCE'
                            )
            self.add_widget(self.response)
        except Exception:
            self.response = Label(
                            text = "Something went wrong, please try again.",
                            font_size= 18,
                            color= '#00FFCE'
                            )
            self.add_widget(self.response)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class DishApp(App):
    def build(self):
        return kv
        
if __name__ == "__main__":
    DishApp().run()