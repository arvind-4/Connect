# Connect

An Open Source Django website Powered by Python, Django-Channels, WebRTC, Tailwind CSS, React, Postgres and Docker.

# Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [bun](https://bun.com/)
- [docker](https://www.docker.com/)

### Set Up in your Local Machine

- Clone the Repo

```bash
mkdir ~/Dev/connect -p
cd ~/Dev/connect
git clone https://github.com/arvind-4/connect.git .
```

- Set up python

```bash
cd ~/Dev/connect
uv sync --all-groups --locked
```

- Set up for UI

```bash
bun install
```

- Run Django Server

```bash
uv run python manage.py runserver
```

- Run Frontend

```bash
bun dev
```

- For Docker Setup

```bash
docker-compose -f compose.yaml uo --build
```

# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.
