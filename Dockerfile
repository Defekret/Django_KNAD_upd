FROM python:3.11-slim

LABEL maintainer="Defekret"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps for Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg-dev \
    libpng-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY project/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY project /app

RUN python manage.py migrate --run-syncdb 2>/dev/null || true

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=3s --start-period=15s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
