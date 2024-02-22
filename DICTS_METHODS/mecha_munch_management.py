"""Functions to manage a users shopping cart items."""

from collections import Counter


def add_item(current_cart: dict, items_to_add) -> dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    current_cart = Counter(current_cart)
    current_cart.update(items_to_add)

    return current_cart


def read_notes(notes) -> dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return Counter(notes)


def update_recipes(ideas: dict, recipe_updates) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates

    return ideas | dict(recipe_updates)


def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment = {}

    for k, v in cart.items():
        aisle, refrigeration = aisle_mapping[k]
        fulfillment[k] = [v, aisle, refrigeration]

    return dict(sorted(fulfillment.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for k, v in fulfillment_cart.items():
        store_inventory[k][0] -= v[0]
        if store_inventory[k][0] == 0:
            store_inventory[k][0] = "Out of Stock"

    return store_inventory
