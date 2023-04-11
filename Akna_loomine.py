import pygame

pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))#создает окно размеров в скобках 
ekraani_pind.fill(( 0, 0, 0))
pygame.display.set_caption("mees portaalis - Kadurin Georgi")


pilt=pygame.image.load("ivi2.png")
ekraani_pind.blit(pilt,(0,0))

pilt=pygame.image.load("pr2.png")
ekraani_pind.blit(pilt,(50,100))


pilt=pygame.image.load("ch1.png")
ekraani_pind.blit(pilt,(100,100))


font=tekst=pygame.font.SysFont("Broadway",15)
sõnad="Kus ma olen!!"
värv=[0,0,0]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(150,90))


