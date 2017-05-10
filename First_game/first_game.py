#Maria Hito(mh4wt)

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 200, "blue", 15, 40)
char3=gamebox.from_image(200, 100, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png")
character.yspeed = 0
coins=[char3]
projectiles=[]
walls = [
    gamebox.from_color(50,250, "slate grey", 200, 10),
    gamebox.from_color(400,150, "slate grey", 200, 10),
    gamebox.from_color(600,25, "slate grey", 200, 10),
]
counter = 0
coin_count=0
game_start=False

def tick(keys):
    # get access to the counter
    global counter
    global coin_count
    global game_start

    camera.clear("black")
    camera.draw("Collect 10 coins to win the game.","Bradley Hand ITC",40,"White",400,200)
    camera.draw("Instructions:","Bradley Hand ITC",30,"White",400,250)
    camera.draw("Press space bar to jump and left and right keys to move the character","Bradley Hand ITC",20,"White",400,300)
    camera.draw("Press enter to start game","Bradley Hand ITC",30,"White",400,400)

    if pygame.K_RETURN in keys:
        game_start=True #checks if game has started
    if game_start: #executes game when enter key has been pressed
        if pygame.K_RIGHT in keys:
            character.x += 10
        if pygame.K_LEFT in keys:
            character.x -= 10
        character.yspeed += 1
        character.y = character.y + character.yspeed

        camera.clear("light cyan")
        camera.draw(character)

        camera.y -= 3

        counter += 1
        if counter % 30 == 0:
            new_wall = gamebox.from_color(random.randint(200,600), camera.y-300,  "slate grey", random.randint(100,250), 10)
            walls.append(new_wall)
        if counter % 35 == 0:
            new_coins = gamebox.from_image(random.randint(5,795),camera.y-300, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png")
            coins.append(new_coins)
        if counter % 70 == 0:
            numstars = random.randint(0,9)
            for i in range(numstars):
                projectiles.append(gamebox.from_color(random.randint(5,795),camera.y-300,"red",6,6))

        for coin in coins:
            coin.y += 1
            if(coin.y > 600):
                coins.remove(coin)
            if character.touches(coin):
                coins.remove(coin)
                coin_count=coin_count+1
                if coin_count >= 10:
                    camera.draw("You Win!","Arial",50,"Red",400,300)
                    gamebox.pause()
            camera.draw(coin)

        for projectile in projectiles:
            # move the projectile
            projectile.y += 3
            if(projectile.y > 600):
                projectiles.remove(projectile)
            if projectile.touches(character):
                #camera.clear("black")
                #projectiles.remove(projectile)
                camera.draw("Game Over!","Arial",40,"Red",400,300)

                gamebox.pause()
            # draw the projectiles
            camera.draw(projectile)

        if character.y - camera.y > 300:
            camera.draw("Game Over!","Arial",40,"Red",400,300)
            #camera.clear("black")
            gamebox.pause()

        for wall in walls:
            if character.bottom_touches(wall):
                character.yspeed = 0
                if pygame.K_SPACE in keys:
                    character.yspeed = -20
            if character.touches(wall):
                character.move_to_stop_overlapping(wall)
            camera.draw(wall)
        #camera.draw(str(ticks_per_second-counter),"Arial",25,"blue",100,62)
        camera.draw("Coins:","Arial",25,"blue",60,60)
        camera.draw(str(coin_count),"Arial",25,"blue",100,62)
        #camera.draw("Time:","Arial",25,"blue",400,60)
        #camera.draw(str(ticks_per_second/30),"Arial",25,"blue",500,60)
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
