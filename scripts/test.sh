#!/bin/bash
set -euxo pipefail

poetry run pytest -s --cov=gildedrose_refactoring/ --cov=tests --cov-report=term-missing "${@-}" --cov-report html
