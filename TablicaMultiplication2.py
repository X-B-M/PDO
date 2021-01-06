#цветной вывод
#       сброс

# \033[0-7m — это различные эффекты, такие как подчеркивание, мигание, жирность и так далее;
# \033[30-37m — коды, определяющие цвет текста (черный, красный, зелёный, жёлтый, синий,фиолетовый,сине-голубой,серый);
# \033[40-47m — коды, определяющие цвет фона.

# Цвет  	Текст 	Фон
# Чёрный 	30 	40
# Красный 	31 	41
# Зелёный 	32 	42
# Жёлтый 	33 	43
# Синий  	34 	44
# Фиолетовый 	35 	45
# Бирюзовый 	36 	46
# Белый	        37 	47

# Код 	Значение
# 0 	Сброс к начальным значениям
# 1 	Жирный
# 2 	Блёклый
# 3 	Курсив
# 4 	Подчёркнутый
# 5 	Редкое мигание
# 6 	Частое мигание
# 7 	Смена цвета фона с цветом текста

x1 = 15
x2 = 30
y1 = 28
y2 = 41
prnStr = "   "
for i in range(x1, x2 + 1):
    prnStr += "%5d" % (i)
print(prnStr)

for i in range(y1, y2 + 1):
    prnStr = "%3d" % (i)
    for j in range(x1, x2 + 1):
        if (i * j) % 10 == 0:
            prnStr += "\033[33m"
        if i == j:
            prnStr += "\033[1m"

        prnStr += "%5d" % (i * j) + "\033[0m"
    print(prnStr)

