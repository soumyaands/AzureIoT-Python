from azure.iot.hub import IoTHubRegistryManager as IHRM
from Utility.Utilities import DEVICE_CONNECTION_STRING as DCS
from DeviceCreation import getDevice
import threading
import time
import random
from azure.iot.device import IoTHubDeviceClient
iothub_connection_string = "HostName=Safiya-IoT-Hub.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=dWEhcgJxlIQoav2EjWOKSWJNpt403bCzMfsVAfTNey0=";
def sendDataToDevice(numberOfDevices,numberOfRequests):
    HostName = "Safiya-IoT-Hub.azure-devices.net"
    ihrm = IHRM.from_connection_string(iothub_connection_string)
    #try:
    deviceList = getDevice(numberOfDevices)
    if deviceList:
        devicePos = 0
        for device in deviceList:
            deviceId = device.device_id
            devicePrimaryKey = device.authentication.symmetric_key.primary_key
            deviceConnectionString = DCS.format(HostName,deviceId,devicePrimaryKey)
            print(deviceConnectionString)
            messageToSend = "{'time':'"+str(time.localtime())+"','data':'"+str(random.randint(1,10))+"'}"
            print(messageToSend)
            iothubdeviceclient = IoTHubDeviceClient.create_from_connection_string(deviceConnectionString)
            #iothubdeviceclient.send_message(messageToSend)
            threading.Thread(target=iothubdeviceclient.send_message,args=(messageToSend))
            # ihrm.send_c2d_message(deviceId,messageToSend)
            # threading.Thread(target = ihrm.send_c2d_message, args=(deviceId,messageToSend))
            # # IHRM.sendMessage(messageToSend)
    # except Exception as e:
    #     print(e)