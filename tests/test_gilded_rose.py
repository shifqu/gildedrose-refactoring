"""Module containing all GildedRose related fixtures, tests and test-utils."""
import json
from pathlib import Path

import pytest

from gildedrose_refactoring.gilded_rose import GildedRose, Item


@pytest.fixture(name="conjured_item")
def fixture_conjured_item() -> Item:
    return Item("Conjured health potion", 5, 40)


@pytest.fixture(name="conjured_item_progress_multiple_days")
def fixture_conjured_item_progress_multiple_days(conjured_item: Item) -> dict[str, Item]:
    name = conjured_item.name
    return {
        "0": Item(name, 5, 40),
        "1": Item(name, 4, 38),
        "2": Item(name, 3, 36),
        "3": Item(name, 2, 34),
        "4": Item(name, 1, 32),
        "5": Item(name, 0, 30),
        "6": Item(name, -1, 26),
        "7": Item(name, -2, 22),
    }


@pytest.fixture(name="items")
def fixture_items() -> list[Item]:
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]


@pytest.fixture(name="items_after_update")
def fixture_items_after_update() -> list[Item]:
    return [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
        Item(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50),
        Item(name="Conjured Mana Cake", sell_in=2, quality=4),
    ]


@pytest.fixture(name="items_json")
def fixture_items_json() -> dict[str, list[dict]]:
    path = Path(__file__).parent / "fixtures" / "gilded_items.json"
    assert path.is_file(), f"Expected {path} to be an existing file."
    with path.open() as fp:
        items_json: dict[str, list[dict]] = json.load(fp)

    return items_json


def destructure(item: Item):
    fields = ["name", "sell_in", "quality"]
    return {field: getattr(item, field) for field in fields}


def assert_items_eq(items: list[Item], other_items: list[Item]) -> None:
    """Assert that items and other_items are equal.

    For an item to be equal to another, their `name`, `sell_in` and `quality` should be equal.
    """
    for item1, item2 in zip(items, other_items, strict=True):
        _assert_item_eq(item1, item2)


def _assert_item_eq(item1: Item, item2: Item) -> None:
    assert item1.name == item2.name
    assert item1.sell_in == item2.sell_in
    assert item1.quality == item2.quality


def test_update_quality(items: list[Item], items_after_update: list[Item]) -> None:
    GildedRose(items).update_quality()
    assert_items_eq(items, items_after_update)


def test_update_multiple_days(items: list[Item], items_json: dict[str, list[dict]]) -> None:
    result: dict[str, list[dict]] = {}
    for day in range(17):
        day_str = str(day)
        result[day_str] = [destructure(item) for item in items]
        GildedRose(items).update_quality()

    result_len = len(result)
    items_json_len = len(items_json)
    assert result_len <= items_json_len, (
        f"The length of the result ({result_len}) should be less or equal to the length of the "
        f"fixture ({items_json_len}). hint: try to lower the day-range in this test."
    )

    for key in result.keys():
        i1 = [Item(**item) for item in result[key]]
        i2 = [Item(**item) for item in items_json[key]]
        assert_items_eq(i1, i2)


def test_item_repr():
    item = Item("Test", 1, 1)
    assert str(item) == "Test, 1, 1"


def test_conjured_items(conjured_item: Item, conjured_item_progress_multiple_days: dict[str, Item]):
    items = [conjured_item]
    for day in conjured_item_progress_multiple_days.keys():
        item = items[0]
        _assert_item_eq(item, conjured_item_progress_multiple_days[day])
        GildedRose(items).update_quality()
