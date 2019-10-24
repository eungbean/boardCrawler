### WELCOME TO BOARD-CRAWLER!

정인아 안녕?

#### Structure
```
.
├── Output\             # Output goes here
├── src\                # Chromedriver included
├── venv\               # Kind virtual environment for your safety  
├── config.json         # You have to config your system inside this file
├── main.py             # Main Crawler
├── LICENSE             # MIT Licence
└── README.md
```

#### 0. Requirement
* selenium
* request
* bs4
* time
* json

#### Activate Virtual environment

I built venv for you.

```sh
# If you don't have, just install it.
pip install virtualenv virtualenvwrapper

# Activate venv
source venv/bin/activate

# Deactivate venv
deactivate
```

#### 1. config.json

```json
"chrome_version": '77' or '78'
"OS" : 'mac' or 'win' or 'linux'
"TARGET_URL" : 
"LOGIN_FORM" : {
    "userId": "",
    "password": ""
    }
```

#### RUN
```sh
python main.py
```

---
Made by [Eungbean Lee](https://eungbean.github.io)