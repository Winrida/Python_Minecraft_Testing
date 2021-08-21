import mcpi.minecraft as minecraft
import time

import random

craft = minecraft.Minecraft.create()

x2 = 66
x1 = 61
z2 = 144
z1 = 136

t = 0

while True:
    time.sleep(1)
    cor = craft.player.getTilePos()

    if cor.x == 37 and cor.y == 71 and cor.z == 136:
        craft.player.setTilePos(63, 74, 147)

    if cor.x == 61 and cor.y == 74 and cor.z == 146:
        xr = random.randint(x1, x2)
        zr = random.randint(z1, z2)
        craft.player.setTilePos(xr, 75, zr)

    if cor.x == 66 and cor.y == 74 and cor.z == 146:
        craft.player.setTilePos(40, 71, 135)

    if t == 5:
        craft.player.setTilePos(63, 74, 147)
        t = 0
        craft.postToChat("Game over")

    elif x1 <= cor.x <= x2 and z1 <= cor.z <= z2:
        craft.postToChat("Time = " + str(t))
        t += 1

    else:
        t = 0
