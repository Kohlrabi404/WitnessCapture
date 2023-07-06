import yagmail
import json
    
class Mailer :
    def __init__(self) :
        self.data = self.get_data()
        self.yag = yagmail.SMTP(self.data.get("sender"), oauth2_file='creds.json')
        
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

    def send_email(self, file_path) :
        self.yag.send(to=self.data.get("to"),
                      subject=file_path,
                      contents=file_path)