import pygame
import time
import random
pygame.font.init()

WIDTH =1000
HEIGHT=800
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

BG=pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH,HEIGHT))


PLAYER_WIDTH=40
PLAYER_HEIGHT=60
PLAYER_VEL=7


PROIECTILE_WIDTH=20
PROIECTILE_HEIGHT=30
PROIECTILE_VEL=5

PR=pygame.transform.scale(pygame.image.load("arr.jpg"),(PROIECTILE_WIDTH,PROIECTILE_HEIGHT))

FONT = pygame.font.SysFont("comicsans",30)

def draw(player,elapse_time,proiectil):
    WIN.blit(BG,(0, 0))
    
    time_text =FONT.render(f"Time: {round(elapse_time)} s", 1, "black")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN,"red",player)
    
    for proiectile in proiectil:
        WIN.blit(PR,proiectile)
    
    pygame.display.update()

def main():
    run=True
    player=pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock= pygame.time.Clock()
    start_time=time.time()
    elapse_time=0
    
    proiectile_add_increment = 2000
    proiectile_count=0
    
    proiectil = []
    hit=False
    
    while run:
        proiectile_count += clock.tick(60)
        elapse_time = time.time() - start_time
        
        if proiectile_count > proiectile_add_increment:
            for _ in range(3):
                proiectile_x=random.randint(0, WIDTH - PROIECTILE_WIDTH )
                proiectile  =pygame.Rect(proiectile_x, -PROIECTILE_HEIGHT, PROIECTILE_WIDTH, PROIECTILE_HEIGHT)
                proiectil.append(proiectile)
            proiectile_add_increment = max(200, proiectile_add_increment-50)
            proiectile_count=0
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
            
        keys=pygame.key.get_pressed()
        if keys [pygame.K_LEFT] and  player.x -PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys [pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL   
             
        for proiectile in proiectil [:]:
            proiectile.y += PROIECTILE_VEL
            if proiectile.y >= HEIGHT:
                proiectil.remove(proiectile)   
            elif proiectile.y + proiectile.height >= player.y and proiectile.colliderect(player):
                proiectil.remove(proiectile)
                hit=True
                break
            
        if hit: 
            lost_text=FONT.render("You Lost!", 1, "black")
            WIN.blit(lost_text, (WIDTH/2-lost_text.get_width()/2,HEIGHT/2-lost_text.get_height()/2)) 
            pygame.display.update()
            pygame.time.delay(4000)
            break   
        draw(player,elapse_time,proiectil)
            
            
    pygame.quit()
    
if __name__=="__main__":
    main()
