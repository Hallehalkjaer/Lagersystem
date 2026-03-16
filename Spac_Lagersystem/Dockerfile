FROM python:3.12.3

WORKDIR /app

COPY backend.py backend.py
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./backend.py"]