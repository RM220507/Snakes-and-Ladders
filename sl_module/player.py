import random

class Player:
    def __init__(self, id, color, row_count, column_count):
        self.id = id
        self.pos_index = 1
        
        self.required_dest = 1
        
        self.color = color
        
        self.row_count = row_count
        self.column_count = column_count
        
    def roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        
        if dice_1 == dice_2:
            self.required_dest = self.clamp(self.pos_index - (dice_1 + dice_2))
        else:
            self.required_dest = self.clamp(self.pos_index + (dice_1 + dice_2))
            
        return dice_1, dice_2
            
    def clamp(self, n):
        if n < 1:
            return 1
        elif n > (self.row_count * self.column_count):
            return (self.row_count * self.column_count)
        else:
            return n
        
    def on_snake_ladder(self, snakes_ladders):
        for snake in snakes_ladders.snakes:
            if snake.start == self.pos_index:
                return snake.end
        
        for ladder in snakes_ladders.ladders:
            if ladder.start == self.pos_index:
                return ladder.end
            
        return self.pos_index