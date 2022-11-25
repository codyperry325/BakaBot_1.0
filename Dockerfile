FROM python:3.9-alpine

RUN mkdir -p /app
WORKDIR /app
ADD bot.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]
