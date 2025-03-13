"""Extend enum decorator."""

import enum


def extend_enum(inherited_enum):
    """Extend enum decorator."""

    def wrapper(added_enum):
        """Extend enum method."""
        joined = {}
        for item in inherited_enum:
            joined[item.name] = item.value
        for item in added_enum:
            joined[item.name] = item.value
        return enum.Enum(added_enum.__name__, joined)

    return wrapper
