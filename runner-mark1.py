import os
import time


def prn_line(offset_x):
    str_height, str_width = os.popen('stty size', 'r').read().split()
    height = int(str_height)
    width = int(str_width)
    if offset_x >= width:
        offset_x = 0
    tmp_str = " " * offset_x
    tmp_str = tmp_str + "\033[32m" + "*" + "\033[0m"
    tmp_str = tmp_str + " " * (width - offset_x)
    print("\033[10;0H", end='')
    print(tmp_str)
    print("\033[11;0H", offset_x)
    return offset_x


x = 0
# x[0] = int(input("Введите X :"))
os.popen('clear', 'w')
while 1:
    x=prn_line(x)
    x = x + 1
    time.sleep(0.1)
