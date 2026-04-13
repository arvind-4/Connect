# Connect

An Open Source Django website Powered by Python, Django-Channels, WebRTC, Tailwind CSS, React, Postgres and Docker.

### Get the Code

#### Clone Repository

```
mkdir Connect
cd Connect
git clone https://github.com/Arvind-4/Connect.git .
```

- Create Virtual Environment for Python

```
pip install virtualenv
python -m venv .
```

- Activate Virtual Environment

```
source bin/activate
```

- Install Dependencies

```
pip install -r web/requirements.txt
```

- db migrations

```
python web/manage.py makemigrations
python web/manage.py migrate
```

- Run Server

```
python web/manage.py runserver
```

- Run Frontend

```
cd frontend/
yarn dev:react
```

**Hot Reload Enabled for React in Django Template**

Visit [127.0.0.1:8000](http://127.0.0.1:8000) .

- Having Docker :

```
docker-compose up --build
```
