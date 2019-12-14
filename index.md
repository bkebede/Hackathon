# Python Hackathon


### Pygame: Sniper

<video src="Python Hackathon.mp4" width="320" height="200" controls preload></video>

```python
for i in range(totalCircles):
    color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # Randomize colors for targets
    myCircle=CircleSprite(20, 20, color)
    myCircle.rect.x = random.randrange(window_width-20) #Randomize X position for targetss
    myCircle.rect.y = random.randrange(window_height-20) #Randomize Y position for targets

    all_circle_list.add(myCircle)
    block_list.add(myCircle)
```

The code above defines the circle objects in my game which are the targets. The targets fall from the top and the code above allows me to randomize the color of these targets as well as their positions on the X and Y axis so that the player has some challenge in hitting the targets. 

```python
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
```

The code above defines the bullets in the game and provides the dynamics for it such as the size of theh bullets and the color of them that will be used. 
```python
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
```

The code above shows the input process within the game, where if you click on your mouse, then a bullet is prompted to shoot at the target wherever you place your mouse cursor. The count to how many bullets you have used goes up by one as the score is reported back to you at the end, showing how many bullets were used as well as your shooting accuracy. 


```python
    if(score == totalCircles):
        print("You won the game in ", (time.time() - start_time), " seconds")
        print("Total bullets used: ", bulletCount)
        print("Shooting Accuracy: ", (totalCircles/bulletCount)*100, "%")
        dead = True
```

The code above gives you the final output of the game, which is a report on your performance. It will display how long it took you to win the game in seconds. It will tell you how many bullets you needed to use and it will tell you your shooting accuracy based off how many bullets needed to hit all the targets in a percentage format. 
