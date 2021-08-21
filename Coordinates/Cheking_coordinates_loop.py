import mcpi.minecraft as minecraft  # Интеграция кода с игрой

craft = minecraft.Minecraft.create()  # Переменная, которой присваиваем функцию для взаимодействия с креативным миром

while True:

    cor = craft.player.getTilePos()  # Принимает значение координат игрока
    craft.postToChat("x = " + str(cor.x) + " y = " + str(cor.y) + " z = " + str(cor.z))

