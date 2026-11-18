FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
COPY ejemplo/ .
=======
COPY . .
>>>>>>> b7bca2ddc468f3596012497fd7b867cd7cdca0c9

RUN mkdir -p /data

EXPOSE 8000

CMD ["gunicorn", "ejemplo.wsgi:application", "--bind", "0.0.0.0:8000"]
