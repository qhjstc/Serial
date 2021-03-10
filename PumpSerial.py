"""
This is Pump project !
It can plot data from stm32
"""

import serial
import time
import matplotlib.pyplot as plt
ser = 'NULL'

def main():
    # print("Build a serial!")
    # ser = serial.Serial()
    # while 1:
    #     try:
    #         ser = serial.Serial('COM6', 115200)  # windows系统使用com1口连接串行口
    #     except Exception as e:
    #         print(".")
    #         time.sleep(0.5)
    #         continue
    #     break
    # ser.parity = serial.PARITY_NONE
    # ser.open()
    # print("Success config a Serial")
    pumpdata = range(128)
    fig = plt.figure(figsize=(9, 4.5))  # creat a panel
    plt.scatter(marker='o', c='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(range(128))
    plt.show()



if __name__ == "__main__":
    print("Hello This is Pump project!")
    main()





