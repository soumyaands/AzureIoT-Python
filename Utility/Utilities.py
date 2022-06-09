
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import ExportImportDevice, AuthenticationMechanism, SymmetricKey


def printDeviceInfo(dataToPrint,device):
    print(dataToPrint + ":")
    print("device_id                      = {0}".format(device.device_id))
    print("authentication.type            = {0}".format(device.authentication.type))
    print("authentication.symmetric_key   = {0}".format(device.authentication.symmetric_key))
    print("authentication.x509_thumbprint = {0}".format(device.authentication.x509_thumbprint))
    print("connection_state               = {0}".format(device.connection_state))
    print("connection_state_updated_tTime = {0}".format(device.connection_state_updated_time))
    print("cloud_to_device_message_count  = {0}".format(device.cloud_to_device_message_count))
    print("device_scope                   = {0}".format(device.device_scope))
    print("etag                           = {0}".format(device.etag))
    print("generation_id                  = {0}".format(device.generation_id))
    print("last_activity_time             = {0}".format(device.last_activity_time))
    print("status                         = {0}".format(device.status))
    print("status_reason                  = {0}".format(device.status_reason))
    print("status_updated_time            = {0}".format(device.status_updated_time))
    print("")