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


place_card_e = {
    "one_card" : (244,18),
    "two_card" : (390,17),
    "three_card" : (534,17)
}

place_card_p = {
    "one_card" : (244,236),
    "two_card" : (390,235),
    "three_card" : (537,235)
}

# place_card_e = {
#     "one_card" : (int(HEIGHT / 2.459),int(WIDTH / 50)),
#     "two_card" : (int(HEIGHT / 1.538),int(WIDTH / 52.941)),
#     "three_card" : (int(HEIGHT / 1.123),int(WIDTH / 52.941))
# }

# place_card_p = {
#     "one_card" : (int(HEIGHT / 2.459),int(WIDTH / 3.813)),
#     "two_card" : (int(HEIGHT / 1.538),int(WIDTH / 3.829)),
#     "three_card" : (int(HEIGHT / 1.117),int(WIDTH / 3.829))
# }

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
        self.card_img = transform.scale(image.load(card_img),(120,180))
        self.DEF = defend
        self.ATK = atk
            
    def move(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def reverse(self):
        self.image = self.card_img



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

r_card_e = 0

r_card_p = 0

n_e_c = 18
rt_e = True
rt_p = True

run = True
finish = False

while run:
    window.blit(bg_image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        # for card in player.cards:
        #     card.draw()

        # for card in enemy.cards:
        #     card.draw()

        if  len(enemy.cards) > 0:
            if rt_e == True:
                enemy.cards[r_card_e].move(place_card_e['one_card'])
                enemy.cards[r_card_e].reverse()
                r_card_e += 1
                enemy.cards[r_card_e].move(place_card_e['two_card'])
                enemy.cards[r_card_e].reverse()
                r_card_e += 1
                enemy.cards[r_card_e].move(place_card_e['three_card'])
                enemy.cards[r_card_e].reverse()
                r_card_e += 1
                rt_e = False
            else:
                pass
        else:
            pass

        if  len(player.cards) > 0:
            if rt_p == True:
                player.cards[r_card_p].move(place_card_p['one_card'])
                player.cards[r_card_p].reverse()
                r_card_p += 1
                player.cards[r_card_p].move(place_card_p['two_card'])
                player.cards[r_card_p].reverse()
                r_card_p += 1
                player.cards[r_card_p].move(place_card_p['three_card'])
                player.cards[r_card_p].reverse()
                r_card_p += 1
                rt_p = False
            else:
                pass
        else:
            pass

    else:   
        window.blit(result, (200, 200))

    for card in enemy.cards:
        card.draw()
    for card in player.cards:
        card.draw()
    display.update()
    clock.tick(FPS)