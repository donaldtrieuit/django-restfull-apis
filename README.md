# django-restfull-apis

## Requirements
 - Python 3.9
 - Postgresql

___
## Setup using Docker
### Prerequisites
This required you having [docker](https://docs.docker.com/get-docker/)
 and [docker-compose](https://docs.docker.com/compose/install/) installed and running.

### Initial setup
Make a copy of the `docker-compose.yml.sample` file. Optionally, make copies of the sample environment files if needed.
```bash
cp docker-compose.yml.sample docker-compose.yml
```

We used [django-environ](https://django-environ.readthedocs.io/en/latest/) package to manage the environment variable, so we need to make a copy of the `.env.sample` file
```bash
cp base/settings/.env.example base/settings/.env
```

### Building and running the application locally
To build and run docker images with the code checked out on your machine, run the following from the root directory of the project
```bash
# Build the app
docker-compose build

# Run the container
docker-compose up
```
- This will start docker services included: Postgresql, Redis, Celery worker, Celery Beat worker and Django server
- You can then view the app by navigating to http://127.0.0.1:8000/admin in your browser

___
### Usage
Set up initial user

```bash
# Connect to the docker container
docker exec -it django-restfull-apis_web_1 /bin/bash

# Create a superuser
python manage.py createsuperuser
```
___
### Running tests
Run test suite
```
$ make test
```

Check sorting on imports
```
make isort
```

Check code formating
```
make flake8
```

Autoformat code
```
make autopep8
```

Audit code
```
$ make flake8
```

Run checks
```
$ make checks
```

Run all tests and code audit tools
```
$ make local-ci
```
