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

font1 = font.SysFont("Impact",35)
font2 = font.SysFont("Impact",35)
font3 = font.SysFont("Impact",70)


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



class Person:
    def __init__(self):
        self.hp = 2000
        self.cards = []
        self.cards_table = []


class Player(Person):
    pass

     

class Enemy(Person):
    pass
       


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

# p_cards_table = player.cards_table
# e_cards_table = enemy.cards_table


def update_hp( p_cards_table, e_cards_table):
    atac_sum_p = 0
    defend_sum_p = 0
    hp_card_p = 0
    for card in player.cards_table:
        atac_sum_p += card.ATK
        defend_sum_p += card.DEF
    atac_sum_e = 0
    defend_sum_e = 0
    hp_card_e = 0
    for card in enemy.cards_table:
        atac_sum_e += card.ATK
        defend_sum_e += card.DEF

    hp_card_e = defend_sum_e - atac_sum_p
    hp_card_p = defend_sum_p - atac_sum_e

    if hp_card_e > hp_card_p:
        if hp_card_e > 0:
            player.hp -= hp_card_e
        elif hp_card_e < 0:
            player.hp += hp_card_e
        else:
            pass
    elif hp_card_e < hp_card_p:
        if hp_card_p > 0:
            enemy.hp -= hp_card_p
        elif hp_card_p < 0:
            enemy.hp += hp_card_p
        else:
            pass
    else:
        pass
    
   

    if True:
        atac_sum_p = 0
        defend_sum_p = 0
        hp_card_p = 0

        atac_sum_e = 0
        defend_sum_e = 0
        hp_card_e = 0
    

    
    # p_cards_table.clear(all)
    # e_cards_table.clear(all)

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
    

    hp_playe = "hp player:" + str(player.hp)
    hp_enem = "hp enemy:" + str(enemy.hp)
    hp__p = font1.render(hp_playe ,True, (255,0,0))
    hp__e = font2.render(hp_enem ,True, (255,0,0))


    if not finish:
        # for card in player.cards:
        #     card.draw()

        # for card in enemy.cards:
        #     card.draw()

        if  len(enemy.cards) > 0 and len(player.cards) > 0:
            if rt_e == True:
                enemy.cards[r_card_e].move(place_card_e['one_card'])
                enemy.cards[r_card_e].reverse()
                enemy.cards_table.append(player.cards[r_card_p])
                r_card_e += 1
                enemy.cards[r_card_e].move(place_card_e['two_card'])
                enemy.cards[r_card_e].reverse()
                enemy.cards_table.append(player.cards[r_card_p])
                r_card_e += 1
                enemy.cards[r_card_e].move(place_card_e['three_card'])
                enemy.cards[r_card_e].reverse()
                enemy.cards_table.append(player.cards[r_card_p])
                r_card_e += 1
                rt_e = False
        

            if rt_p == True:
                player.cards[r_card_p].move(place_card_p['one_card'])
                player.cards[r_card_p].reverse()
                player.cards_table.append(player.cards[r_card_p])
                player.cards.remove(player.cards[r_card_p])
                r_card_p += 1
                player.cards[r_card_p].move(place_card_p['two_card'])
                player.cards[r_card_p].reverse()
                player.cards_table.append(player.cards[r_card_p])
                player.cards.remove(player.cards[r_card_p])
                r_card_p += 1
                player.cards[r_card_p].move(place_card_p['three_card'])
                player.cards[r_card_p].reverse()
                player.cards_table.append(player.cards[r_card_p])
                player.cards.remove(player.cards[r_card_p])
                r_card_p += 1
                rt_p = False
        
                update_hp(player.cards_table,enemy.cards_table)
        


        if player.hp <= 0:
            finish = True
            result = font3.render("Ви Програли",True, (255,0,0))

        if enemy.hp <= 0:
            finish = True
            result = font3.render("Ви Перемогли",True, (255,0,0))



    else:   
        window.blit(result, (200, 480))

    for card in enemy.cards:
        card.draw()
    for card in player.cards:
        card.draw()

    for card in enemy.cards_table:
        card.draw()
    for card in player.cards_table:
        card.draw()
    
    window.blit(hp__p, (WIDTH - 220, 520))
    window.blit(hp__e, (WIDTH - 220, 20))
    display.update()
    clock.tick(FPS)
