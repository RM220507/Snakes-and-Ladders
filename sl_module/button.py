import pygame

from .base_widget import BaseWidget

class Button(BaseWidget):
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets, text, font_size, text_col, bg_col, hover_col):
        super().__init__(parent_surface, x, y, w, h, colors, text_assets)
        
        self.text = text
        self.font_size = font_size
        self.text_col = text_col
        
        self.bg_col = bg_col
        self.hover_col = hover_col
    
    @property
    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        return self.x < mouse_x < self.x + self.w and self.y < mouse_y < self.y + self.h
    
    @property
    def is_pressed(self):
        left_click = pygame.mouse.get_pressed()[0]
        
        return self.is_hovered and left_click
    
    def draw(self):
        if self.is_hovered:
            self.surface.fill(self.hover_col)
        else:
            self.surface.fill(self.bg_col)
        
        self.text_display(self.text, self.font_size, self.text_col, (self.w // 2, self.h // 2))
        
        self.draw_to_parent()