# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class BiomesTopping(Topping):
    KEY = "biomes"
    NAME = "Biomes"
    ITEMS = (("id", "ID"),
             ("color", "Color"),
             ("temperature", "Temperature"),
             ("rainfall", "Rainfall"),
             ("minh", "Min height"),
             ("maxh", "Max height"))
    ESCAPE_TITLE = False
    PRIORITY = 0

    def parse_entry(self, entry, key):
        if "height" in entry:
            entry["minh"], entry["maxh"] = entry["height"]
        if "color" in entry:
            entry["color"] = "#%06x" % entry["color"]
            color = entry["color"]
        else:
            color = "none"
        return '%s<div class="color" style="background:%s;"></div>' % (
                entry["name"], color), entry["name"]

    def SORTING(self, (k, v)):
        if "id" in v:
            return v["id"], v
        return k, v
