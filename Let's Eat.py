from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LetsEat(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.introduction = Label(
                        text= "Have you ever had a problem with coming up with a recepie for dinner \n or maybe you had a problem with choosing a wine fitting the dish you've made? ",
                        font_size=18,
                        font_family="Comic Sans MS",
                        color= '#c77dff',
                        halign="center",
                        valign="middle",
                        )
        self.window.add_widget(self.introduction)
        
        self.introduction2 = Label(
                        text= " If so this app is perfect for you.",
                        font_size=18,
                        font_family="Comic Sans MS",
                        italic=True,
                        bold=True,
                        color= '#c77dff',
                        halign="center",
                        valign="middle",
                        )
        self.window.add_widget(self.introduction2)
        

        # button widget
        self.button_dish = Button(
                      text= "DISH",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#c77dff',
                      )
        self.button_dish.bind(on_press=self.callback)
        self.window.add_widget(self.button_dish)

        self.button_wine = Button(
                      text= "WINE",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#c77dff',
                      )
        self.button_wine.bind(on_press=self.callback)
        self.window.add_widget(self.button_wine)
        
        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        print("Hello")

# run Say Hello App Calss
if __name__ == "__main__":
    LetsEat().run()