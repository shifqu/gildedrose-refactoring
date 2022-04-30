"""The main file for when the project is run."""
from argparse import ArgumentParser

from gildedrose_refactoring import version


def main() -> None:
    """Execute the main function for when the project is run."""
    parser = ArgumentParser("gildedrose_refactoring")
    parser.add_argument("--version", action="version", version=version)
    parser.parse_args()


if __name__ == "__main__":
    main()
