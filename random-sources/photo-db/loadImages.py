from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

class DownloadImages:
  def auth():
    gauth = GoogleAuth() 
    drive = GoogleDrive(gauth)
    return drive

  def loadfiles(self, folder_id):
    drive = self.auth()
    file_list = drive.ListFile({'q': folder_id + " in parents and trashed=false"}).GetList()
    for i,file1 in enumerate(file_list):
      file1['title'] = f'{i}.jpg'
    for i,file1 in enumerate(file_list):
      file = drive.CreateFile({'id': file1['id']})
      file.GetContentFile(f'{i}.jpg') 
