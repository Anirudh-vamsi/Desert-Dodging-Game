import pygame
import time
import random

pygame.init()

WIDTH,HEIGHT= 1000,800

green=(0,255,0)

WIN=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space Dodge")

BG=pygame.transform.scale(pygame.image.load("back.jpeg"),(WIDTH,HEIGHT))

player=pygame.image.load('car.png')

car_height=60

car_width=40

clock=pygame.time.Clock()

Font=pygame.font.Font('FreeSansBold.ttf',25)

clock.tick(60)

def stars(STAR_X,STAR_Y,STAR_WIDTH,STAR_HEIGHT,color):
    pygame.draw.rect(WIN,color,[STAR_X,STAR_Y,STAR_WIDTH,STAR_HEIGHT])
    for i in range(10):
        pygame.display.update()
    

def draw(x,y,elapsed_time):
    WIN.blit(BG,(0,0))
    WIN.blit(player,(x,y))
    time_text=Font.render(f"Time: {round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))
    pygame.display.update()
    

def text_objects(text,font):
    textSurface = font.render(text, True, 'black')
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('FreeSansBold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((500),(200))
    WIN.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    

def crash():
    message_display("You crashed!")


def main():
    run=True
    
    start_time=time.time()
    elapsed_time=0
    
    x=(WIDTH*0.45)
    y=(HEIGHT*0.8)
    
    x_change=0
    y_change=0
    
    STAR_X=random.randrange(0,WIDTH)
    STAR_Y=-10
    STAR_WIDTH= 20
    STAR_HEIGHT=40
    STAR_VEL=5

    while run:
        elapsed_time=time.time()-start_time
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change= -5
                if event.key==pygame.K_RIGHT:
                    x_change= 5
                if event.key==pygame.K_UP:
                    y_change= -1
                if event.key==pygame.K_DOWN:
                    y_change= 1
                if event.key==pygame.K_ESCAPE:
                    x=(WIDTH*0.45)
                    y=(HEIGHT*0.8)
                    pygame.time.delay(1000)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT and event.key==pygame.K_RIGHT:
                    x_change=0    
        

        x +=x_change
        y +=y_change

        if x>WIDTH - car_width or x<0:
            crash()
        if y>HEIGHT-car_height or y<0:
            crash()

        stars(STAR_X,STAR_Y,STAR_WIDTH,STAR_HEIGHT,green)
        STAR_Y+=STAR_VEL
        draw(x,y,elapsed_time)

        if STAR_Y>HEIGHT:
            STAR_Y=0-STAR_HEIGHT
            STAR_X= random.randrange(0,WIDTH)

        if y<STAR_Y+ STAR_HEIGHT:
            print('x Crossover')
            if x>STAR_X and x< STAR_X + STAR_WIDTH or x+car_width>STAR_X and x+car_width < STAR_X+STAR_WIDTH:
                print('x crossover')
                crash()
        pygame.display.update()
        

    
main()    
pygame.quit()


