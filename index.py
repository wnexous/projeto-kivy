from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class Lanchonete(BoxLayout):
    total = NumericProperty(3)

    def adicionar_item(self, valor, ativo):
        if ativo:
            self.total += valor
        else:
            self.total -= valor

class LanchoneteApp(App):
    def build(self):
        return Lanchonete()

if __name__ == '__main__':
    LanchoneteApp().run()
