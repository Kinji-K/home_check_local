import httplib2
import os.path
import json
import requests
import os
from googleapiclient import discovery
from oauth2client import client
from oauth2client.file import Storage
from oauth2client import tools

class DriveUpload:

    # コントラクタ（認証とファイル名の設定）
    def __init__(self,file_title):
        SCOPES = ["https://www.googleapis.com/auth/drive"]
        self.service = None
        self.drives = []
        creds = None

        store = Storage("/opt/working/drive_credential.json")
        creds = store.get()

        http = creds.authorize(httplib2.Http())
        self.service = discovery.build('drive','v3',http=http)
        self.line = file_title
        
        result = self.service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='house'").execute()
        self.folder = result.get("files",[])[0]["id"]

        result = self.service.files().list(q="name='"+ self.line + "' and '" + self.folder + "' in parents").execute()
        self.check = result.get("files",[])

    # ファイルアップロード
    def FileUpload(self):
        try:
            print(self.check[0]["id"])
        except IndexError:
            metadata = {'name': self.line, 'parents':[self.folder]}
            self.file = self.service.files().create(body=metadata,media_body="").execute()

    # ファイルデリート
    def FileDelete(self):
        try:
            print(self.check[0]["id"])
            self.file = self.service.files().delete(fileId=self.check[0]["id"]).execute()
        except IndexError:
            pass

    def CheckOut(self):
        try:
            print(self.check[0]["id"])
            return 1
        except IndexError:
            return 0

if __name__ == "__main__":
    drive = DriveUpload("aaa")
    drive.FileUpload()