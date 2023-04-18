# Getting start

## Standard way

1. Install Python 3.10
2. Go to project's folder
3. From the `tool.poetry.dependencies` group in `pyproject.toml`, install all dependencies (except python) by command `pip install`
4. Run tests by command `python -m pytest`

## Poetry way

1. Install Python 3.10
2. Install Poetry: https://python-poetry.org/docs/#installation
3. Go to project's folder
4. Run `poetry install`
5. Activate your virtual environment by command `poetry shell`
6. Run tests by command `python -m pytest`
