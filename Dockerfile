FROM python:3.9-alpine
RUN mkdir -p /app
RUN apk --no-cache add gcc musl-dev
WORKDIR /app
ADD bot/ .
ADD requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]
