# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"\nCurrent Room: {self.name}\nDescription: {textwrap.fill(self.description)}\n"
