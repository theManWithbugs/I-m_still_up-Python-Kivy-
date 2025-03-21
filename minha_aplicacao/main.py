from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_image = 'cenario1.webp'  
        self.background_texture = CoreImage(self.background_image).texture

        self.character_x = 100
        self.character_y = 200
        self.character_width = 50
        self.character_height = 50
        self.character_texture = CoreImage('persongame_right.png').texture 
        
        with self.canvas:
            self.background = Rectangle(texture=self.background_texture, pos=(0, 0), size=self.size)

            self.character = Rectangle(texture=self.character_texture, pos=(self.character_x, self.character_y),
                                       size=(self.character_width, self.character_height))

     
        self.bind(size=self.update_background_size)

        
        self.keys_pressed = set()
        Window.bind(on_key_down=self.on_key_down, on_key_up=self.on_key_up)

        
        Clock.schedule_interval(self.update, 1 / 60)

    def update_background_size(self, *args):
        
        self.background.size = self.size

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        
        self.keys_pressed.add(key)

    def on_key_up(self, window, key, scancode):
        
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def update(self, dt):
        
        if 276 in self.keys_pressed:  # Tecla seta para a esquerda
            self.character_x -= 5
            self.character.texture = CoreImage('persongame_left.png').texture  # Atualiza a textura diretamente
        if 275 in self.keys_pressed:  # Tecla seta para a direita
            self.character_x += 5
            self.character.texture = CoreImage('persongame_right.png').texture  # Atualiza a textura diretamente
        if 273 in self.keys_pressed:  # Tecla seta para cima
            self.character_y += 5
        if 274 in self.keys_pressed:  # Tecla seta para baixo
            self.character_y -= 5

        # Atualiza a posição do personagem
        self.character.pos = (self.character_x, self.character_y)

class SimpleGameApp(App):
    def build(self):
        return GameWidget()

if __name__ == "__main__":
    SimpleGameApp().run()
