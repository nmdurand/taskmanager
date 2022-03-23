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