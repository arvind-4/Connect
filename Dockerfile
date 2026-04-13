FROM python:3.9.2-slim

COPY . /web
WORKDIR /web

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r ./requirements.txt && \
    chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]