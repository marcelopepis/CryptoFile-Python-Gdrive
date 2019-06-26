from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


class upGdrive:
    def __init__(self, drive):
      self.drive = drive


      
    @staticmethod
    def autenticator():
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        return(drive)


    @staticmethod
    def upload(arquivo, drive):
        with open(arquivo, "r") as file:
            file_drive = drive.CreateFile({'title':os.path.basename(file.name)})
            file_drive.SetContentString(file.read())
            file_drive.Upload()
            #file_drive.GetContentFile('teste_download.txt', mimetype=None)
    



