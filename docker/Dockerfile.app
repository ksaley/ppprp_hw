FROM python:3.10.5-slim-buster
WORKDIR /app
COPY ../src/ ./
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]