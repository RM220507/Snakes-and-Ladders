import pygame

from .base_widget import BaseWidget

class Board(BaseWidget):
    def __init__(self, parent_surface, x, y, w, h, colors, text_assets, row_count, column_count):
        super().__init__(parent_surface, x, y, w, h, colors, text_assets)
        
        self.column_count = column_count
        self.row_count = row_count
        
        self.column_width = self.w // self.column_count
        self.row_height = self.h // self.row_count

        self.grid = self.gen_grid()
        
    def gen_grid(self):
        grid = []
        for row_num in range(self.row_count):
            row = [i for i in range((row_num * self.column_count) + 1, (row_num * self.column_count) + self.column_count + 1)]

            if row_num % 2 == 1:
                row.reverse()
                
            grid.append(row)

        grid.reverse()
        return grid
    
    def draw(self, players, snakes_ladders):
        self.surface.fill(self.colors.black)
        
        for i in range(0, 8):
            pygame.draw.line(self.surface, self.colors.white, (i * self.column_width, 0), (i * self.column_width, self.h))

        for i in range(0, 8):
            pygame.draw.line(self.surface, self.colors.white, (0, i * self.row_height), (self.w, i * self.row_height))

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                self.text_display("%02d" % cell, 10, self.colors.white, ((j * 50) + 25, (i * 50) + 25))

        self.draw_snakes_ladders(snakes_ladders)
        self.draw_players(players)

        self.draw_to_parent()
        
    def draw_snakes_ladders(self, snakes_ladders):
        for snake in snakes_ladders.snakes:
            start_coord, end_coord = self.line_coord_from_snake_ladder(snake.start, snake.end)
            
            pygame.draw.line(self.surface, self.colors.dark_green, start_coord, end_coord, 4)
            
        for ladder in snakes_ladders.ladders:
            start_coord, end_coord = self.line_coord_from_snake_ladder(ladder.start, ladder.end)
            
            pygame.draw.line(self.surface, self.colors.brown, start_coord, end_coord, 4)
    
    def line_coord_from_snake_ladder(self, start, end):
        start_row, start_col = self.grid_pos(start)
            
        x1 = start_col * self.column_width - (self.column_width // 2)
        y1 = (self.row_count - start_row) * self.row_height - (self.row_height // 2)
            
        end_row, end_col = self.grid_pos(end)
            
        x2 = end_col * self.column_width - (self.column_width // 2)
        y2 = (self.row_count - end_row) * self.row_height - (self.row_height // 2)
    
        return (x1, y1), (x2, y2)
    
    def draw_players(self, players):
        for player in players:
            row, column = self.grid_pos(player.pos_index)

            pygame.draw.circle(self.surface, player.color, (column * self.column_width - (self.column_width // 2), (self.row_count - row) * self.row_height - (self.row_height // 2)), 20 - (player.id * 2))
            
    def grid_pos(self, pos_index):
        row = (pos_index - 1) // self.row_count

        if row % 2 == 0:
            column = ((pos_index - 1) % self.column_count) + 1
        else:
            column = self.column_count - (pos_index - 1) % self.column_count

        return row, column