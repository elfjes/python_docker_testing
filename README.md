# Testing Docker containers using pytest
This is a small template project for testing your docker container. It uses `pytest` and the 
`pytest_docker_compose` plugin

## Requirements
- A Docker engine

## Usage
```bash

# install the dev requirements (Recommended to use a virtualenv)
pip install -r requirements-dev.txt

# run the tests
cd tests && pytest -v
```
