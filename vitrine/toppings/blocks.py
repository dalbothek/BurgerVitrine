# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .itemtitletopping import ItemTitleTopping


class BlocksTopping(ItemTitleTopping):
    KEY = "blocks.block"
    NAME = "Blocks"
    ITEMS = (("id", "ID"),
             ("name", "Name"),
             ("hardness", "Hardness"))
    ESCAPE_TITLE = False
    PRIORITY = 10
    
    def SORTING(self, (k, v)):
        if self.diff:
            if v[0] is not None:
                return int(v[0]["id"]), k
            else:
                return int(v[1]["id"]), k
        else:
            return int(v["id"]), k

    def parse_entry(self, entry, key):
        if "display_name" in entry:
            entry["name"] = entry["display_name"]
        elif "name" not in entry:
            entry["name"] = "Unknown"
        if "texture" in entry:
            icon = [-entry["texture"][axis] * 32 for axis in ("x", "y")]
            return ('<div title="%s" class="texture" ' +
                    'style="background-position:%spx %spx;"></div>') % (
                        entry["name"], icon[0], icon[1]
                    ), entry["id"]
        else:
            return '<div title="%s" class="craftitem">%s</div>' % (
                entry["name"], entry["id"]
            ), entry["id"]
