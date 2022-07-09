import base64
import os
import uuid
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import SymmetricKey, AuthenticationMechanism, ExportImportDevice
from Utility import Utilities
iothub_connection_string = "HostName=SoumyasHub.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=s21HMIgS8616PdgkDRm8GeplN1Hp7nKgBBSPwCpke/A=";
#os.getenv("IOTHUB_CONNECTION_STRING")
global iothub_registry_manager #= IoTHubRegistryManager.from_connection_string(iothub_connection_string)
def addDevice(deviceFamily,numberOfDevices):
    deviceList = []
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(iothub_connection_string)
    try:
        for i in range(0,numberOfDevices):
            primaryKey = base64.b64encode(str(uuid.uuid4()).encode()).decode()
            secondaryKey = base64.b64encode(str(uuid.uuid4()).encode()).decode()
            symmetricKey = SymmetricKey(primary_key=primaryKey,secondary_key=secondaryKey)
            authentication = AuthenticationMechanism(type="sas",symmetric_key=symmetricKey)
            device = ExportImportDevice(id="device_"+deviceFamily+"_"+str(i),status="enabled",authentication=authentication)

            #DEVICE_CREATION
            device.import_mode="create"
            deviceList.append(device)
        iothub_registry_manager.bulk_create_or_update_devices(deviceList)
    except Exception as e:
        print("Some Exception Description : {0}".format(e))
    iothub_registry_manager=None
    return deviceList

def getDevice(numberOfDevices):
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(iothub_connection_string)
    try:
        deviceList = iothub_registry_manager.get_devices(numberOfDevices)
        if deviceList:
            devicePos = 0
            for device in deviceList:
                #Utilities.printDeviceInfo("{0}th device".format(devicePos),device)
                devicePos+=1
            return deviceList;
        else:
            print("No Devices Found")
    except Exception as e:
        print("Some Exception Description : {0}".format(e))
    

# def deleteDevice(deviceName):
#     try:
#         authentication = AuthenticationMechanism(type="sas",symmetric_key=symmetricKey)
#         device = ExportImportDevice(id=deviceName,status="enabled",authentication=authentication)
#         device.import_mode = "delete"
#         iothub_registry_manager.bulk_create_or_update_devices(device)
#     except Exception as e:
#         print("Some Exception Description : {0}".format(e))