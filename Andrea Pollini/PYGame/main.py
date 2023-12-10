'''
Creiamo una finestra colorata che contenga la nostra immagine jpg
facendola poi muovere da sinistra a destra. 
Utilizzeremo la funzione sin per ciclare lo spostamento avanti ed indietro
Il master contiene la versione con 2 immagini. Nei commit sono presenti versioni
con 1 sola immagine!
'''
import pygame as pg
from math import sin, radians

# inizializzo il modulo
pg.init()

# definisco le dimensioni della finestra
SCREEN_SIZE = (800, 600)


# definiamo le dimensioni della finestra
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

# variabile per interrompere il loop
running = True

counter = 0

# load my image for insert into window
my_image = pg.image.load("asa.jpeg")
my_image_1 = pg.image.load("marx.jpg")

# loop per la generazione della finestra e dei singoli frame
while running:
    counter += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# window color fill
    screen.fill((200, 50, 50))


# spostamento immagine usando il seno
# radians trasforma i gradi in radianti
    screen.blit(my_image, (50 + 50 * (2 * sin(radians(counter))), 0))
    screen.blit(my_image_1, (150 + 150 * (4 * sin(radians(counter))), 0))

# redraw display
    pg.display.update()
    clock.tick(60)

# calcoliamo gli fps della nostra finestra
    fps = clock.get_fps()

# set titolo nella finestra
    pg.display.set_caption(f"fps: {fps: .2f}")

# uscita dalla finestra
pg.quit()
