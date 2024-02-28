from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button(text='Pressione-me', on_press=self.on_press_button)

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
