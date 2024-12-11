FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY frontend/ /app/frontend/

RUN pip install flask

ENV CONTAINER_NAME=""

EXPOSE 5000

CMD ["python", "app.py"]
