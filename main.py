import pygame
from random import randint
# Экран
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 420

pygame.display.set_caption("Save the bird")
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x2 = -0  # -1051 Переменная для движения фона
score = 0

# Игрок
x = SCREEN_WIDTH / 2  # 210
y = 200

# Частота кадров
FPS = 60

# Отсчет для деревьев начинается от 425
vremy = 425

# Расположение деревьев по оси Y
y_wood = 300
y_wood1 = y_wood - 700
life = True




pygame.init()

# Класс фона
class Back(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('img\\bg1.png').convert_alpha()
bgg = Back()

# Класс птицы
class Player(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('img\\player.png').convert_alpha()  # 85x64
      self.rect = self.image.get_rect()
player = Player()

# Класс деревьев
class Wood(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('img\\wood.png').convert_alpha()  # 85x504
      self.rect = self.image.get_rect()
wood = Wood()

clock = pygame.time.Clock()
run = True
while(run):

   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

# Движение фона
   x2 -= 1
# Нижняя граница птички по оси Y
   y1 = y + 50
# Для коллизии дерева
   vremy1 = vremy + 43
   vremy2 = vremy + 73

# Повтор фона
   if x2 <= -1051:
      x2 = 0
# Не дает улететь и упасть за экран
   if y <= 0:
      y = 0
   if y >= 650:
      y = 650
# Коллизия с деревьями(было сложно, но я придумал это)
   if (y1>y_wood and (vremy <= 274 and vremy >= 210) or y1>y_wood and (vremy1 <= 274 and vremy1 >= 210) or y1>y_wood and (vremy2 <= 274 and vremy2 >= 210)):
      life = False

   if (y<y_wood1+485 and (vremy <= 274 and vremy >= 210) or y<y_wood1+485 and (vremy1 <= 274 and vremy1 >= 210) or y<y_wood1+485 and (vremy2 <= 274 and vremy2 >= 210)):
      life = False

# Поведение игры на нажатие кнопки пробела
   keys = pygame.key.get_pressed()
   if life == True:
      if keys[pygame.K_SPACE]:
         y -= 8
         x2 -= 1
         vremy -= 3

         player.image = pygame.image.load('img\\player2.png').convert_alpha() # 85x64
      else:
# Гравитация
         y += 8
         vremy -= 3
         player.image = pygame.image.load('img\\player.png').convert_alpha()  #  85x64

# Появление в окне фона и птички
   win.blit(bgg.image, (x2, 0))
   win.blit(player.image, (x, y))


# Появление деревьев
   if vremy <= 425:
      win.blit(wood.image, (vremy, y_wood))  # Нижнее дерево
      win.blit(wood.image, (vremy, y_wood1))  # Верхнее дерево
   if vremy == -100 or vremy == -105:
      vremy = 425
# +1 К счету после исчезания дерева
      score += 1
      print("ТВОЙ СЧЕТ:",score)
      y_wood = randint(210, 540)
      y_wood1 = y_wood - 704


# Возродиться нажатием кнопки "r"
   if keys[pygame.K_r]:
      x2 = -0  # -1051 # Переменная для движения фона

# Координаты игрока
      x = SCREEN_WIDTH / 2  # 210
      y = 200

# Частота кадров
      FPS = 60

# Отсчет для деревьев начинается от 425
      vremy = 425

# Расположение деревьев по оси Y
      y_wood = 300
      y_wood1 = y_wood - 700
      life = True

   pygame.display.update()



pygame.quit()

