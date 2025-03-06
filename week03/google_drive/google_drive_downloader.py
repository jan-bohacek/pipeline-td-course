import sys
import requests
import json

class GoogleDriveDownloader():
    def download_file_from_google_drive(self, file_id, destination):
        URL = "https://drive.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={"id": file_id}, stream=True)
        token = self.get_confirm_token(response)

        if token:
            params = {"id": file_id, "confirm": token}
            response = session.get(URL, params=params, stream=True)

        self.save_response_content(response, destination)


    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

        return None


    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


    def download(self, file_id, destination):
        if len(sys.argv) >= 3:
            file_id = sys.argv[1]
            destination = sys.argv[2]
        else:
            file_id = file_id
            destination = destination
        self.download_file_from_google_drive(file_id, destination)


if __name__ == "__main__":
    gd_download = GoogleDriveDownloader()

    destination = "google_drive/asset_download"

    with open("week03/google_drive/asset_list.json", "r") as file:
        assets = json.load(file)

    for asset in assets.values():
        print(asset["name"])
        file_id = asset["link"].replace("https://drive.google.com/file/d/", "").replace("/view?usp=drive_link", "")
        gd_download.download(file_id, f"{destination}/{asset["name"]}.{asset["format"]}")

    print("Done!")