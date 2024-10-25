# Citrix Workspace Auto Login

This is a Python automation project that uses Selenium to automatically log into Citrix Workspace.

## Requirements

- Python 3.x
- Selenium

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/Nkhll/citirix-auto-login.git

   cd citrix-auto-login

2. **Install Selenium**
    ```sh
    pip install selenium

3. **Modify config.py**
    Fill your username, password, login_url, download_dir ex. (C:\\Users\\Username\\Downloads)

4. **Run the startup script**
    ```sh
    python startup.py

5. **Recommended : Compile and generate a .exe**
    After a successful compilation, it's recommended to generate a .exe file to avoid running the script multiple times.

    ```sh
    pip install pyinstaller
    pyinstaller --onefile startup.py

6. **Run the exe file**
    Navigate to /dist folder and use startup.exe for auto login.



That should cover the basics. Feel free to customize it further based on your specific requirements.
Raise an issue with details if you run into or reach out to devwork8nikhil@gmail.com.
Don't forget to star this repo if it helped you.

Happy coding! 🚀

