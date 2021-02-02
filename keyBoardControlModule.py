from djitellopy import tello
import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))


    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    #NOTE UPDATE TO WASD KEYS
    if getKey("LEFT"):
        print("LEFT KEY PRESSED")
    if getKey("RIGHT"):
        print("RIGHT KEY PRESSED")

if __name__ == '__main__':
    init()
    while True:
        main()