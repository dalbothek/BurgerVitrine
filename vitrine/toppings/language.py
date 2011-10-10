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
        for key,value in entry.iteritems():
            if value == "":
                continue
            elif key.endswith(".name") or key.endswith(".desc"):
                yield (key, key[:-5])
            else:
                yield key

    def _get_dl(self, entry):
        dl = Topping._get_dl(self, entry)
        return dl[:3] + ' class="wide"' + dl[3:]
