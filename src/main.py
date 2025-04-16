import pygame as py

W, H = 1080, 720

# Inizializza la libreria
py.init()

screen = py.display.set_mode((W, H))
py.display.set_caption("2D Minecraft")

clock = py.time.Clock()

# Fasi del programma: menù, gioco...
inMenu = True
inGame = False

running = True

def main():
    while(running):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

        if(inMenu):
            screen.fill((240, 240, 240))

        if(inGame):
            ...

        py.display.update()

# Esegui solo se fatto in main.py
if __name__ == "__main__":
    main()