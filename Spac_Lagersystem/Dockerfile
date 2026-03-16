FROM python:3.12.3

WORKDIR /app

# Backend code
COPY backend.py backend.py
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Frontend code
COPY frontend frontend

CMD ["flask", "run", "--host=0.0.0.0"]