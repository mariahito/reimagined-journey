##############################
# Zombie Room Counter
##############################

from __future__ import division
import pygame
import gamebox

size = (0,0)
zombie = zombie_pics = camera = None

CELLSIZE = 100
EDGEBUFFER = 70

def make_room(width, height):
	global size, camera, zombie_pics, zombie
	size=(width,height)
	camera = gamebox.Camera(size[0]*CELLSIZE+2*EDGEBUFFER,size[1]*CELLSIZE+2*EDGEBUFFER)
	zombie_pics = gamebox.load_sprite_sheet("Monster-zombie.png",8,7)
	zombie = gamebox.from_image(EDGEBUFFER+CELLSIZE/2,EDGEBUFFER+CELLSIZE/2, zombie_pics[0])
	zombie.width = CELLSIZE
	look_right()


DOWN = 0
RIGHT = 1
LEFT = 2
UP = 3
blown_up = False



ticks_per_second = 10
#pygame.time.set_timer(pygame.USEREVENT, int(1000/ticks_per_second))

frame = 0
faceing = 1
dist = CELLSIZE
x = 0
y = 0

allDone = False

def action(frame,facing,moving):
	global blown_up, allDone
	pygame.time.set_timer(pygame.USEREVENT, int(1000/ticks_per_second))
	ticks = 0
	while ticks < ticks_per_second*0.25 and not blown_up:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			allDone = True
			break

		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			allDone = True
			break
		if event.type == pygame.USEREVENT:
			pygame.event.clear(pygame.USEREVENT)
			if moving:
				frame += 1
				frame %= len(zombie_pics)
				zombie.image = zombie_pics[frame%7 + 7*facing]
			camera.clear("red")

			for i in range(size[1]+1):
				camera.draw(gamebox.from_color(EDGEBUFFER+size[0]*CELLSIZE/2,EDGEBUFFER+CELLSIZE*(i),"black",size[0]*CELLSIZE+5,5))
			for i in range(size[0]+1):
				camera.draw(gamebox.from_color(EDGEBUFFER+CELLSIZE*(i),EDGEBUFFER+size[1]*CELLSIZE/2,"black",5,size[1]*CELLSIZE-5))

			camera.draw(zombie)
			camera.display()
			ticks += 1

def blow_up():
	global blown_up
	action(frame,6,True)
	action(frame,7,True)
	blown_up = True

def move_left():
	global x
	x-=1
	for i in range(4):
		zombie.x-=dist/4
		action(frame,LEFT,True)
	if x < 0:
		blow_up()

def move_right():
	global x
	x+=1
	for i in range(4):
		zombie.x+=dist/4
		action(frame,RIGHT,True)
	if x >= size[0]:
		blow_up()


def move_down():
	global y
	y+=1
	for i in range(4):
		zombie.y+=dist/4
		action(frame,DOWN,True)
	if y >= size[1]:
		blow_up()

def move_up():
	global y
	y-=1
	for i in range(4):
		zombie.y-=dist/4
		action(frame,UP,True)
	if y < 0:
		blow_up()

def look_right():
	action(frame,RIGHT,False)
	if x >= size[0]-1:
		return False
	else:
		return True

def look_left():
	action(frame,LEFT,False)
	if x > 0:
		return True
	else:
		return False

def look_up():
	action(frame,UP,False)
	if y == 0:
		return False
	else:
		return True

def look_down():
	action(frame,DOWN,False)
	if y < size[1]-1:
		return True
	else:
		return False

def announce(score_value):
	score = gamebox.from_text(EDGEBUFFER+size[0]*CELLSIZE/2,EDGEBUFFER+size[1]*CELLSIZE/2, str(score_value), "arial", 200, "white")
	camera.clear("red")

	for i in range(size[1]+1):
		camera.draw(gamebox.from_color(EDGEBUFFER+size[0]*CELLSIZE/2,EDGEBUFFER+CELLSIZE*(i),"black",size[0]*CELLSIZE+5,5))
	for i in range(size[0]+1):
		camera.draw(gamebox.from_color(EDGEBUFFER+CELLSIZE*(i),EDGEBUFFER+size[1]*CELLSIZE/2,"black",5,size[1]*CELLSIZE-5))

	camera.draw(zombie)
	camera.draw(score)
	camera.display()




def run_algorithm():
	while True:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			break
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			break

