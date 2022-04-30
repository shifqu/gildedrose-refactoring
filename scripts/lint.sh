#!/bin/bash
set -euxo pipefail

poetry run cruft check
find . -not -path '*/\.*' -not -path '*/__*' -not -path '*/tests/*' -type f \( -iname "*md" -o -iname "*txt" \) | poetry run xargs proselint
find scripts/ -type f -not -name '*py' | poetry run xargs shellcheck
poetry run isort --check --diff gildedrose_refactoring/ tests/
poetry run black --check gildedrose_refactoring/ tests/
poetry run pydocstyle gildedrose_refactoring/ tests/
poetry run flake8 gildedrose_refactoring/ tests/
poetry run mypy gildedrose_refactoring/
poetry run bandit -r gildedrose_refactoring/
poetry run safety check
