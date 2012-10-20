# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class SoundsTopping(Topping):
    KEY = "sounds"
    NAME = "Sounds"
    PRIORITY = 3.5
    RESOURCE_URL = "http://s3.amazonaws.com/MinecraftResources/"

    def parse_entry(self, entry, key=None):
        return entry["name"]

    def _get_dl(self, entry):
        aggregate = "<dl>"
        for version in entry['versions']:
            aggregate += "<dt>%s</dt>" % version
            aggregate += "<dd>%s</dd>" % "<br />".join(
                "<a href=\"{0}{1}\">{1}</a>".format(self.RESOURCE_URL,
                                                    sound['path'])
                for sound in entry['versions'][version]
            )
        aggregate += "</dl>"
        return aggregate
