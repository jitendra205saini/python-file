import pygame
import time
import os


pygame.init()
sound ={}


sound['up'] = pygame.mixer.Sound('C:/Users/jiten/Music/butterfly/firststepsound.wav.wav')
sound['mid'] = pygame.mixer.Sound('C:/Users/jiten/Music/butterfly/birds-flapping-wings-14763 (mp3cut.net).wav')
sound['down'] = pygame.mixer.Sound('C:/Users/jiten/Music/flippingbird/download (3).wav')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_pattern_1():  
    for i in range(1, 16):
        for j in range(1, 40):
            if (i == 3 and (j in range(1, 5) or j in range(16, 18) or j in range(23, 25) or j in range(36, 40))) or \
               (i == 4 and (j in range(1, 10) or j == 18 or j == 22 or j in range(31, 40))) or \
               (i == 5 and (j in range(2, 13) or j == 19 or j == 21 or j in range(28, 39))) or \
               (i == 6 and (j in range(2, 16) or j == 20 or j in range(25, 39))) or \
               (i == 7 and (j in range(3, 18) or j in range(19, 22) or j in range(23, 38))) or \
               (i == 8 and (j in range(4, 37))) or \
               (i == 9 and (j in range(6, 35))) or \
               (i == 10 and (j in range(4, 37))) or \
               (i == 11 and (j in range(3, 18) or j in range(19, 22) or j in range(23, 38))) or \
               (i == 12 and (j in range(4, 17) or j in range(19, 22) or j in range(24, 37))) or \
               (i == 13 and (j in range(5, 15) or j == 20 or j in range(26, 36))) or \
               (i == 14 and (j in range(7, 12) or j in range(29, 34))):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print("\n\n\nbutterfly flying animation...")
    sound['up'].play()

def print_pattern_2():
    for i in range(1, 16):
        for j in range(1, 40):
            if (i == 3 and (j in range(16, 18) or j in range(23, 25))) or \
               (i == 4 and (j == 18 or j == 22)) or \
               (i == 5 and (j in range(4, 11) or j == 19 or j == 21 or j in range(29, 37))) or \
               (i == 6 and (j in range(1, 14) or j == 20 or j in range(26, 40))) or \
               (i == 7 and (j in range(1, 18) or j in range(19, 22) or j in range(23, 40))) or \
               (i == 8 and (j in range(3, 38))) or \
               (i == 9 and (j in range(5, 36))) or \
               (i == 10 and (j in range(9, 32))) or \
               (i == 11 and (j in range(8, 18) or j in range(19, 22) or j in range(23, 33))) or \
               (i == 12 and (j in range(9, 17) or j == 20 or j in range(24, 32))) or \
               (i == 13 and (j in range(12, 16) or j in range(25, 29))):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print("\n\n\nbutterfly flying animation.....")
   
    sound['mid'].play()
def print_pattern_3():    
    for i in range(1, 16):
        for j in range(1, 40):
            if (i == 3 and (j in range(16, 18) or j in range(23, 25))) or \
               (i == 4 and (j == 18 or j == 22)) or \
               (i == 5 and (j == 19 or j == 21)) or \
               (i == 6 and (j == 20)) or \
               (i == 7 and (j in range(19, 22))) or \
               (i == 8 and (j in range(10, 18) or j in range(19, 22) or j in range(23, 31))) or \
               (i == 9 and (j in range(6, 35))) or \
               (i == 10 and (j in range(3, 38))) or \
               (i == 11 and (j in range(1, 40))) or \
               (i == 12 and (j in range(1, 18) or j in range(19, 22) or j in range(23, 40))) or \
               (i == 13 and (j in range(6, 18) or j == 20 or j in range(23, 35))) or \
               (i == 14 and (j in range(12, 17) or j in range(24, 29))):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print("\n\n\nbutterfly flying animation.......")
    sound['down'].play()  

def animate_patterns():
    while True:
      
        clear_screen()
        print_pattern_1()
        time.sleep(0.5) 
        clear_screen()
        print_pattern_2()
        time.sleep(0.5)  
        clear_screen()
        print_pattern_3()
        time.sleep(0.5)  


animate_patterns()
