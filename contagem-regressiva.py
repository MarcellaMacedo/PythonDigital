from time import sleep
from playsound import playsound

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOOOW!!!')
playsound('firework.mp3')
