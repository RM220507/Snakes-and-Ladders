from .base_widget import BaseWidget

class GameUI(BaseWidget):
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets):
        super().__init__(parent_surface, x, y, w, h, colors, text_assets)
        
        self.announce_text = ""
        self.prompt_text = ""
        
    def draw(self):
        self.surface.fill(self.colors.black)
        
        self.text_display(self.announce_text, 20, self.colors.white, (self.w // 2, self.h // 3))
        self.text_display(self.prompt_text, 20, self.colors.white, (self.w // 2, round(self.h * 0.75)))

        self.draw_to_parent()