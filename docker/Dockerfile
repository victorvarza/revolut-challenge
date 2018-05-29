FROM python:3.6-alpine3.7

LABEL \
  app="revolut" \
  layer="frontend" \
  git-url="https://github.com/victorvarza/revolut-challenge.git"

ENV REDIS_HOST='redis'
ENV REDIS_PORT=6379

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "python", "revolut.py" ]
