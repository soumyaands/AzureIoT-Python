from azure.iot.hub import IoTHubRegistryManager as IHRM
from Utility.Utilities import DEVICE_CONNECTION_STRING as DCS
from DeviceCreation import getDevice
import threading
import time
import random
import multiprocessing
from azure.iot.device import IoTHubDeviceClient
from datetime import datetime
iothub_connection_string = "HostName=Safiya-IoT-Hub.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=w31yH21GCoNQz6/LBoKtS01iL3qvp0jEXUiwYcRSrHA=";
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
            for i in range(0,numberOfRequests):
                date_format = "%Y-%m-%dT%H:%M:%S.%fZ" 
                dateTimeNow = datetime.now().strftime(date_format)
                messageToSend = "{'time':'"+str(dateTimeNow)+"','data':'"+str(random.randint(1,10))+"'}"
                print(messageToSend)
                iothubdeviceclient = IoTHubDeviceClient.create_from_connection_string(deviceConnectionString)
                iothubdeviceclient.connect()
                iothubdeviceclient.send_message(messageToSend)
                
            #threading.Thread(target=iothubdeviceclient.send_message,args=(messageToSend))
            # ihrm.send_c2d_message(deviceId,messageToSend)
            # threading.Thread(target = ihrm.send_c2d_message, args=(deviceId,messageToSend))
            # # IHRM.sendMessage(messageToSend)
    # except Exception as e:
    #     print(e)
mutex = threading.Lock()                                                   
def split_processing(numberOfDevices,numberOfRequests, num_splits=4):                                      
    split_size = 2#len(items) // num_splits                                       
    threads = []                                                                
    for i in range(num_splits):                                                 
        # determine the indices of the list this thread will handle             
        start = i * split_size                                                  
        # special case on the last chunk to account for uneven splits           
        end = None if i+1 == num_splits else (i+1) * split_size                 
        # create the thread 
        #mutex.acquire()
        process = multiprocessing.Process(target = sendDataToDevice,args=(numberOfDevices,numberOfRequests))
        print(process.is_alive())
        process.start()
        # threads.append(                                                         
        #     threading.Thread(target=sendDataToDevice, args=(numberOfDevices,numberOfRequests)))         
        # threads[-1].start() # start the thread we just created                  
        #mutex.release()

    # wait for all threads to finish                                            
    for t in threads:                                                           
        t.join()        