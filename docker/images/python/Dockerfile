FROM python:3.9.18-alpine

WORKDIR /app

# install nodemon
RUN apk add nodejs npm
RUN npm install -g npm@10.2.1
RUN npm install -g nodemon

# Install system dependencies for lxml build
RUN apk --no-cache add libxml2 libxml2-dev libxslt libxslt-dev gcc musl-dev

# upgrade pip
RUN python -m pip install --upgrade pip

# dependencies from requirements.txt
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /data

ENTRYPOINT python main.py