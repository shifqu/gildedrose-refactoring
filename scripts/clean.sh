#!/bin/bash
set -euxo pipefail

poetry run isort gildedrose_refactoring/ tests/
poetry run black gildedrose_refactoring/ tests/
