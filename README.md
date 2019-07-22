# Testing Docker containers using pytest
This is a small template project for testing your docker container. It uses `pytest` and the 
`pytest_docker_compose` plugin. While this project features a small Flask, your own project doesn't
need to be a Python app at all. It doens't even need to be a web service. It might be useful 
though for it to be some kind of service, with a port exposed so that you can interface with it.

## Requirements
- A Docker engine

## Usage
```bash

# install the dev requirements (Recommended to use a virtualenv)
pip install -r requirements-dev.txt

# run the tests
pytest -v
```
