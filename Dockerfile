FROM python:3.10-slim

WORKDIR /app

COPY main.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "main.py"]

