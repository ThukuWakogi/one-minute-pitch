# one-minute-pitch

This app enables a user to share and review pitches

## author

Timothy Oliver [@ThukuWakogi](https://github.com/ThukuWakogi)

## features

1. Users can login or and register into the website.
2. users can read and write pitches

## SetUp

To view a demo of the application, click [here](https://https://thukuwakogi-one-minute-pitch.herokuapp.com/).

The source code for this application can be accessed. For it to run, you will need [Python](https://www.python.org/) and an api key from [News API](https://newsapi.org/)

a copy of the source code can be gotten through:

- downloading the zip from github.
- opening a terminal in the preferred directory then entering `git clone https://github.com/ThukuWakogi/news-highlight.git`
- using a git client such as [Github desktop](https://desktop.github.com/) or [GitKraken](https://www.gitkraken.com/)

### installing

#### windows

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python -m venv virtual`
* Activating the virtual environment may change based on the terminal or shell being used.
* For command prompt, enter `virtual\Scripts\activate` or simply type in activate.
* For powershell, the execution policy should be bypassed for the script to run. This can be done by entering `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then proceeding on with entering .`.\virtual\Scripts\Activate.ps1`
* Install packages. `pip install -r requirements.txt`
* Setting environment variables differs with the terminal or shell being used
* 
* initiate database the database `python3.6 manage.py db upgrade`
* then start the server `python manage.py server`

#### unix

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python3.x -m venv --without-pip virtual` replace x with version in host machine, preferably version v3.6 for this project
* Activate the virtual environment `source virtual/bin/activate`
* Download pip into the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install packages. `pip install -r requirements.txt`>`
* initiate database the database `python3.6 manage.py db upgrade`
* start the server `python3.x manage.py server`

## Development tools
* [Python](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Material](https://material.io/)
* [Google fonts](https://fonts.google.com/)
* HTML
* CSS

## license
This project is under the MIT license. click [here](https://github.com/ThukuWakogi/one-minute-pitch/blob/master/LICENSE) for more details
