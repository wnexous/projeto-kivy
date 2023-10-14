from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.popup import Popup


class Lanchonete(BoxLayout):
    total = NumericProperty(3)
    itens = ListProperty([])

    def adicionar_item(self, valor, ativo, item):
        if ativo:
            self.total += valor
            if item not in self.itens:
                self.itens.append(item)
        else:
            self.total -= valor
            if item in self.itens:
                self.itens.remove(item)

    def show_popup(self):
        forma_pagamento = self.ids.spinner_pagamento.text
        popup = Popup(title='Compra realizada!', content=Label(text='Seu pedido foi realizado com sucesso!\nOs itens do seu sanduíche são: \n\n' + '\n'.join(
            self.itens) + '\n\nForma de pagamento escolhida foi: ' + forma_pagamento + f"\n\nVALOR TOTAL: {self.total},00"), size_hint=(None, None), size=(400, 400))
        popup.open()
        self.itens = []


class LanchoneteApp(App):
    def build(self):
        return Lanchonete()


if __name__ == '__main__':
    LanchoneteApp().run()
