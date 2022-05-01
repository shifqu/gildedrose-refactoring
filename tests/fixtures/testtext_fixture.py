"""A fixture to be used with testtexts.

References
----------
See `https://texttest.org/` for more information on texttests.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from gildedrose_refactoring.gilded_rose import GildedRose, Item
from tests.test_gilded_rose import destructure


def _write(items):
    utc_now_timestamp = int(datetime.now(tz=timezone.utc).timestamp())
    path = Path(__file__).parent / f"gilded_items_{utc_now_timestamp}.json"
    if path.exists():
        input_ = input(f"The file {path} already exists, ok to overwrite? (y/N)")
        if input_.lower() not in ["yes", "y"]:
            print("User aborted the write, file exists.")
            return

    with path.open("w") as fp:
        json.dump(items, fp)


if __name__ == "__main__":
    print("OMGHAI!")
    items = [
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

    days = 17
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    result: dict[str, list[dict]] = {}
    for day in range(days):
        day_str = str(day)
        result[day_str] = [destructure(item) for item in items]
        print(f"-------- day {day_str} --------")
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()

    if os.environ.get("WRITE"):
        _write(result)
