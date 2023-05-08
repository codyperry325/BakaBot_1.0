DATE:=$(shell date +'%y%m%d%H%M%S')
BOT_NAME:=khg-bot
REPO_NAME:=git.bhaanukaul.com/bhaanukaul
build:
	docker build -t $(REPO_NAME)/$(BOT_NAME):$(DATE) -t $(REPO_NAME)/$(BOT_NAME):latest .

push:
	docker push -t $(REPO_NAME)/$(BOT_NAME):latest

run:
	docker run -d $(REPO_NAME)/$(BOT_NAME):latest
