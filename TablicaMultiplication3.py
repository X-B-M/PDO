import os


x1 = int(input("Введите X :"))
y1 = int(input("Введите Y :"))
#x1: int = 15
#y1: int = 28


str_height, str_width = os.popen('stty size', 'r').read().split()
height = int(str_height)
width = int(str_width)

tmp =y1 + height #максимальное значение y1
tmp1=tmp*x1      #приблизительно большое значение x1
tmp1_len=len(str(tmp1)) #ширина большого значения
tmp2 = width//tmp1_len #примерно столько значений войдет на ширину экрана
tmpMax=tmp*(x1+tmp2) #точное большое значение
max_len = len(str(tmpMax))+1 #необходимая ширина одного столбца
f = "%"+str(max_len)+"d"

prnStr: str = " " * max_len
i = x1
while len(prnStr) <= width-max_len:
    prnStr += f % i
    i = i + 1
prnStr=prnStr[:width]
print(prnStr)

for i in range(y1, y1 + height - 2):
    prnStr = f % i
    prnStrClear = f % i
    j = x1
    while len(prnStrClear) <= width-max_len:
        if (i * j) % 10 == 0:
            prnStr += "\033[33m"
        if i == j:
            prnStr += "\033[1m"

        prnStr += f % (i * j) + "\033[0m"
        prnStrClear += f % (i*j)
        j = j + 1
    print(prnStr)

