import pygame
pygame.init()
pygame.mixer.music.load(C:\Users\mat_m\OneDrive\Área de Trabalho\mp3)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)