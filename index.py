from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Lanchonete(BoxLayout):
    total = NumericProperty(3)

    def adicionar_item(self, valor, ativo):
        if ativo:
            self.total += valor
        else:
            self.total -= valor

    def show_popup(self):
      popup = Popup(title='Compra realizada!', content=Label(text='Seu pedido foi realizado com sucesso!'), size_hint=(None,None), size=(400,400))
      popup.open()

class LanchoneteApp(App):
    def build(self):
      return Lanchonete()

if __name__ == '__main__':
    LanchoneteApp().run()
