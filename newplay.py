import numpy as np
import pygame

# List of audio files
audio_files = [
    "1.mp3",
    "2.mp3",
    "3.mp3",
    "4.mp3",
    "5.mp3",
    "6.mp3",
    "7.mp3",
    "8.mp3",
    "9.mp3",
    "10.mp3"
]

# Initialize pygame mixer
pygame.mixer.init()

# Convert audio_files to numpy array for shuffling
audio_files = np.array(audio_files)

# Play audio randomly without repetition within a cycle
unplayed_audios = audio_files.copy()
np.random.shuffle(unplayed_audios)

paused = False
while unplayed_audios.size > 0:
    if not paused:
        audio_file = unplayed_audios[0]
        unplayed_audios = unplayed_audios[1:]
        print("Now playing:", audio_file)

        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    # Wait for the audio to finish playing or handle pause/resume/skip
    while pygame.mixer.music.get_busy() or paused:
        command = input("Enter 'p' to pause, 'r' to resume, 's' to skip, or 'q' to quit: ")

        if command == 'p':
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                paused = True
                print("Audio paused.")
        elif command == 'r':
            if paused:
                pygame.mixer.music.unpause()
                paused = False
                print("Audio resumed.")
        elif command == 's':
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                print("Skipped to the next song.")
        elif command == 'q':
            pygame.mixer.music.stop()
            unplayed_audios = np.array([])
            print("Playback stopped.")
            break

# Clean up resources
pygame.mixer.quit()

