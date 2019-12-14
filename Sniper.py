import pygame
import random
import time



# initialize game engine
pygame.init()
pygame.display.set_caption('Sniper')


#background = pygame.image.load('Space2.png')

# Game music 
pygame.mixer.music.load("Good_Times.mp3") 
pygame.mixer.music.play(-1,0.0)

# Initialize values for color (RGB format)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

window_width=800
window_height=600
clock_tick_rate=20

# Total number of circles to draw
totalCircles=5


# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

# Set title to the window
pygame.display.set_caption("Sniper")

dead=False

clock = pygame.time.Clock()

all_circle_list=pygame.sprite.Group()
block_list=pygame.sprite.Group()

# Contains all bullets information
bullet_list=pygame.sprite.Group()

# Number of bullets used
bulletCount=0

# Class used to draw circle game objects
class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color, [0, 0, 20, 20])

    def update(self): # Speed of targets falling
        self.rect.y+=1

        if(self.rect.y==window_height):
            self.rect.y=10

# Player circle
class Player(CircleSprite):
    def __init__(self, width, height, color):
        super().__init__(width, height, color)
        self.rect.y = window_height-10

# Class represent Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
# Bullet color and size
    
        pygame.draw.line(self.image, RED, [5,0], [5, 15], 3)
        pygame.draw.line(self.image, RED, [5,0], [0, 5], 3)
        pygame.draw.line(self.image, RED, [5,0], [10, 5], 3)

        self.rect = self.image.get_rect()

# Define all circle game objects
for i in range(totalCircles):
    color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # Randomize colors for targets
    myCircle=CircleSprite(20, 20, color)
    myCircle.rect.x = random.randrange(window_width-20) #Randomize X position for targetss
    myCircle.rect.y = random.randrange(window_height-20) #Randomize Y position for targets

    all_circle_list.add(myCircle)
    block_list.add(myCircle)
    
# Set player shape size
playerSprite = Player(20, 20, GREEN)
playerSprite.rect.y = window_height-20
all_circle_list.add(playerSprite)
score=0

# Program start time
start_time = time.time()

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        elif event.type == pygame.MOUSEBUTTONDOWN: # Input mouse click for bullet
            bullet = Bullet(BLACK)
            bullet.rect.x = playerSprite.rect.x
            bullet.rect.y = playerSprite.rect.y
            all_circle_list.add(bullet)
            bullet_list.add(bullet)
            bulletCount+=1
            #print("Good Job!")
    
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
    playerSprite.rect.x = pos[0]

    for tempBullet in bullet_list:
        tempBullet.rect.y-=10 # Bullet speed

        if(tempBullet.rect.y==0):
            bullet_list.remove(tempBullet)
            all_circle_list.remove(tempBullet)
            print("Missed the target")

        blocks_hit_list = pygame.sprite.spritecollide(tempBullet, block_list, True)

        num=len(blocks_hit_list)

        if(num > 0): #Keep score
            score+=num
            print("You have hit", score, "targets")
            bullet_list.remove(tempBullet)
            all_circle_list.remove(tempBullet)

        if(tempBullet.rect.y==0):
            bullet_list.remove(tempBullet)
    screen.fill((0,0,0))
    #screen.blit(background, (0,0))
    for circle in block_list:
        circle.update()

    all_circle_list.draw(screen)

   

    pygame.display.flip()
    clock.tick(clock_tick_rate)
    
# Provide results 
    if(score == totalCircles):
        print("You won the game in ", (time.time() - start_time), " seconds")
        print("Total bullets used: ", bulletCount)
        print("Shooting Accuracy: ", (totalCircles/bulletCount)*100, "%")
        dead = True
 
        

pygame.quit()
