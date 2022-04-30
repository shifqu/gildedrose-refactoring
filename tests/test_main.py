"""Tests for the `main` method."""
import subprocess

import pytest

from gildedrose_refactoring import version


@pytest.mark.parametrize(
    ("cmd", "expected_output"),
    [
        ("python -m gildedrose_refactoring --version", version),
        ("python -m gildedrose_refactoring.main --version", version),
    ],
)
def test_main(cmd, expected_output):
    """Test that calling the application from a script with --version returns the version."""
    return_value = subprocess.run(cmd.split(" "), capture_output=True)
    assert return_value.stdout.decode("utf-8").strip() == version
