import mcpi.minecraft as minecraft  # Интеграция кода с игрой

craft = minecraft.Minecraft.create()  # Переменная, которой присваиваем функцию для взаимодействия с креативным миром

while True:
    cor = craft.player.getTilePos()  # Принимает значение координат игрока

    if (cor.x == 39 and cor.y == 71 and cor.z == 141) or (cor.x == 40 and cor.y == 71 and cor.z == 141):
        craft.postToChat("Welcome home")
    else:
        craft.postToChat("Go home")