import time

from .base_widget import BaseWidget
from .button import Button

class MainMenu(BaseWidget):
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets, max_players):
        super().__init__(parent_surface, x, y, w, h, colors, text_assets)
        
        self.layer = 0
        
        self.max_players = 6
        self.number_of_players = 1
        
        self.play_button = Button(self.surface, (self.w // 2) - 100, self.h // 4, 200, 75, self.colors, self.text_assets, self.text_assets["menu.play"], 40, self.colors.red, self.colors.white, self.colors.black)
        self.how_button = Button(self.surface, (self.w // 2) - 100, self.h // 2, 200, 75, self.colors, self.text_assets, self.text_assets["menu.how_to"], 40, self.colors.red, self.colors.white, self.colors.black)
        self.quit_button = Button(self.surface, (self.w // 2) - 100, round(self.h * 0.75), 200, 75, self.colors, self.text_assets, self.text_assets["menu.quit"], 40, self.colors.red, self.colors.white, self.colors.black)
        self.done_button = Button(self.surface, round(self.w * 0.75), round(self.h * 0.75), 200, 75, self.colors, self.text_assets, self.text_assets["menu.done"], 40, self.colors.red, self.colors.white, self.colors.black)
        
        self.left_arrow = Button(self.surface, (self.w // 4) - 100, self.h // 2, 50, 50, self.colors, self.text_assets, "<", 50, self.colors.red, self.colors.black, self.colors.white)
        self.right_arrow = Button(self.surface, round(self.w * 0.75) + 100, self.h // 2, 50, 50, self.colors, self.text_assets, ">", 50, self.colors.red, self.colors.black, self.colors.white)
        
        
    def draw(self):
        self.surface.fill(self.colors.black)
        
        self.text_display(self.text_assets["menu.title"], 40, self.colors.white, (self.w // 2, self.h // 8))
        
        if self.layer == 0:
            self.play_button.draw()
            self.how_button.draw()
            self.quit_button.draw()
            
            if self.how_button.is_pressed:
                self.layer = 1
                
            if self.play_button.is_pressed:
                self.layer = 2
                
        elif self.layer == 1:
            self.text_display(self.text_assets["menu.instructions"], 20, self.colors.white, (self.w // 2, self.h // 2))
            
            self.done_button.draw()
            if self.done_button.is_pressed:
                self.layer = 0
                
        elif self.layer == 2:
            self.text_display(self.text_assets["menu.player_prompt"], 30, self.colors.white, (self.w // 2, self.h // 4))
            
            self.left_arrow.draw()
            
            self.text_display(str(self.number_of_players), 40, self.colors.white, (self.w // 2, self.h // 2))
            
            self.right_arrow.draw()
            
            if self.left_arrow.is_pressed:
                if self.number_of_players > 1:
                    self.number_of_players -= 1
                time.sleep(0.1)
                
            if self.right_arrow.is_pressed:
                if self.number_of_players < self.max_players:
                    self.number_of_players += 1
                time.sleep(0.1)
                    
            self.done_button.draw()
            
        self.draw_to_parent()