import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #2
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #8
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True ,False)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200 #9
        screen.blit(bg_img, [-x, 0])   #6
        screen.blit(bg_img2,[1600-x,0]) #7 もう一枚追加  
        screen.blit(bg_img,[3200-x,0]) #9 もう一枚追加 
        screen.blit(kk_img, [300, 200]) #4
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()