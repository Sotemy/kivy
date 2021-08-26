from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout


def get_ingridients(m):
    nitro=str(10 * m / 1000)
    salt=str(15 * m / 1000)
    starts=str(0.5 * m / 1000)
    sugar=str(5 * m / 1000)
    time=str(round(m / 500 * 2))

    return {'salt': salt, 
            'nitro': nitro, 
            'starts': starts, 
            'sugar': sugar, 
            'time': time}

class Container(GridLayout):
    
    def calculate(self):
        try:
            mass=int(self.text_input.text)
        except:
            mass=0

        i = get_ingridients(mass)

        self.salt.text = i.get('salt') + ' +5'
        self.nitro.text = i.get('nitro')
        self.starts.text = i.get('starts')
        self.sugar.text = i.get('sugar')
        self.time.text = i.get('time')

class MyApp(MDApp):
    title='Q Recepie'
    def build(self):
        def __init__(**kwargs):
            self.theme_cls.theme_style = "Light"
            super().__init__(**kwargs)
        return Container()

if __name__ == '__main__':
    MyApp().run()
        