FROM python:3.10.8

WORKDIR /usr/src

COPY ["requirements.txt", "."]

RUN pip install -r ./requirements.txt

EXPOSE 8000

#CMD ["node", "index.js"]
