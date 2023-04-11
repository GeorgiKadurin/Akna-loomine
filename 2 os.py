import pygame

pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))#создает окно размеров в скобках 
ekraani_pind.fill(( 0, 0, 0))
pygame.display.set_caption("Lumememm - Kadurin Georgi")














#основ тело мал
lil=pygame.Rect(130,10,50,50)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)

#глаз 1
lil=pygame.Rect(140,25,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,200), lil)

#глаз 1
lil=pygame.Rect(163,25,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,200), lil)

#нос
lil=pygame.Rect(151,38,7,12)
pygame.draw.ellipse(ekraani_pind, (255,165,0), lil)

#основ тело сред
lil=pygame.Rect(123,58,65,65)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)

#рука 1
ristkülik=pygame.Rect(80,85,50,7)                            
pygame.draw.rect(ekraani_pind,(250,250,250),ristkülik)

#рука 2
ristkülik=pygame.Rect(180,85,50,7)                            
pygame.draw.rect(ekraani_pind,(250,250,250),ristkülik)

#пуговица 1
lil=pygame.Rect(152,70,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,0), lil)

#пуговица 2
lil=pygame.Rect(152,90,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,0), lil)


#основ тело большое
lil=pygame.Rect(113,120,85,85)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)



#метла
ristkülik=pygame.Rect(80,50,7,120)                            
pygame.draw.rect(ekraani_pind,(205,133,63),ristkülik)




lopp_x=120
lopp_y=0
for i in range(10):
    pygame.draw.line(ekraani_pind,"#a17c38",(83,60),(lopp_x,lopp_y),3 )
    lopp_x-=8
    lopp_y+=2



pygame.display.flip()

while True:
    event=pygame.event.poll()  
    if event.type==pygame.QUIT:
        break

pygame.quit() 



