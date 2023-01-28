# elastic-fastapi-test

## Sections
- [elastic-fastapi-test](#elastic-fastapi-test)
  - [Sections](#sections)
    - [Requirements:](#requirements)
  - [📦 Installation](#-installation)
  - [⚡Usage](#usage)
    - [Script](#script)
    - [API Server](#api-server)
    - [Testing](#testing)


### Requirements:
 - Python3.10 or higher

## 📦 Installation

```bash
poetry install
```
You can also install packages from `requirements.txt` file

## ⚡Usage

### Script

Run `python3 app/script.py` to fill elasticsearch datastorage with data from `test.json` file


### API Server
1. Set your elasticsearch server credentials in `.env` file like in `.env.example`

2. Start uvicorn server with API using this command:
   ```bash
   python3 app/main.py
   ```
This command is starting the development server on `http://localhost:8000`

### Testing

To run test that valid for data from testing file(`test.json`) just run `pytest` or `poetry run pytest` inside your virtual environment.

- `api_test.py` contains 8 tests for api with and withount queries