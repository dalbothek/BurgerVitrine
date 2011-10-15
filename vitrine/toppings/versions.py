# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class VersionsTopping(Topping):
    KEY = "version"
    NAME = "Versions"
    PRIORITY = 6.5

    def parse_entry(self, entry, key=None):
        return key
        
    def _get_dl(self, entry):
        return entry
