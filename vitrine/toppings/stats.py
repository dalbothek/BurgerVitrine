# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class StatsTopping(Topping):
    KEY = "stats"
    NAME = "Stats"
    ITEMS = (("desc", None),)
    PRIORITY = 6

    def parse_entry(self, entry, key=None):
        return key
