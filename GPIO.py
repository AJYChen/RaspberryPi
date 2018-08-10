from gpiozero import RGBLED
from time import sleep
rgbled = RGBLED(17,27,22)
colors = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,1,0),(1,1,1)]
print("run");
while True:
    if __name__ == "__main__":
        for color in colors:
            rgbled.color = color
            sleep(1)