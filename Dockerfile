FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements/requirements.txt

EXPOSE 8080
CMD ["gunicorn","-c","gconfig.py","postcode:app"]