from azure.storage.blob import BlobClient

blob = BlobClient("https://Safiya.Anjum.blob.core.windows.net",container_name="safiya-blob-container",blob_name="safiyaiotblob",credential="ZhbjE3dkRxOlitllxw/MCYzkWe2+sVaL+lJEg/6lEz2LKMS5oVbGtrq9SFbw1iHsH+YWNvaib3JV+AStuYGHsA==")

with open("example.csv", "wb") as f:
    data = blob.download_blob()
    data.readinto(f)