"""Functions to keep track and alter inventory."""

from collections import Counter


def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory: dict[str, int] = {}

    return add_items(inventory, items)


def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    inventory = Counter(inventory)
    inventory.update(items)

    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)

    return inventory


def remove_item(inventory: dict, item: list) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, 0)

    return inventory


def list_inventory(inventory: dict) -> list[tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, value) for key, value in inventory.items() if value > 0]
