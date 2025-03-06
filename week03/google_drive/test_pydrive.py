from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json


gauth = GoogleAuth()

gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

folder_id = "18MXDhj8jLLuwGHMxX4vvVsKgTk-IjXCn"
with open("week03/google_drive/asset_list.json", "r") as asset_list:
    assets = json.load(asset_list)

for asset in assets.values():
    # print(asset["name"])
    # print(asset["local_path"])

    file = drive.CreateFile({"title": asset["name"], "parents": [{"id": folder_id}]})
    file.SetContentFile(asset["local_path"])
    file.Upload()
    print(f"Asset   {asset["name"]}   was successfully uploaded.")

# file = drive.CreateFile({"title": "head.obj"})

# file.SetContentFile("week03/google_drive/asset_upload/head.obj")

# file.Upload()