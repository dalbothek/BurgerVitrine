# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import os
import sys
import getopt
import json

def usage():
    print "Example usage:",
    print "Burger/munch.py -c 1.5.jar 1.6.jar | Hamburglar/hamburglar.py"


def import_toppings():
    """
    Attempts to load all available toppings.
    """
    this_dir = os.path.dirname(__file__)
    toppings_dir = os.path.join(this_dir, "vitrine", "toppings")
    from_list = ["topping"]

    # Traverse the toppings directory and import everything.
    for root, dirs, files in os.walk(toppings_dir):
        for file_ in files:
            if not file_.endswith(".py"):
                continue
            elif file_.startswith("__"):
                continue

            from_list.append(file_[:-3])

    imports = __import__("vitrine.toppings", fromlist=from_list)

    toppings = imports.topping.Topping.__subclasses__()
    subclasses = toppings
    while len(subclasses) > 0:
        newclasses = []
        for subclass in subclasses:
            newclasses += subclass.__subclasses__()
        subclasses = newclasses
        toppings += subclasses

    return toppings

def embed(html):
    return """<html>
                <head>
                  <title>Burger Vitrine</title>
                  <link rel="stylesheet" href="style.css" />
                </head>
                <body>%s</body>
              </html>""" % html

def generate_html():
    toppings = import_toppings()

    # Load JSON objects from stdin
    if sys.stdin.isatty():
        print "Error: Vitrine expects Burger or Hamburglar output via stdin.\n"
        usage()
        sys.exit(3)

    try:
        data = json.load(sys.stdin)
    except ValueError, err:
        print "Error: Invalid input (" + str(err) + ")\n"
        usage()
        sys.exit(5)

    diff = not isinstance(data, list)
    if not diff:
        data = data[0]

    # Generate HTML
    aggregate = ""

    for topping in toppings:
        if topping.KEY == None:
            continue
        keys = topping.KEY.split(".")
        obj = data
        skip = False
        for key in keys:
            if key not in obj:
                skip = True
                break
            obj = obj[key]
        if skip:
            continue

        aggregate += str(topping(obj, diff))

    if not only_body:
        aggregate = embed(aggregate)

    # Output results
    output.write(aggregate)

def extract():
    import extractor
    if extractor.extract(jar, mode, output) is None:
        sys.exit(1)

if __name__ == '__main__':
    try:
        opts, args = getopt.gnu_getopt(
            sys.argv[1:],
            "o:bi:t:",
            [
                "output=",
                "body",
                "items=",
                "terrain="
            ]
        )
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(1)

    # Default options
    output = sys.stdout
    only_body = False
    mode = "html"
    jar = None

    for o, a in opts:
        if o in ("-o", "--output"):
            output = open(a, "ab")
        elif o in ("-b", "--body"):
            only_body = True
        elif o in ("-i", "--items"):
            mode = "items"
            jar = a
        elif o in ("-t", "--terrain"):
            mode = "terrain"
            jar = a


    if mode == "html":
        generate_html()
    else:
        extract()
