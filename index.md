# Python Hackathon


### Pygame: Sniper

<video src="Python Hackathon.mp4" width="320" height="200" controls preload></video>



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

