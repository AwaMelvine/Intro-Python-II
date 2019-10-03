# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = [Item('Apple', 'A fruit you can eat.'), Item(
            'Ball', 'Kids and grown ups alike run after it and kick it away when they meet it')]

    def __str__(self):
        roomInfo = f"\nCurrent Room: {self.name}\nDescription: {textwrap.fill(self.description)}\n"

        i = 1
        if len(self.items) == 0:
            roomInfo += f"\nNo items in this room."
        else:
            roomInfo += f"\nAvailable Items:"
            for item in self.items:
                roomInfo += f"\n{i}. {item.name}"
                i += 1

        return roomInfo + "\n"
