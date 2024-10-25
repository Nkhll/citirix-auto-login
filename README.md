# Citrix Workspace Auto Login

This Python automation project uses Selenium to log into Citrix Workspace automatically.

## Requirements

- Python 3.x
- Selenium
- pyinstaller

## Installation

1. **Clone the repository**
```sh
git clone https://github.com/Nkhll/citirix-auto-login.git

cd citrix-auto-login
```

2. **Install Selenium**
```sh
pip install selenium
```

## Configuration

**Modify config.py**

Fill your `username`, `password`, `login_url`, `download_dir` ex. `(C:\\Users\\Username\\Downloads)`

## Usage

**Run the startup script**
```sh
python startup.py
```

## Additional feature

**Recommended: Compile and generate a .exe**

After a successful compilation, it's recommended to generate a .exe file to avoid running the script multiple times.

```
pip install pyinstaller
pyinstaller --onefile startup.py
```

**Run the exe file**

Navigate to the /dist folder and use startup.exe for auto login.

## Contributing

1. Fork the Project
2. Create a branch for your feature (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


## License
It is distributed under the `BSD 2-Clause License` License. See LICENSE for more information.

## Contact
Nikhil Kumar Srivastava - devwork8nikhil@gmail.com.

That should cover the basics. Feel free to customize it further based on your specific requirements.
Raise an issue with details if you run into
Don't forget to star ⭐ this repo if it helps you.

Happy coding! 🚀

