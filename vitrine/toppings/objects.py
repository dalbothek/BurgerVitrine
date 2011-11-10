# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class EntitiessTopping(Topping):
    KEY = "entities.object"
    NAME = "Objects"
    ITEMS = (
        ("object_id", "ID"),
        ("name", "Name"),
        ("id", "Entity ID"),
        ("height", "Height"),
        ("width", "Width"),
        ("texture", "Texture")
    )
    PRIORITY = 7.1

    def parse_entry(self, entry, key=None):
        entry["object_id"] = entry.pop("id")
        if "entity" in entry:
            entity = entry["entity"]
            for key in ("id", "name", "width", "height", "texture"):
                if key in entity:
                    entry[key] = entity[key]
        return entry.get("name", entry["object_id"])
