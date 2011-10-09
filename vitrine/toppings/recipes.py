# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping

class RecipesTopping(Topping):
    KEY = "recipes"
    NAME = "Recipes"
    NO_ESCAPE = ("json")
    
    def _get_entry_html(self, entry, key=None):
        if entry is None:
            return ""
        else:
            aggregate = ""
            for recipe in entry:
                aggregate += self._entry(self.parse_entry(recipe, key),
                               self._get_dl(recipe), False)
            return aggregate

    def _entry(self, title, content, escape=True):
        if escape:
            title = self.escape(title)
        return ('<div class="entry">' +
                '<div class="workbench"><div class="craftgrid">%s</div><div class="result">%s</div></div></div>') % (content, title)

    def parse_entry(self, entry, key):
        result = self.craft_item(entry["makes"], entry["amount"])
        aggregate = ""
        if entry["type"] == "shape":
            materials = {' ':'<div class="craftable"></div>'}
            for key,material in entry["raw"]["subs"].iteritems():
                materials[key] = self.craft_item(material)
            rows = entry["raw"]["rows"]
            for i in range(3-len(rows)):
                rows.append("   ")
            rows.reverse()
            for row in rows:
                while len(row) < 3:
                    if len(row) % 2 == 0:
                        row += ' '
                    else:
                        row = ' ' + row
                aggregate += '<div class="craftrow">'
                for col in row:
                    aggregate += materials[col]
                aggregate += "</div>"
        else:
            aggregate += '<div class="craftrow">'
            i = 0
            while len(entry["ingredients"]) < 9:
                entry["ingredients"].append(' ')
            for material in entry["ingredients"]:
                aggregate += self.craft_item(material)
                i += 1
                if i % 3 == 0:
                    aggregate += '</div><div class="craftrow">'
            aggregate += "</div>"

        
        entry["json"] = aggregate
        return result

    def craft_item(self, material, amount=1):
        if material is None:
            content = 'X'
        if "icon" in material:
            icon = [-material["icon"][axis]*32 for axis in ("x", "y")]
            content = ('<div class="icon" style="background-position:' +
                       '%spx %spx;"></div>') % (icon[0], icon[1])
        elif "texture" in material:
            icon = [-material["texture"][axis]*32 for axis in ("x", "y")]
            content = ('<div class="texture" style="background-position:' +
                       '%spx %spx;"></div>') % (icon[0], icon[1])
        elif "id" in material:
            content = material["id"]
        else:
            content = material
        if amount > 1:
            content = '%s<span class="amount">%s</span>' % (content, amount)
        return '<div class="craftable">%s</div>' % content
