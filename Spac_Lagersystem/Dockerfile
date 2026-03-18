FROM python:3.12.3

WORKDIR /app

# Backend code
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Frontend code
COPY static static
CMD ["python", "app.py"]