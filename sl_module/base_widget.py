import pygame

class BaseWidget:
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets):
        self.parent_surface = parent_surface
        
        self.x = x
        self.y = y
        
        self.w = w
        self.h = h
        
        self.colors = colors
        self.text_assets = text_assets
        
        self.surface = self.setup_surface()
        
    def setup_surface(self):
        surface = pygame.Surface((self.w, self.h))
        return surface
    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def text_display(self, text, font_size, color, pos):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        TextSurf, TextRect = self.text_objects(text, font, color)
        TextRect.center = pos
        self.surface.blit(TextSurf, TextRect)
        
    def draw_to_parent(self):
        self.parent_surface.blit(self.surface, (self.x, self.y))