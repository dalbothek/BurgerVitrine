# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .itemtitletopping import ItemTitleTopping

class ItemsTopping(ItemTitleTopping):
    KEY = "items.item"
    NAME = "Items"
    ITEMS = (("id", "ID"),
             ("name", "Name"))
    ESCAPE_TITLE = False
    PRIORITY = 9
    
    def parse_entry(self, entry, key):
        if "display_name" in entry:
            entry["name"] = entry["display_name"]
        elif "name" not in entry:
        	entry["name"] = "Unknown"
        icon = [-entry["icon"][axis]*32 for axis in ("x", "y")]
        return ('<div class="item" title="%s" style="background-position:' +
                        '%spx %spx;"></div>') % (entry["name"], icon[0], icon[1])
