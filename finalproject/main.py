from pygame import *
from random import randint

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




card_rand = randint(0,17)

class Player:
    def __init__(self):
        self.hp = 500
        self.ballets = sprite.Group()
        self.cards = 

    # def card(self):
    #     cards = [card_rand]

class Enemy(GameSprite):
    def __init__(self):
        super().__init__(card_rand , 10, 90, 20, 20)
        self.hp = 500
        self.cards =

    # def card(self):
    #     cards = [card_rand]


class Card(GameSprite):
    def __init__(self, name, card_img, defend, atk):
        super().__init__('reverse.png', x, y, width, height)
        self.name = name
        self.card_img = card_img
        self.DEF = 0
        self.ATK = 0
            



bg_image = transform.scale(image.load("cards/Pole.png"),(WIDTH, HEIGHT))

clock = time.Clock()
p_cards = []
for card in cards_list:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'])
    p_cards.append(new_card)

e_cards = []
for card in cards_list:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'])
    e_cards.append(new_card)

FPS = 60
run = True
finish = False

while run:
    window.blit(bg_image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        pass



    else:
        window.blit(result, (200, 200))

    display.update()
    clock.tick(FPS)