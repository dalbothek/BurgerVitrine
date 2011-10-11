# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from .topping import Topping

try:
    from pygments import highlight
    from pygments.lexers import JavaLexer
    from pygments.formatters import HtmlFormatter
    SYNTAX_HIGHLIGHT = True
    FORMATTER = HtmlFormatter(classprefix="hl_", nowrap=True)
    LEXER = JavaLexer()
except:
    SYNTAX_HIGHLIGHT = False


class PacketsTopping(Topping):
    KEY = "packets.packet"
    NAME = "Packets"
    ITEMS = ("Direction",
             ("size", "Size"),
             ("code", None))
    NO_ESCAPE = ("code")

    DIRECTIONS = {(True, True): "Both",
                  (True, False): "Client to server",
                  (False, True): "Server to client",
                  (False, False): "None"}
    TYPES = {"byte": "writeByte",
             "boolean": "writeBoolean",
             "short": "writeShort",
             "int": "writeInt",
             "float": "writeFloat",
             "long": "writeLong",
             "double": "writeDouble",
             "string16": "writeString",
             "byte[]": "writeBytes"
        }
    PRIORITY = 7

    def parse_entry(self, entry, key):
        entry["Direction"] = self.DIRECTIONS[(
            entry["from_client"],
            entry["from_server"]
        )]
        entry["code"] = self.code(entry["instructions"])
        return "0x%02x (%s)" % (entry["id"], entry["id"])

    def code(self, instructions):
        code = self.instructions(instructions)
        if SYNTAX_HIGHLIGHT:
            code = highlight(code, LEXER, FORMATTER)
        else:
            code = self.escape(code)
        return "<pre>%s</pre>" % code

    def instructions(self, instructions, level=0):
        close = False
        case = False
        aggregate = ""
        for instr in instructions:
            html, close, case = self.instruction(instr, close, case, level)
            aggregate += html
        if close:
            aggregate += self.indent("}", level)
        return aggregate

    def instruction(self, instr, close=False, case=False, level=0):
        aggregate = ""
        if case:
            level += 1
        if close:
            aggregate = self.indent("}", level)
        close = True
        if instr["operation"] == "write":
            aggregate += self.indent("%s(%s);" % (
                self.TYPES[instr["type"]],
                instr["field"]
            ), level)
            close = False
        elif instr["operation"] == "if":
            aggregate += self.indent("if(%s) {" % instr["condition"], level)
            aggregate += self.instructions(instr["instructions"], level + 1)
        elif instr["operation"] == "else":
            aggregate = self.indent("} else {", level)
            aggregate += self.instructions(instr["instructions"], level + 1)
        elif instr["operation"] == "loop":
            aggregate += self.indent("while(%s) {" % instr["condition"], level)
            aggregate += self.instructions(instr["instructions"], level + 1)
        elif instr["operation"] == "switch":
            aggregate += self.indent("switch(%s) {" % instr["field"], level)
            aggregate += self.instructions(instr["instructions"], level + 1)
        elif instr["operation"] == "case":
            if case:
                level -= 1
            aggregate += self.indent("case %s:" % instr["value"], level)
            close = False
            case = True
        elif instr["operation"] == "break":
            aggregate += self.indent("break;", level)
            close = False
        elif instr["operation"] == "increment":
            if instr["amount"] == "1":
                aggregate += self.indent("%s++;" % instr["field"], level)
            else:
                aggregate += self.indent("%s += %s;" % (
                    instr["field"],
                    instr["amount"]
                ), level)
            close = False
        else:
            aggregate += self.indent("// %s" % instr["operation"], level)
            close = False
        return (aggregate, close, case)

    def indent(self, string, level):
        return "  " * level + string + "\n"
