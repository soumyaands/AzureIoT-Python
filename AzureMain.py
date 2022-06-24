# from tokenize import group
# import DeviceCreation as DC
# import concurrent
# DC.addDevice("Test",10)
# DC.getDevice(10)
# for i in range(0, 10):
#     DC.deleteDevice("device_Test_"+str(i))

import SendData as SD
from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
if __name__ == '__main__':
    #freeze_support()
    info('main line')
    p = Process(target=SD.sendDataToDevice, args=(10,10))
    p.start()
    p.join()
#SD.split_processing(10,10,1)
#SD.sendDataToDevice(10,10);