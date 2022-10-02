from pygame import *
from random import randint

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



cards = ["cards/CLOUDCASTEL.png","cards/CRIMSON.png","cards/DARK FLLATOR.png","cards/DARK HINGHLANDER.png","cards/DRAGON KNIGHT.png","cards/FAERI DRAGON.png","cards/GDAGON IMPULSO.png","cards/GENOYIOYS.png","cards/HERALD.png","cards/LEO.png","cards/POWER DRAGON.png","cards/STARDUS DRAGON.png","cards/TATSON.png","cards/UNDERWORLD.png","cards/UNICORN.png","cards/VANARGANDER.png","cards/VINGMAN.png"]
card_rand = randint(0,17)

# class Player(GameSprite):
#     def __init__(self):
#         super().__init__("" , 400, 450, 60, 100)
#         self.speed = 5
#         self.hp = 500
#         self.points = 0
#         self.ballets = sprite.Group()

#     def card(self):
#         cards = [card_rand]





bg_image = transform.scale(image.load("cards/Pole.png"),(WIDTH, HEIGHT))

clock = time.Clock()
FPS = 60
run = True
finish = False

while run:
    window.blit(bg_image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    # if not finish:
        



    # else:
        # window.blit(result, (200, 200))
    display.update()
    clock.tick(FPS)