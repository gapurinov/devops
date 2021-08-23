# Moscow time
This is a simple app which shows current time at Moscow.
## Installation
Clone this repository
Go to the app_python file
Install Poetry package manager 
```bash
cd app_python
pip install poetry
poetry install
```
## Run
We will run our application using Poetry package manager
```bash
poetry run python main.py
```
## Docker
Also we have an opportunity to run this app using docker.
Firstly, we need to download our docker image from dockerhub
```bash
sudo docker pull gapurinov/simple_app
```
Then we need to run this docker image with command:
```bash
sudo docker run -p 5000:5000 gapurinov/simple_app
```
Finally you can open 'http://127.0.0.1:5000/' on your browser.
