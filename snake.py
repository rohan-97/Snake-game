import pygame
import sys
import random
import time
from builtins import str

check_err=pygame.init()
if check_err[1]>0:
    print("{0} error occured".format(check_err[0]))
    sys.exit(-1)
else:
    print("sucessful")

# play Surface
x=1000
y=500
gameSurface=pygame.display.set_mode((x,y))
pygame.display.set_caption("Your game")
# time.sleep(5)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
brown=pygame.Color(165,42,42)

# Frames per second
fps=20
fpsController=pygame.time.Clock()

# Variables

snakepos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]
foodPos=[random.randrange(1,x/10)*10,random.randrange(1,y/10)*10]
foodSpawn=True

direction="Right"
changeTo=direction

# Game Over

def gameOver(pt):
    font=pygame.font.SysFont("papyrus",75)
    GOSurface=font.render("yeah..Game Over ur points:"+str(pt), True,red)
    GORect=GOSurface.get_rect()
    GORect.midtop=(x/2,0)
    gameSurface.blit(GOSurface,GORect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
    
# gameOver()
time.sleep(10)

def points(pt):
    fnt=pygame.font.SysFont("monaco",65)
    ptsrfc=fnt.render("points: "+str(pt),True,brown)
    rect=ptsrfc.get_rect()
    rect.topleft=(0,0)
    gameSurface.blit(ptsrfc,rect)
# Main Logic

pts=0
while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            pygame.quit
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeTo="Right"
            elif event.key==pygame.K_UP or event.key==ord('w'):
                changeTo="Up"
            elif event.key==pygame.K_LEFT or event.key==ord('a'):
                changeTo="Left"
            elif event.key==pygame.K_DOWN or event.key==ord('s'):
                changeTo="Down"
            elif event.key==pygame.K_ESCAPE:
                pygame.quit
                sys.exit()
            
#     Vaildation 
    if changeTo=="Right" and direction!="Left":
        direction="Right"
    if changeTo=="Left" and direction!="Right":
        direction="Left"
    if changeTo=="Up" and direction!="Down":
        direction="Up"
    if changeTo=="Down" and direction!="Up":
        direction="Down"
    
#     Directions
    if direction=="Right":
        snakepos[0]+=10
    if direction=="Left":
        snakepos[0]-=10
    if direction=="Up":
        snakepos[1]-=10
    if direction=="Down":
        snakepos[1]+=10
    snakepos[0]%=x
    snakepos[1]%=y
    if snakepos[0]==foodPos[0] and snakepos[1]==foodPos[1]:
        snakeBody.insert(0,list(snakepos))
        pts+=1
        if pts%5==0:
            fps+=1
        foodSpawn=False
    else:
        snakeBody.insert(0,list(snakepos))
        snakeBody.pop()
    if(not foodSpawn):
        foodPos=[random.randrange(1,x/10)*10,random.randrange(1,y/10)*10]
        foodSpawn=True
    #Drawing Snake
    gameSurface.fill(white)
    
    for body in snakeBody:
        pygame.draw.rect(gameSurface,black,pygame.Rect(body[0],body[1],10,10))
    pygame.draw.rect(gameSurface,red,pygame.Rect(foodPos[0],foodPos[1],10,10))
    
    for bd in snakeBody[1:]:
        if bd[0]==snakepos[0] and bd[1]==snakepos[1]:
            gameOver(pts)
    points(pts)
    pygame.display.flip()
    fpsController.tick(fps)