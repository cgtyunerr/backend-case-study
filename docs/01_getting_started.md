# Getting Started

## Table of contents
* [Installation](#installation)
* [Configuration](#configuration)
* [Running](#running)

## Installation

Make sure that you have installed Poetry with Python 3.10.

Activate the virtual environment of Poetry:
```bash
poetry shell
```

To install dependencies of the project:
```bash
make install
```

or

```bash
poetry install
```

## Configuration

You need to export environment variables to run emp-backend.
You can check the `.env.test` file for the required environment variables.

You can define them in several ways:

  * manually using `export`
  * sourcing a script with the `export` commands

## Running

### Development

For development, you can run the project with:

- For healthAI
```bash
uvicorn app.healthai.src.api.main:api --reload --log-level debug
```

or

```bash
make runh
```

- For travelAI
```bash
uvicorn app.travelai.src.api.main:api --reload --log-level debug
```

or

```bash
make runt
```

You can then access the API at <http://localhost:8000> and the [Swagger UI](https://swagger.io/tools/swagger-ui/) (interactive API documentation) at <http://localhost:8000/docs>.
