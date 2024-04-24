FROM python:3.11

RUN mkdir docker/
WORKDIR docker/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /docker/*.sh