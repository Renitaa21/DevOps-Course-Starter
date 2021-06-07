# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Trello and the API Key and Tokens

We're going to be using Trello's API to fetch
and save to-do tasks. In order to call their
API, you need to first create an account https://trello.com/signup , then
generate an API key and token by following
the instructions here. https://trello.com/app-key 
Add these to the .env file and ensure this file is in the gitignore file so this does not get committed. 

You also need to get the list ids for the todo, doing and done lists by clicking on a card in each of these lists in trello , then click on Share and then Export JSON. Within the JSON response you can find the idList example - "idList":"6047ecb966a18d23e8029cd2". Add these ids into the .env file too. 

## Testing

Install pytest via pip or another package manager. example $ pip install pytest
to run pytest simply run the command from the root of your project eg $pytest
Here's how it works:
1. You write test functions that include assertions.
2. You run pytest.
3. Pytest automatically discovers your test functions, runs them,
and reports any failed assertions.

To run the tests individually click on the conical flask icon named Testing and you should be able to see all your individual tests there after expanding the structure. Click on the play icon in front of individual tests to run them. 

to run the tests as a whole you can cick on the play icon next to you test file and that should run all the tests in that file. If you see a green tick all have passed else if you see a red cross at least one test case has failed

To run these tests directly from a command line use poetry run pytest. There are dependancies such as Firefox and Geckodriver that are needed to run the end to end tests successfully. To run the selenium tests you can use poetry run pytest test_selenium. For Geckodriver - you will need to download the Gecko Driver executable and place it in the root of your project - the selenium driver just uses this under the hood. Install firefox as this is a dependancy.