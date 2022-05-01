"""Module containing the core objects used by the Gilded Rose."""
from dataclasses import dataclass


@dataclass()
class GildedItem:
    """Represent an Item with extra functionality to update the sell_in and quality."""

    name: str
    sell_in: int
    quality: int

    def is_backstagepass(self) -> bool:
        """Check if the item is a backstagepass."""
        if self.name.startswith("Backstage passes"):
            return True
        return False

    def is_better_with_age(self) -> bool:
        """Check if the item's quality should increase over time."""
        if self.name == "Aged Brie":
            return True
        return False

    def is_conjured(self) -> bool:
        """Check if the item's quality should degrade twice as fast."""
        if self.name.startswith("Conjured"):
            return True
        return False

    def is_expired(self) -> bool:
        """Check if the item's sell_in is negative."""
        if self.sell_in < 0:
            return True
        return False

    def is_legendary(self) -> bool:
        """Check if the item is a legendary item."""
        if self.name == "Sulfuras, Hand of Ragnaros":
            return True
        return False

    def update(self) -> None:
        """Update the sell_in and the quality of the item."""
        if self.is_legendary():
            return  # Do not update legendary items

        self._update_sell_in()

        if self.is_backstagepass():
            self._update_backstagepass()
            return

        quality_modifier = 1
        if self.is_expired():
            quality_modifier = 2

        if self.is_better_with_age():
            new_quality = self.quality + quality_modifier
        elif self.is_conjured():
            new_quality = self.quality - (quality_modifier * 2)
        else:
            new_quality = self.quality - quality_modifier
        self._update_quality(new_quality)

    def _update_backstagepass(self) -> None:
        if self.is_expired():
            self.quality = 0
            return
        if self.sell_in >= 10:
            quality_modifier = 1
        elif self.sell_in >= 5:
            quality_modifier = 2
        else:
            quality_modifier = 3
        new_quality = self.quality + quality_modifier
        self._update_quality(new_quality)

    def _update_quality(self, quality: int) -> None:
        if quality < 0:
            self.quality = 0
        elif quality > 50:
            self.quality = 50
        else:
            self.quality = quality

    def _update_sell_in(self) -> None:
        self.sell_in -= 1


class GildedRose:
    """Represent the Gilded Rose Inn."""

    def __init__(self, items: list["Item"]) -> None:
        self.items = items

    def update_quality(self) -> None:
        """Update the quality for all items in the Gilded Rose.

        References
        ----------
        See `GildedRoseRequirements.txt` for more information on this method.
        """
        for i, item in enumerate(self.items):
            gilded_item = GildedItem(item.name, item.sell_in, item.quality)
            gilded_item.update()
            item = Item(gilded_item.name, gilded_item.sell_in, gilded_item.quality)
            self.items[i] = item


class Item:
    """Represent an Item that is available in the Gilded Rose Inn."""

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        """Return a human-friendly representation of an Item."""
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
