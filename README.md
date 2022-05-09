# CS361 - News API Microservice

This microservice is middleware that returns information from NewsAPI.

## Setup
### Running on Windows
These are the steps I've taken to getting venv environment to work on Windows.
I am not an expert, so if you have a better workaround please do so.
- Clone the repository to Pycharm.
  - Use the Terminal > Command Prompt to navigate the next steps:
    - Run in the location you want to create the venv: `python -m virtualenv .`
    - Activate the virtual environment with source `.\scripts\activate`
    - Install virtualvenv with `pip install virtualenv`
    - Run `virtualenv venv`
    - Run `.\venv\scripts\activate`
    - Run `pip install -r requirements.txt`

To end the venv: `deactivate`


### Running on MacOS/Linux
- Clone the repository to Pycharm.
- Use the Terminal to navigate the next steps:
  - Activate the virtual environment with source `./venv/bin/activate`
  - Install dependencies with `pip install -r requirements.txt`
  - You might need to setup the Python interpreter and Flask configuration.
  - Run the program normally.

## Contact
- Please contact me in Discord @Melissa#2838
- Or email me at: peremeli@oregonstate.edu
