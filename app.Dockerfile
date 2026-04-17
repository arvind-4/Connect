FROM oven/bun:1.3.12-alpine@sha256:26d8996560ca94eab9ce48afc0c7443825553c9a851f40ae574d47d20906826d AS base
WORKDIR /tmp

COPY package.json bun.lock turbo.json ./
COPY apps ./apps
COPY packages ./packages
COPY public ./public
COPY templates ./templates

RUN bun install --frozen-lockfile
RUN bun run build

FROM python:3.9.24-alpine@sha256:f4b6234fd621f280bce58b3f4e8669d92346f36f2f73d8cc912f4a3aed28cb5d AS web-build

WORKDIR /usr/src/connect

COPY --from=ghcr.io/astral-sh/uv:0.10.9 /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --locked

COPY --from=base /tmp/public ./public
COPY backend ./backend
COPY manage.py ./
COPY templates ./templates
COPY commands ./commands
COPY manage.py ./

RUN /usr/src/connect/.venv/bin/python manage.py collectstatic --no-input

FROM python:3.9.25-alpine3.22@sha256:c99b6eb43b3ac4d750db3d6e8b22268d5ea9a99deead7218ce3deda7f2ca029c AS runner

WORKDIR /usr/src/connect
COPY --from=web-build /usr/src/connect/.venv /usr/src/connect/.venv
COPY --from=web-build /usr/src/connect/staticfiles_build /usr/src/connect/staticfiles_build
COPY --from=web-build /usr/src/connect/backend /usr/src/connect/backend
COPY --from=web-build /usr/src/connect/templates /usr/src/connect/templates
COPY --from=web-build /usr/src/connect/commands /usr/src/connect/commands
COPY --from=web-build /usr/src/connect/manage.py /usr/src/connect/manage.py

RUN chmod +x /usr/src/connect/commands/docker-start.sh
