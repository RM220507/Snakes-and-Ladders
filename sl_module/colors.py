class ColorPalette:
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    dark_green = (1, 50, 32)
    brown = (150, 75, 0)
    
    purple = (255, 0, 255)
    yellow = (0, 255, 255)
    grey = (128, 128, 128)
    
    @property
    def player_color(self):
        return [self.red, self.green, self.blue, self.purple, self.yellow, self.grey]