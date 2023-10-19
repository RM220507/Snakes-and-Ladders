import json

class SnakesLaddersData:
    def __init__(self, filepath):
        self.filepath = filepath
        
        self.load_data_from_file()
        self.gen_lists()
        
    def gen_lists(self):
        self.snakes = []
        
        raw_snakes = self.raw_data.get("snakes", [])
        for snake_data in raw_snakes:
            snake = Snake(snake_data[0], snake_data[1])
            self.snakes.append(snake)
            
        self.ladders = []
        
        raw_ladders = self.raw_data.get("ladders", [])
        for ladder_data in raw_ladders:
            ladder = Ladder(ladder_data[0], ladder_data[1])
            self.ladders.append(ladder)
        
    def load_data_from_file(self):
        with open(self.filepath, "r") as f:
            self.raw_data = json.load(f)

class SnakeLadder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Snake(SnakeLadder):
    def __init__(self, start, end):
        super().__init__(start, end)
        
class Ladder(SnakeLadder):
    def __init__(self, start, end):
        super().__init__(start, end)