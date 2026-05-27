FROM python:3.9-slim


WORKDIR /app

RUN pip install requests

# Копируем твой скрипт внутрь
COPY updater.py .

# Команда для запуска
CMD ["python", "updater.py"]
