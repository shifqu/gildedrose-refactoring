# gildedrose-refactoring
An attempt at the Gilded Rose Refactoring Kata.

---

[![Test Status](https://github.com/shifqu/gildedrose-refactoring/actions/workflows/test.yml/badge.svg)](https://github.com/shifqu/gildedrose-refactoring/actions?query=workflow%3ATest)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/gildedrose-refactoring/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat)](https://pycqa.github.io/isort/)

---
## System requirements
gildedrose-refactoring requires [Python 3.10+](https://www.python.org/downloads/) and [Poetry 1.0+](https://python-poetry.org/docs/).

##### Tip: The recommended IDE is [VSCode](https://code.visualstudio.com/). A `.vscode` directory is provided with a file containing recommended extensions alongside default launch configurations and workspace specific settings.

## Installation
gildedrose-refactoring uses Poetry to manage the virtual environments. This makes installing the application locally a breeze.  

`poetry install`

`poetry run pip install --upgrade pip`

`poetry update`

`poetry run pre-commit install -t pre-commit -t pre-push`

##### Tip: This repository ships with an install script (./scripts/install.sh) which will run above commands for you

## Run the tests
The tests can be run locally, but this means you would need to install python 3.10, poetry and follow steps above to install the application.

If you have docker installed, this repository includes a Dockerfile which just builds and installs the project inside the container.

### Run locally
`./scripts/done.sh`

OR
### Build the container
`docker build .`

### Run a disposable container and open a bash shell inside
`docker run --rm -it <container-id> bash`

### To prevent the container from being disposed, run the following instead
`docker exec -it <container-id> bash`

---
[Browse GitHub Code Repository](https://github.com/shifqu/gildedrose-refactoring/)

---
