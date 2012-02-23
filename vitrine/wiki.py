# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import requests
import re

class CoalitionWiki:
    URL = "http://wiki.vg/Protocol"
    
    def __init__(self):
        self._names = {}
        self._urls = {}
        self._load()

    def _load(self):
        r = requests.get(self.URL)
        if r.status_code != requests.codes.ok:
            raise Exception("MinecraftCoalition Wiki returns status code %s" % r.status_code)

        for packet in re.finditer('toclevel-2.*href="([^"]*)".*<span class="toctext">(.*) \((0x.*)\)</span>', r.content):
            id = int(packet.group(3), 16)
            self._names[id] = packet.group(2)
            self._urls[id] = packet.group(1)

    def name(self, id, default=None):
        return self._names.get(id, default)

    def url(self, id, default=None):
        if id in self._urls:
            return "%s%s" % (self.URL, self._urls[id])
        return default
