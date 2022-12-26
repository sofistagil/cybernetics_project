
import pygame
from gpiozero import Button
btn= Button(17)
btn2= Button(22)


def hello():
    print("Hello")
    pygame.mixer.music.load("Cartoon-02.wav")
    pygame.mixer.music.play()
    return
    
    
def holi():
    print("Holi")
    pygame.mixer.music.load("Cartoon-02.wav")
    pygame.mixer.music.play()
    return


pygame.mixer.init()

while True:
    btn.when_pressed=hello  
    btn2.when_pressed=holi



#user_input=input("pls give your input:")                                                  
#if hit=="b":

#elif hit=="duck":
#    pygame.mixer.music.load("Cartoon-02.wav")
#    pygame.mixer.music.play()
#else:
#    print("not found")
