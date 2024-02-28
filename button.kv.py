from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button(text='Aperte o botão!',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      on_press=self.on_press_button)

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
