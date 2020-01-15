import pygame
import sprites


pygame.init()
try:
  pygame.mixer.init()
  pygame.mixer.music.load('music.wav')
  pygame.mixer.music.play(-1)
except:
  pass

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("5 Nights at Destromos's")

def drawGame(sprites):   
  pass

running = True
while running:
    pygame.time.delay(100)
    
    
    
    
    
    
    
    
    