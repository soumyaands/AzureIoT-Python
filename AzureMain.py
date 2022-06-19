from tokenize import group
import DeviceCreation as DC
import concurrent
#DC.addDevice("Test",10)
DC.getDevice(10)
# for i in range(0, 10):
#     DC.deleteDevice("device_Test_"+str(i))


import SendData as SD
SD.split_processing(10,10,10)