pConnectionString = "Endpoint=sb://soumyas-iot-hub-event-hub.servicebus.windows.net/;SharedAccessKeyName=iothubroutes_SoumyasHub;SharedAccessKey=wBf/GWNSRSNGM7ObjmIrlR17/3gAkGFkO1+voUTuEY0=;EntityPath=eventsoumyasiothub"
import asyncio
from azure.eventhub.aio import EventHubConsumerClient

# from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

from datetime import datetime
import json
# import matplotlib.pyplot as plt
import csv

from isodate import date_isoformat
global file
async def on_event(partition_context, event):
    # Print the event data.
    dataBodyRx = event.body_as_str(encoding='UTF-8')
    print(dataBodyRx)
    try:
        file = open("test/Test.csv","a")
        dictData = (json.loads(str(dataBodyRx)))
        print(dictData["time"])
        print(dictData["data"])
        print(dictData["device"])
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        dateTimeSent = datetime.strptime(dictData["time"],date_format)
        dateTimeNow = datetime.now().strftime(date_format)
        timeRequired = datetime.strptime(dateTimeNow,date_format) - dateTimeSent;
        # plt.scatter(str(dateTimeNow),str(timeRequired))
        # plt.show()
        file.write(dictData["time"]+","+dictData["data"]+","+dictData["device"]+","+str(timeRequired)+"\n")
        print(timeRequired)
        
    except Exception as e:
        print(e)
    #print("Received the event: \"{}\" at time : "+str(dateTimeNow)+" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    # checkpoint_store = BlobCheckpointStore.from_connection_string("AZURE STORAGE CONNECTION STRING", "BLOB CONTAINER NAME")
    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(pConnectionString, consumer_group="$Default", eventhub_name="eventsoumyasiothub")
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())