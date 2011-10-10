# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping

class BlocksTopping(Topping):
    KEY = "blocks.block"
    NAME = "Blocks"
    ITEMS = (("id", "ID"),
             ("name", "Name"),
             ("hardness", "Hardness"))
    ESCAPE_TITLE = False

    def parse_entry(self, entry, key):
        if "display_name" in entry:
            entry["name"] = entry["display_name"]
        elif "name" not in entry:
        	entry["name"] = "Unknown"
        if "texture" in entry:
            icon = [-entry["texture"][axis]*32 for axis in ("x", "y")]
            return ('<div title="%s" class="texture" style="background-position:' +
                    '%spx %spx;"></div>') % (entry["name"], icon[0], icon[1])
        else:
            return '<div title="%s" class="craftitem">%s</div>' % (entry["name"], entry["id"])
