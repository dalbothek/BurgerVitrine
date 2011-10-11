# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class LanguageTopping(Topping):
    KEY = "language"
    NAME = "Language"
    ITEMS = ()
    PRIORITY = 4

    def parse_entry(self, entry, key=None):
        self.ITEMS = self.filter_keys(entry)
        return key

    def filter_keys(self, entry):
        for key, value in entry.iteritems():
            if value == "":
                continue
            if value is None:
                entry[key] = "-"
            if key.endswith(".name") or key.endswith(".desc"):
                yield (key, key[:-5])
            else:
                yield key

    def _get_dl(self, entry):
        dl = Topping._get_dl(self, entry)
        return dl[:3] + ' class="wide"' + dl[3:]

    def _parse_entry(self, entry, key=None):
        if self.diff:
            return self.compare(entry, key)
        else:
            return Topping._parse_entry(self, entry, key)

    def compare(self, entry, title):
        if isinstance(entry, dict):
            left = {}
            right = {}
            for key, values in entry.iteritems():
                if values[0] in ("", None) and values[1] in ("", None):
                    continue
                elif values[0] != values[1]:
                    left[key] = values[0]
                    right[key] = values[1]
            if len(left) == 0:
                return ""
            entry = [left, right]
        return Topping._parse_entry(self, entry, title)
