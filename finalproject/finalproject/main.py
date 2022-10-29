from pygame import *
from random import randint,shuffle

from cards import cards_list
mixer.init()
font.init()
init()

WIDTH = 900
HEIGHT = 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Zenterost")




class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.width = width
        self.height = height
    
    def draw(self):
        window.blit(self.image, self.rect)






class Player:
    def __init__(self):
        self.hp = 500
        self.cards = []

    

    

class Enemy:
    def __init__(self):
        self.hp = 500
        self.cards = []



class Card(GameSprite):
    def __init__(self, name, card_img, defend, atk, x, y):
        super().__init__('cards/reverse.png', x, y, 120, 180)
        self.name = name
        self.card_img = transform.scale(image.load(card_img),(60,100))
        self.DEF = defend
        self.ATK = atk
            



bg_image = transform.scale(image.load("cards/Pole.png"),(WIDTH, HEIGHT))

clock = time.Clock()

player = Player()
player.cards = []

p_x = 50
p_y = 400
name_cards = list(cards_list.keys())
shuffle(name_cards)
for card in name_cards:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'],p_x, p_y)
    p_x -= 0.5
    p_y += 0.5 
    player.cards.append(new_card)


e_x = 50
e_y = 50
enemy = Enemy()
shuffle(name_cards)
enemy.cards = []
for card in name_cards:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'],e_x,e_y)
    e_x -= 0.5
    e_y += 0.5 
    enemy.cards.append(new_card)


FPS = 60

r_card = 0
rt = 0
n_e_c = 18

run = True
finish = False

while run:
    window.blit(bg_image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        for card in player.cards:
            card.draw()

        for card in enemy.cards:
            card.draw()

        if  len(enemy.cards) > 0:
            if rt == True:
                enemy.cards[r_card].move(place_card_e[one_card])
                r_card += 1
                window.blit(enemy.cards[r_card], (place_card_e[two_card]))
                r_card += 1
                window.blit(enemy.cards[r_card], (place_card_e[three_card]))
                r_card += 1
                rt == False
            else:
                pass
        else:
            pass


    else:   
        window.blit(result, (200, 200))
    enemy.cards.draw(window)
    display.update()
    clock.tick(FPS)