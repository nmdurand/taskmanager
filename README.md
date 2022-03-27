# README

## Installation

### Create a new virtualenv:
    $ python -m venv taskmanager

### Activate virtual environment:
    $ source env/bin/activate

### Install dependencies:
    $ pip install -r requirements.txt

### Run the app
    $ flask run

### Make flask server externally visible
Turn off the debugger by setting the FLASK_DEBUG env variable to false.

Run the app:

    $ flask run --host=0.0.0.0

### Deploy the app in a Docker container 

## Build docker image and create container
    $ docker build -t taskmanager .
    $ docker run -p 5000:5000 --name taskmanager -it taskmanager

open project homepage at url ```localhost:5000```

## Start Docker container
    $ docker start -a taskmanager