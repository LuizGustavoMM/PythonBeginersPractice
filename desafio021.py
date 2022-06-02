'''from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3('mcpz.mp3')
play(song)
'''
import pygame
pygame.init()
pygame.mixer.music.load('mcpz.mp3')
pygame.mixer.music.play()
pygame.event.wait()