from .base_widget import BaseWidget
from .button import Button

class EndDisplay(BaseWidget):
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets, winning_player):
        super().__init__(parent_surface, x, y, w, h, colors, text_assets)
        
        self.winning_player = winning_player
        
        self.quit_button = Button(self.surface, (self.w // 2) - 100, round(self.h * 0.75), 200, 75, self.colors, self.text_assets, self.text_assets["menu.quit"], 40, self.colors.red, self.colors.white, self.colors.black)
        self.menu_button = Button(self.surface, (self.w // 2) - 100, self.h // 2, 200, 75, self.colors, self.text_assets, self.text_assets["menu.main_menu"], 40, self.colors.red, self.colors.white, self.colors.black)
        
    def draw(self):
        self.surface.fill(self.colors.black)
        
        self.text_display(self.text_assets["menu.title"], 40, self.colors.white, (self.w // 2, self.h // 8))
        
        self.text_display(self.text_assets["play.won"] % (self.winning_player.id), 30, self.winning_player.color, (self.w // 2, self.h // 4))
        
        self.quit_button.draw()
        self.menu_button.draw()
        
        self.draw_to_parent()