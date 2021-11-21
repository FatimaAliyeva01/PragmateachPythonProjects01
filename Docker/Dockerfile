FROM python:3.8

WORKDIR /code

COPY . .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

CMD [ "flask", "run" ,  "--host=0.0.0.0","-p","5000"]


