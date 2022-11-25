DATE:=$(shell date +'%y%m%d%H%M%S')
BOT_NAME:=khg-bot
build:
	docker build -t $(BOT_NAME):$(DATE) -t $(BOT_NAME):latest .

run:
	docker run -d $(BOT_NAME):latest
