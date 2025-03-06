from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_asset(name, file):
    gauth = GoogleAuth()

    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    folder_id = "18MXDhj8jLLuwGHMxX4vvVsKgTk-IjXCn"

    file = drive.CreateFile({"title": name, "parents": [{"id": folder_id}]})
    file.SetContentFile(file)
    file.Upload()
    print(f"Asset < {name} > was successfully uploaded.")