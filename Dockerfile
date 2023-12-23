
FROM python:3

RUN mkdir -p /usr/src/bot

WORKDIR /usr/src/bot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "botomploy/__main__.py" ]
