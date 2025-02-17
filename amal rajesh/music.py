import pygame
import random
pygame.init()

print("CHANGE THE MOOD WITH SONGS")

songs = {
    'romantic': [
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 1.32.24 PM.mpeg',
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 1.32.25 PM.mpeg',
    ],
    'party': [
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 1.51.12 PM.mpeg',
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 1.55.20 PM (1).mpeg',

    ],
    'sleep': [
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 2.01.48 PM.mpeg',
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 2.03.13 PM.mpeg',
    ],
    'trending': [
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 1.32.25 PM.mpeg',
        r'C:\Users\kithy\Downloads\WhatsApp Audio 2024-01-05 at 2.07.02 PM.mpeg',

    ],
}

def suggestsong(mood):
    mood = mood.lower()
    if mood in songs:
        songlist = songs[mood]
        if songlist:
            return random.choice(songlist)
        else:
            return "Sorry, no songs found for that mood."
    else:
        return "Invalid mood. Please enter a valid mood."

while True:
    usermood = input("Enter your mood (romantic, party, sleep, trending, etc.), or press 0 to pause: ").lower()
    if not usermood.strip():
        break

    result = suggestsong(usermood)
    print("Recommended song:", result)
    pygame.mixer.init()
    pygame.mixer.music.load(result)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if input("Press 0 to stop the music (or press 0 to change mood): ").strip():
            pygame.mixer.music.stop()
            break
pygame.quit()

