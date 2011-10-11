# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from solum import JarFile
from StringIO import StringIO

try:
    from PIL import Image
except:
    try:
        from Imaging import Image
    except:
        Image = None


PATHS = {"terrain": "terrain.png",
         "items": "gui/items.png"}


def extract(jar, file, output):
    if Image is None:
        print "Extracting textures requires PIL"
        return

    try:
        jar = JarFile(jar)
    except:
        print "Opening jar file failed"
        return

    path = PATHS[file]
    data = jar.zp.read(path)

    image = Image.open(StringIO(data))
    image.resize((512, 512)).save(output, format="PNG")

    return True
