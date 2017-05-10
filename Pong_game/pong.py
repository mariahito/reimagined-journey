# Maria Hito(mh4wt)
#Dalton Anderson (dja3vf)

import pygame
import gamebox
camera = gamebox.Camera(800,600)

p_width = 10
p_height = 80
ball_velocity = 15
player_speed = 14
p1_score = 0
p2_score = 0
game_on = False

ticker = 0

paddle_sound = gamebox.load_sound("paddle.wav")
wall_sound = gamebox.load_sound("wall.wav")

walls = [
    gamebox.from_color(400, 600, "green", 1000, 20),
    gamebox.from_color(400, 0, "green", 1000, 20),
]

p1 = gamebox.from_color(20, 400, "red", 15, 100)
p2 = gamebox.from_color(780, 400, "yellow", 15, 100)
ball = gamebox.from_color(400,300, "green", 20, 20)

ball.xspeed = ball_velocity
ball.yspeed = ball_velocity
players=[p1,p2]
def tick(keys):

    global game_on
    global p1_score
    global p2_score

    # --- BALL MOVEMENT ---
    if pygame.K_SPACE in keys:
        game_on = True

    if game_on:
        ball.x +=ball.xspeed
        ball.y +=ball.yspeed
        if pygame.K_s in keys:
            p1.y += player_speed
        if pygame.K_w in keys:
                p1.y -= player_speed
        if pygame.K_UP in keys:
                p2.y -= player_speed
        if pygame.K_DOWN in keys:
                p2.y += player_speed

    # ----- COLLISION DETECTION -----
        for player in players:
            if ball.touches(player):
                ball.xspeed = -ball.xspeed
                paddle_sound.play()
        for wall in walls:
           if ball.touches(wall):
                ball.yspeed = -ball.yspeed
                wall_sound.play()

    # ----- SCORING ------
        if ball.x < 0:
            p2_score+=1
            ball.x=400
            ball.y=300
            game_on=False

        if ball.x > 800:
            p1_score+=1
            ball.x=400
            ball.y=300
            game_on=False

    # ----- DRAW METHODS --------
    # We have provided all of the draw methods for you.
    # You do not need to add anything here.
    camera.clear("black")
    camera.draw(gamebox.from_text(300, 50, str(p1_score), "Arial", 50, "Red", True))
    camera.draw(gamebox.from_text(500, 50, str(p2_score), "Arial", 50, "Yellow", True))

    # Draw all the walls
    for wall in walls:
        camera.draw(wall)

    # Draw the player paddles and the ball
    camera.draw(p1)
    camera.draw(p2)
    camera.draw(ball)

    # ---- CHECKING FOR WIN ----
    if p1_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Red Wins!", "Arial", 40, "Red", True))
        gamebox.pause()
    if p2_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Yellow Wins!", "Arial", 40, "Yellow", True))
        gamebox.pause()
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)