FROM python:3.10.12-bookworm

WORKDIR /app

RUN apt-get -y update && apt-get -y upgrade \
    && apt-get install -y ffmpeg
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:85"]
