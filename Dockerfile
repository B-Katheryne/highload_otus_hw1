FROM python:3.12.7

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt ./

RUN pip3 install --upgrade pip --no-cache-dir && pip3 install -r requirements.txt --no-cache-dir

COPY ./alembic.ini ./start.sh ./
COPY ./migration ./migration
COPY ./src ./src

CMD ./start.sh
