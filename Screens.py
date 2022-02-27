from ast import Pass
from re import L
from tkinter.font import BOLD
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from random import randint
import webbrowser
import spoonacular as sp
import config
api = sp.API(config.api_key)


class FirstWindow(Screen):
    pass
class SecondWindow(Screen): 
    pass
class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    def changer(self, *args):
           self.manager.current = "second"
    
    def on_pre_enter(self, *args):
        self.dish_search(self.manager.ids.dish.ids.food_type.text)
        
    def dish_search(self,food_type):
        self.clear_widgets()
        self.logo = Image(
                    source = 'logo.png',
                    pos_hint={'center_x':0.5, 'center_y':0.9},
                    size_hint=(0.15,0.15),
                    )
        self.add_widget(self.logo)
        self.go_back_btn = Button(
                            text="Go back",
                            font_size=18,
                            bold= True,
                            pos_hint={'center_x':0.2, 'center_y':0.1},
                            size_hint=(0.3,0.1),
                            background_color= '#c77dff',
                            )
        
        self.go_back_btn.bind(on_release=self.changer)
        self.add_widget(self.go_back_btn)
        self.retry = Button(
                            text="Repick a dish",
                            font_size=18,
                            bold= True,
                            pos_hint={'center_x':0.8, 'center_y':0.1},
                            size_hint=(0.3,0.1),
                            background_color= '#c77dff',
                            )
        self.retry.bind(on_release=self.on_pre_enter)
        self.add_widget(self.retry)
        try:
            response = api.search_recipes_complex(food_type)
            data = response.json()
            print(len(data['results']))
            rand_dish = randint(0, len(data['results'])-1)
            print(rand_dish)
            self.response = Label(
                            text = data['results'][rand_dish]['title'],
                            pos_hint={'center_x':0.5, 'center_y':0.8},
                            font_size= 18
                            )
            self.add_widget(self.response)
            self.jpg_response = data['results'][rand_dish]['image']
            #print(self.jpg_response)
            self.add_widget(AsyncImage(
                            source=self.jpg_response,
                            pos_hint={'center_x':0.5, 'center_y':0.5}
                            ))
        except Exception:
            self.response = Label(
                            text = "Something went wrong, please try again.",
                            font_size= 18
                            )
            self.add_widget(self.response)

class FifthWindow(Screen):
    class WrappedLabel(Label):
            
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.bind(
                width=lambda *x:
                self.setter('text_size')(self, (self.width, None)),
                texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))
    
    def changer(self, *args):
        self.manager.current = 'third'
    
    def open_website(self, link):
        webbrowser.open(link)
    
    def on_pre_enter(self, *args):
        self.wine_paring(self.manager.ids.wine.ids.dish_type.text)
    
    def wine_paring(self, dish):
        self.clear_widgets()
        self.logo = Image(
                    source = 'logo.png',
                    pos_hint={'center_x':0.5, 'center_y':0.9},
                    size_hint=(0.15,0.15),
                    )
        self.add_widget(self.logo)
        self.go_back_btn = Button(
                            text="Go back",
                            font_size=18,
                            bold= True,
                            pos_hint={'center_x':0.2, 'center_y':0.1},
                            size_hint=(0.3,0.1),
                            background_color= '#c77dff',
                            )
        
        self.go_back_btn.bind(on_release=self.changer)
        self.add_widget(self.go_back_btn)
        self.wine_website = Button(
                             text="Website",
                             font_size=18,
                             bold= True,
                             pos_hint={'center_x':0.8, 'center_y':0.1},
                             size_hint=(0.3,0.1),
                             background_color= '#c77dff'
                             )
        self.add_widget(self.wine_website)
       
        try:
            response = api.get_wine_pairing(dish)
            data = response.json()
            print(data)
            self.paringInfo = self.WrappedLabel(
                            text = data['pairingText'],
                            size_hint=(0.75, None),
                            pos_hint={'center_x':0.5, 'center_y':0.7},
                            halign='center',
                            font_size= 14
                            )
            self.add_widget(self.paringInfo)
            
            if(len(data['productMatches'])!=0):
                self.recommendation = Label(
                                        text = data['productMatches'][0]['title'],
                                        font_size= 14,
                                        bold= True,
                                        pos_hint= {'center_x':0.5, 'center_y':0.58},
                                     )
                self.add_widget(self.recommendation)
                self.recommendation_description = self.WrappedLabel(
                                        text = data['productMatches'][0]['description'],
                                        size_hint=(0.75, None),
                                        pos_hint= {'center_x':0.5, 'center_y':0.5},
                                        halign='center',
                                        font_size= 14
                                     )
                self.add_widget(self.recommendation_description)
                #self.wine_url = data['productMatches'][0]['link']
                #print(self.wine_url)
                #self.wine_website.bind(on_click=print(self.wine_url))
            else:
                self.provideMoreInfo = Label(
                                text = "Please give more detailed information about your dish.",
                                font_size= 14,
                                bold= True,
                                pos_hint= {'center_x':0.5, 'center_y':0.5}
                                )
                self.add_widget(self.provideMoreInfo)
                
        except Exception:
            self.response = Label(
                            text = "Something went wrong, please try again.",
                            font_size= 18
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