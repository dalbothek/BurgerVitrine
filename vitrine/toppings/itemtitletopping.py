# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping


class ItemTitleTopping(Topping):
    def _entry(self, title, content, anchor, escape=True):
        if escape:
            title = self.escape(title)
        return ('<div class="entry"><h3 id="{2}" class="item_title"><a href="#{2}">{0}</a></h3>' +
            '<div>{1}</div></div>').format(title, content, self.anchor(anchor))
