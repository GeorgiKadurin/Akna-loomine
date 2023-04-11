import pygame

pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))#создает окно размеров в скобках 
ekraani_pind.fill(( 255, 255, 0))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(280,140,70,400)                            #фигура
pygame.draw.rect(ekraani_pind,(100,100,0),ristkülik)            #меняем цвет в стиле ргб

ristkülik=pygame.Rect(170,100,50,180)                            
pygame.draw.rect(ekraani_pind,(100,100,0),ristkülik)

ristkülik=pygame.Rect(170,100,50,180)                            
pygame.draw.rect(ekraani_pind,(100,100,0),ristkülik)

ristkülik=pygame.Rect(220,240,60,40)                            
pygame.draw.rect(ekraani_pind,(100,100,0),ristkülik)

pilt=pygame.image.load("ivi.png")
ekraani_pind.blit(pilt,(270,100))

font=tekst=pygame.font.SysFont("Broadway",40)
sõnad="kõrb!"
värv=[0,0,0]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(250,15))



#ristkülik=pygame.Rect(0,0,100,100)
#pygame.draw.rect(ekraani_pind,(100,0,0),ristkülik)


#lil=pygame.Rect(200,100,250,200)
#pygame.draw.ellipse(ekraani_pind, (100,0,0), lil)

pygame.display.flip() #нужно для того, чтобы код работала и запускался #отображает

while True:
    event=pygame.event.poll()  #функция для крестика, чтобы закрыть раб.  код
    if event.type==pygame.QUIT:
        break

pygame.quit() #нужно для того, чтобы код работала





























