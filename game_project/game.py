#Maria Hito(mh4wt)
#Alex Williams (arw8ah)

import pygame
import gamebox
camera = gamebox.Camera(800,600)

background=gamebox.from_image(0, 0, "http://vignette2.wikia.nocookie.net/harrypotter/images/5/59/Forbidden_Forest.png")
background.size=900,700
camera.draw("Press enter to start game","Bradley Hand ITC",30,"White",400,300)

#elements
spike=gamebox.from_image(2200,507, "http://http://www.gameart2d.com/free-sci-fi-platformer-tileset.html/Spike.png")
spike.scale_by(0.4)
spike2=gamebox.from_image(4080, 408, "http://http://www.gameart2d.com/free-sci-fi-platformer-tileset.html/Spike.png")
spike2.scale_by(0.4)
tree=gamebox.from_image(300,470, "http://www.dumbmanex.com/bynd_freestuff.html/s_gantmound_idle.png")
tree.scale_by(3)
tree2=gamebox.from_image(2000,445, "http://img00.deviantart.net/81fd/i/2013/333/f/1/spooky_tree_06_png_stock_by_jumpfer_stock-d6w1uxf.png")
tree2.scale_by(.2)
house=gamebox.from_image(6800,150, "http://orig12.deviantart.net/2bcb/f/2013/084/f/a/png_____country_house_i_by_fumar_porros-d5z8f5g.png")
house.scale_by(.5)
signs=[
    gamebox.from_image(120, 520, "http://www.gameart2d.com/free-platformer-game-tileset.html/Sign_2.png"),
    gamebox.from_image(1630, 525, "http://www.gameart2d.com/free-platformer-game-tileset.html/Sign_2.png"),
    gamebox.from_image(3770, 425, "http://www.gameart2d.com/free-platformer-game-tileset.html/Sign_2.png"),
    gamebox.from_image(3700, -30, "http://www.gameart2d.com/free-platformer-game-tileset.html/Sign_2.png"),
    gamebox.from_image(5400, 15, "http://www.gameart2d.com/free-platformer-game-tileset.html/Sign_2.png")
]

#Character
sheet = gamebox.load_sprite_sheet("http://img.webme.com/pic/e/ego-rpgmaker/cloudbp5.png",4,4)
counter = 0
frame=0
character1 = gamebox.from_image(200,200, sheet[frame])
character1.speedy = 0

walls = [
    gamebox.from_color(100, 600, "dark green", 800, 100), gamebox.from_color(100, 1250, "deep sky blue", 90000, 400),
    gamebox.from_color(750, 380, "dark green", 200, 40), gamebox.from_color(1050, 500, "dark green", 200, 40),
    gamebox.from_color(1900, 600, "dark green", 700, 90), gamebox.from_color(4000, 500, "dark green", 700, 90),
    gamebox.from_color(3800, 20, "dark green", 300, 40), gamebox.from_color(5600, 90, "dark green", 700, 90),
    gamebox.from_color(6600, 380, "dark green", 800, 100),
    gamebox.from_image(1800, 400, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(2000, 200, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(2500, 600, "http://www.dumbmanex.com/bynd_freestuff.html/b_posiplain_inside.png"),
    gamebox.from_image(2700, 750, "http://www.dumbmanex.com/bynd_freestuff.html/b_posiplain_inside.png"),
    gamebox.from_image(2700, 400, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(2890, 200, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(3000, 90, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(3250, 240, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    tree, tree2,
    gamebox.from_image(4420, 280, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(4850, 140, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png"),
    gamebox.from_image(4320, 96, "http://www.dumbmanex.com/bynd_freestuff.html/b_symswamp_top.png")
]

coins=[
    gamebox.from_image(750, 310, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(1050, 410, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(2063, 110, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(2200, 130, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(2200, 90, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(2700, 570, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(3000, 1, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(3290, 70, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(3400, 70, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(2920, 300, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(4100, 80, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(5700, 5, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(5500, 5, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(3900, -55, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(3800, -85, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(5700, 5, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png"),
    gamebox.from_image(5600, 5, "http://www.gdunlimited.net/resources/image/4946/leprechauns-gold-coin-new/gallery_19500_228_193.png")
]

coin_sound=gamebox.load_sound("https://www.freesound.org/people/bradwesson/sounds/135936/135936__bradwesson__collectcoin.wav")
gameOver_sound=gamebox.load_sound("256091__soundeffectspodcast-com__game-over-voice-2b.wav")
win_sound=gamebox.load_sound("Short_triumphal_fanfare-John_Stracke-815794903.wav")
game_start=False
game_over=False
coin_count=0
timer=0

def tick(keys):
    global game_start
    global coin_count
    global frame
    global counter
    global game_over
    global timer

    background.center=[character1.x,character1.y]

    if pygame.K_RETURN in keys:
        game_start=True #checks if game has started
    if game_start:
        counter += 1
        frame +=1
        if frame ==100:
            frame = 0

        if pygame.K_LEFT in keys:
            character1.x = character1.x - 8
            if counter % 10== 0:
                character1.image = sheet[4]
            elif counter%9==0:
                character1.image=sheet[5]
            elif counter%8==0:
                character1.image=sheet[6]
            elif counter%7==0:
                character1.image=sheet[7]

        if pygame.K_RIGHT in keys:
            character1.x = character1.x + 8
            if counter % 10== 0:
                character1.image = sheet[8]
            elif counter%9==0:
                character1.image=sheet[9]
            elif counter%8==0:
                character1.image=sheet[10]
            elif counter%7==0:
                character1.image=sheet[11]

        #gravity
        character1.speedy = character1.speedy + 0.25
        character1.y = character1.y + character1.speedy

        # check for collisions
        for wall in walls:
            # check for jump
            if character1.bottom_touches(wall):
                if pygame.K_UP in keys: # possible to jump
                    if character1.speedy >= 0: # not already moving up
                        character1.speedy = -10 # jump!
                    if counter%4==0:
                        character1.image=sheet[11]
            # check if character hits wall
            if character1.touches(wall):
                character1.move_to_stop_overlapping(wall) # and stop overlapping

        camera.center = character1.center # cause the camera to follow the character


        if character1.touches(spike):
            game_over=True
            camera.clear("black")
            camera.draw("Game Over","Bradley Hand ITC",50,"White",400,300)
            gameOver_sound.play()
            gamebox.pause()

        elif character1.touches(spike2):
            game_over=True
            camera.clear("black")
            camera.draw("Game Over","Bradley Hand ITC",50,"White",400,300)
            gameOver_sound.play()
            gamebox.pause()
        elif character1.touches(walls[1]):
            game_over=True
            camera.clear("black")
            camera.draw("Game Over","Bradley Hand ITC",50,"White",400,300)
            gameOver_sound.play()
            gamebox.pause()
        else:
            game_over=False
            camera.draw(background)
            for wall in walls:
                camera.draw(wall)
            # collect coins
            for coin in coins:
                camera.draw(coin)
                if character1.touches(coin):
                    coins.remove(coin)
                    coin_sound.play()
                    coin_count=coin_count+1
            camera.draw(spike2)

            for sign in signs:
                camera.draw(sign)
            camera.draw(spike)
            camera.draw(character1)
            camera.draw("Coins:","Arial",25,"yellow",60,60)
            camera.draw(str(coin_count),"Arial",25,"yellow",100,62)
            camera.draw(house)
            # Timer
            camera.draw("Timer:","Arial",25,"yellow",360,62)
            seconds=(pygame.time.get_ticks()-timer)/1000
            camera.draw(str(int(seconds)),"Arial",25,"yellow",400,62)
            if seconds>100:
                camera.clear("black")
                camera.draw("Game Over","Bradley Hand ITC",50,"White",400,300)
                camera.draw("You ran out of time","Bradley Hand ITC",40,"White",400,400)
                gameOver_sound.play()
                gamebox.pause()

            if character1.touches(house):
                camera.clear("black")
                camera.draw("You Win!","Bradley Hand ITC",50,"White",400,300)
                gamebox.pause()
                win_sound.play()

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 60
# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

