import time
import pygame

#路径
filePath = r'C:\Users\Jhon117\Desktop\demo\day12\7.播放音乐\泠鸢yousa - 前前前世（Slow Ver.）.mp3'

#初始化
pygame.mixer.init()

#加载
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()

#暂停
time.sleep(5)
# pygame.mixer.music.pause()
#停止
pygame.mixer.music.stop()