import pygame
import json

from sl_module import *

pygame.init()

display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Snakes & Ladders")

colors = ColorPalette()

def load_text_assets(lang):
    with open(f"lang/{lang}.json", "r") as f:
        data = json.load(f)
        
    return data

text_assets = load_text_assets("en_GB")

def gen_players(player_count):
    return [Player(i, colors.player_color[i], 7, 7) for i in range(player_count)]

def main(number_of_players):
    board = Board(display, 10, 10, 351, 351, colors, text_assets, 7, 7)
    gameUI = GameUI(display, 400, 10, 400, 100, colors, text_assets)
    snakes_ladders = SnakesLaddersData("board_data.json")

    players = gen_players(number_of_players)

    current_player = 0
    waiting_for_roll = True
    animation_counter = 0

    gameUI.announce_text = text_assets["play.roll_prompt"] % current_player

    running = True
    while running:
        player_object = players[current_player]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if waiting_for_roll:
                        waiting_for_roll = False
                        
                        roll_1, roll_2 = players[current_player].roll()
                        gameUI.announce_text = text_assets["play.roll_announce"] % (current_player, roll_1, roll_2)
                        gameUI.prompt_text = ""
                        
        if not waiting_for_roll:
            animation_counter += 1
            
            if player_object.pos_index == player_object.required_dest:
                animation_counter = 0
                        
                if player_object.pos_index == 49: #! THIS NEED TO BE DYNAMIC
                    running = False
                    break
                
                revised_pos = player_object.on_snake_ladder(snakes_ladders)
                if revised_pos < player_object.pos_index:
                    gameUI.announce_text = text_assets["play.snake_hit"] % current_player
                    # play sound for snake
                elif revised_pos > player_object.pos_index:
                    gameUI.announce_text = text_assets["play.ladder_climb"] % current_player
                    # play sound for ladder
                player_object.pos_index = revised_pos
                
                current_player = (current_player + 1) % len(players)
                waiting_for_roll = True
                
                gameUI.prompt_text = text_assets["play.roll_prompt"] % current_player
            else:
                if animation_counter % 2 == 0:
                    if player_object.required_dest > player_object.pos_index:
                        player_object.pos_index += 1
                    else:
                        player_object.pos_index -= 1
        
        display.fill(colors.black)
        
        board.draw(players, snakes_ladders)
        gameUI.draw()
        
        pygame.display.update()
        
    game_end(player_object)
    
def game_end(winning_player):
    end_display = EndDisplay(display, 0, 0, 1000, 600, colors, text_assets, winning_player)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display.fill(colors.black)
        end_display.draw()
        
        if end_display.quit_button.is_pressed:
            pygame.quit()
            quit()
            
        if end_display.menu_button.is_pressed:
            run_menu()
        
        pygame.display.update()
        
def run_menu():
    main_menu = MainMenu(display, 0, 0, 1000, 600, colors, text_assets, 6)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display.fill(colors.black)
        main_menu.draw()
        
        if main_menu.quit_button.is_pressed:
            pygame.quit()
            quit()

        if main_menu.done_button.is_pressed and main_menu.layer == 2:
            main(main_menu.number_of_players)

        
        pygame.display.update()
    
run_menu()