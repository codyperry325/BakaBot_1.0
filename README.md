### Local environment setup
This repo uses pre-commit to
```
$ python3.9 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ pre-commit install
```



### Build and Run
The Dockerfile will build a container with the default name `khg-bot`, use the `BOT_NAME=<your bot name>` (without the brackets) parameter for the make command to use a custom name for the container image.
```
$ make [BOT_NAME=<your bot name>] build
$ make [BOT_NAME=<your bot name>] run
```
