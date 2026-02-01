from pygame import *

init()
screen = display.set_mode((500,500)) 
screen.fill((255,255,255))
clock = time.Clock()

class Sprite:
    def __init__(self, x, y, w, h, img):
        self.image = image.load(img)
        self.image = transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class TextArea:
    def __init__(self, x, y, w, h, color):
        self.rect = Rect(x, y, w, h)
        self.color = color
        
    def set_text(self, text, color, size_text):
        self.text = text
        self.image = font.Font(None, size_text).render(text, True, color)

    def draw(self, x, y):
        draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.x + x, self.rect.y + y))

counter = 0
collide_counter = TextArea(470, 0, 30, 30, (255,255,255))
collide_counter.set_text(str(counter), (0,0,0), 50)
object_1 = Sprite(100, 100, 20, 20, 'картинка.png')
object_1.draw()
object_2 = Sprite(200, 200, 30, 30, 'картинка.png')
object_2.draw()

while True:
    screen.fill((255,255,255))
    collide_counter.draw(0, 0)
    object_1.draw()
    object_2.draw()
    pressed_keys = key.get_pressed()
    if pressed_keys[K_a] and object_1.rect.x >= 0:
        object_1.rect.x -= 3
    if pressed_keys[K_d] and object_1.rect.x <= 480:
        object_1.rect.x += 3
    if pressed_keys[K_s] and object_1.rect.y <= 475:
        object_1.rect.y += 3
    if pressed_keys[K_w] and object_1.rect.y >=0:
        object_1.rect.y -= 3
    if pressed_keys[K_LEFT] and object_2.rect.x >= 0:
        object_2.rect.x -= 3
    if pressed_keys[K_RIGHT] and object_2.rect.x <= 470:
        object_2.rect.x += 3
    if pressed_keys[K_DOWN] and object_2.rect.y <= 465:
        object_2.rect.y += 3
    if pressed_keys[K_UP] and object_2.rect.y >= 0:
        object_2.rect.y -= 3
    if object_1.rect.colliderect(object_2.rect):
        object_1.rect.x = 0
        object_1.rect.y = 0
        object_2.rect.x = 470
        object_2.rect.y = 465
        counter += 1
        collide_counter.set_text(str(counter), (0,0,0), 50)
    for e in event.get():
        if e.type == QUIT:
            exit()
    clock.tick(60)
    display.update()