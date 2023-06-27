# FROM python:3.8.10-alpine
FROM python:3.8.10

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

    
WORKDIR /app

COPY requirements.txt /app

# RUN apk update && apk upgrade
# RUN apk add --no-cache mariadb-connector-c-dev build-base
# RUN apk add --no-cache build-base cmake
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY . /app
# Exponer puerto 5000
EXPOSE 5000

CMD ["python", "index.py"]