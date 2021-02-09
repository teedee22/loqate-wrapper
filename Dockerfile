FROM python:2.7-alpine

COPY ./src/loqate.py /app/app.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "-u", "app.py"]