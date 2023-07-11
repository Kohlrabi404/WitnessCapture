import yagmail
import json
from picapture import Data
    
class Mailer :
    def __init__(self) :
        self.data = self.get_data()
        self.yag = yagmail.SMTP(self.data.get("sender"), oauth2_file='creds.json')
        self.pi = Data()
        
    def get_data(self) :
        try:
            with open("data.json") as file :
                data = json.load(file)
            
            return data
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON syntax in the file.")
        except Exception as e:
            print("An error occurred while reading the JSON file:", str(e))

    def send_email(self, file_name, file_paths) :
        self.yag.send(to=self.data.get("to"),
                      subject=file_name,
                      attachments=file_paths)
        
    def send_pic_and_vid(self) :
        while True :
            file_name, pic, vid = self.pi.get_pic_and_vid()
            self.send_email(file_name, [pic, vid])