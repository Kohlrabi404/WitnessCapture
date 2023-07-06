# WitnessCapture

---

## Human Presence Detection and Media Capture System

This program is designed to detect human presence within a specified range using computer vision techniques, capture pictures or videos of the detected individuals, and automatically send them via email. 

## Features

- **Human Presence Detection**: Utilizes computer vision algorithms to detect human presence within a specified range, typically using a camera or video feed as input.
- **Media Capture**: Captures images or records videos of the detected individuals once their presence is confirmed.
- **Email Notification**: Automatically sends the captured media files via email to a specified recipient or email address.


## Requirements

- Python 3.x
- picamera
- RPi
- yagmail

## Installation and Usage

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Ensure that you have Python 3.8 or a higher version installed.

3. Navigate to the project directory.

4. It is recommended to create a virtual environment to manage project dependencies.

```bash

    python3 -m venv venv

```
5. Install the required dependencies by running the following code in your terminal

 ```bash

    pip install -r requirements.txt

 ``` 

 6. Activate the virtual environment.

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

7. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

8. A bot mail with OAuth2 Credentials is required. Specific on how to create one in the below link.
[Google OAuth2](https://developers.google.com/identity/protocols/oauth2)

9. Save the credential as creds.json in main folder

10. Set the sender bot email, receipient email in data.json

4. Run the program using

 ```bash
 
    python main.py
    
```

5. The program will continuously monitor the specified range, detect human presence, capture media files when individuals are detected, and automatically send them via email.

## Contributions

Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
