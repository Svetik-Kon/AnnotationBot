# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем переменную окружения для предотвращения создания .pyc файлов
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . /app/

# Запускаем бота
CMD ["python", "main.py"]
