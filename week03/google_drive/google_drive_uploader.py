from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveUploader():
    def upload_to_google_drive(self, file_path, folder_id=None):
        # Authenticate and create the PyDrive client
        gauth = GoogleAuth()

        # Try to load saved client credentials
        gauth.LoadCredentialsFile("week03/google_drive/credentials/mycreds.txt")

        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()

        # Save the current credentials to a file
        gauth.SaveCredentialsFile("week03/google_drive/credentials/mycreds.txt")

        drive = GoogleDrive(gauth)

        # Create a GoogleDriveFile instance with the file path
        gfile = drive.CreateFile({'title': file_path.split('/')[-1]})

        # Set the content of the file
        gfile.SetContentFile(file_path)

        # If a folder ID is provided, set the parent folder
        if folder_id:
            gfile['parents'] = [{'id': folder_id}]

        # Upload the file
        gfile.Upload()

        print(f"File {file_path} uploaded successfully with file ID {gfile['id']}")

if __name__ == "__main__":
    gd_upload = GoogleDriveUploader()

    file_path = 'week03/google_drive/asset_upload/head.obj'
    folder_id = '18MXDhj8jLLuwGHMxX4vvVsKgTk-IjXCn'  # Optional: ID of the folder where you want to upload the file
    
    gd_upload.upload_to_google_drive(file_path, folder_id)