FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
#docker run --rm -v $PWD/site_for_attack.txt:/app/site_for_attack.txt python-ddos -t 1000