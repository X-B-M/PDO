import os
import time


def prn_line(offset_x):
    str_height, str_width = os.popen('stty size', 'r').read().split()
    height = int(str_height)
    width = int(str_width)
    if offset_x[0] >= width:
        offset_x[0] = 0
    tmp_str = " " * offset_x[0]
    tmp_str = tmp_str + "\033[32m" + "*" + "\033[0m"
    tmp_str = tmp_str + " " * (width - offset_x[0])
    print("\033[10;0H", end='')
    print(tmp_str)


x = [0]
# x[0] = int(input("Введите X :"))
while 1:
    prn_line(x)
    x[0] = x[0] + 1
    time.sleep(0.1)
