# Gamehub
`Gamehub` is a video game and gaming merchandise retailer application that leverages the Flask Web Framework.

Table of Contents
========
*  [Features](#features)
*  [Installation](#installation)
*  [Resources](#resources)

## Installation
### Prerequisites :wrench:
| Package | Description |
| --- | --- |
| `git` | [Software for tracking source code changes](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) |
| `pip3` | [Python Package Manager](https://pip.pypa.io/en/stable/installation/) |
| `python3` | [Interpreted, object-oriented, high-level programming language](https://www.python.org) |

This setup was tested on macOS Ventura.

### Step One - Clone Git Repository
```
git clone [git_repository]
cd [git_repository]
```
### Step Two - Install and Activate Virtual Environment
On macOS
```
python3 -m venv venv
source venv/bin/activate
```

On Windows
```
python3 -m venv venv
.\venv\Scripts\activate
```

### Step Three - Install Packages
```
pip install -r requirements.txt
```

### Step Four - Run Flask Application
```
flask run
```

### Step Five - Testing
Open [http://127.0.0.1:8080](http://127.0.0.1:8080) on a browser or open a new terminal and test the API using curl.
```
curl http://127.0.0.1:8080
```
In both instances you should receive a JSON response.
```json
{"hello": "world"}
```

<img src='/assets/localhost_test_screenshot.png?raw=true' title='Default Route Test' width='500' alt='Default Route Test' />

## Features

## Resources
[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
[peewee Documentation](http://docs.peewee-orm.com/en/latest/)