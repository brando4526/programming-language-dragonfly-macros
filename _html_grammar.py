# Author:Brandon Lovrien
# This script includes commands used for HTML coding

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule, Choice)

class HTMLEnabler(CompoundRule):
    spec = "Enable HTML"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        htmlBootstrap.disable()
        htmlGrammar.enable()
        print "HTML grammar enabled"

class HTMLDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        htmlGrammar.disable()
        htmlBootstrap.enable()
        print "HTML grammar disabled"


class HTMLTestRule(CompoundRule):
    spec = "test HTML"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "HTML grammar tested"


class HTMLTags(MappingRule):

    mapping  = {
                   "doc type":          Text("<!DOCTYPE HTML>"),
                   "comment":           Text( "<!---->" ) + Key( "left" ) + Key( "left" ) + Key( "left" ),
                   "tags":              Text("<></>"),
                   "line break":        Text( "<br />" ),
                   "image":             Text( "<img />" ),
                   "equals":            Text( "=" ),
                   "<tagname> tags":    Text("<%(tagname)s></%(tagname)s>"),

                   # used to specify tag attributes
                   "attribute":                             Text( ' attributeName=""' ) + Key( "left" ),
                   "attribute <attribute>":                Text( ' %(attribute)s=""' ) + Key( "left" ),
                   
               
               }
    extras = [
        Choice("attribute", {
                               "ID": "id",
                               "class": "class",
                               "style": "style",
                               "title": "title",
                               "SRC": "src",
                               "HREF": "href",
                             }
                    ),
        Choice("tagname", {
                              "anchor": "a",
                              "abbreviation": "abbr",
                              "address": "address",
                              "area": "area",
                              "article": "article",
                              "aside": "aside",
                              "audio": "audio",
                              "bold": "b",
                              "base": "base",
                              "BDI": "bdi",
                              "BDO": "bdo",
                              "block quote": "blockquote",
                              "body": "body",
                              "button": "button",
                              "Canvas": "canvas",
                              # means the same thing and represents a table caption
                              "caption": "caption",  "table caption": "caption",
                              "cite": "cite",
                              "code": "code",
                              "table column": "col",
                              "table column group": "colgroup",
                              "command": "command",
                              "data list": "datalist",
                              "definition description": "dd",
                              "del": "del",
                              "details": "details",
                              "dfn": "dfn",
                              "div": "div",
                              "dl": "dl",
                              "dt": "dt",
                              "em": "em",
                              "embed": "embed",
                              "field set": "fieldset",
                              "figure caption": "figcaption",
                              "figure": "figure",
                              "footer": "footer",
                              "form": "form",
                              "H1": "h1",
                              "H2": "h2",
                              "H3": "h3",
                              "H4": "h4",
                              "H5": "h5",
                              "H6": "h6",
                              "head": "head",
                              "H group": "hgroup",
                              "HR": "hr",
                              "HTML": "html",
                              "I": "i",
                              "I frame": "iframe",
                              "input": "input",
                              "INS": "ins",
                              "key gen": "keygen",
                              "KBD": "kbd",
                              "label": "label",
                              "legend": "legend",
                              "list item": "li",
                              "Link": "link",
                              "Mark": "mark",
                              "menu": "menu",
                              "meta": "meta",
                              "meter": "meter",
                              "nav": "nav",
                              "no script": "noscript",
                              "object": "object",
                              "ordered list": "ol",
                              "option group": "optgroup",
                              "option": "option",
                              "output": "output",
                              "p": "p",
                              "parameter": "param",
                              "pre": "pre",
                              "progress": "progress",
                              "g": "g",
                              "RP": "rp",
                              "RT": "rt",
                              "Ruby": "ruby",
                              "s": "s",
                              "sample": "samp",
                              "script": "script",
                              "section": "section",
                              "select": "select",
                              "small": "small",
                              "source": "source",
                              "span": "span",
                              "strong": "strong",
                              "style": "style",
                              "sub": "sub",
                              "summary": "summary",
                              "superscript": "sup",
                              "table": "table",
                              "T body": "tbody",
                              # means the same thing and represents a table cell
                              "TD": "td",     "table cell": "td",
                              "textarea": "textarea",
                              "T foot": "tfoot",
                              # means the same thing and represents a table header
                              "TH": "th", "table header": "th",
                              "T head": "thead",
                              "time": "time",
                              "title": "title",
                              # means the same thing and represents a table row
                              "table row": "tr",   "TR": "tr",
                              "track": "track",
                              "unordered list": "ul",
                              "variable": "var",
                              "video": "video",
                              "label": "label",
                               
                             }
                    )
             ]

#  Code for initial setup of the HTML grammar
htmlBootstrap = Grammar("html bootstrap")                # Create a grammar to contain the command rule.
htmlBootstrap.add_rule(HTMLEnabler())
htmlBootstrap.load()


htmlGrammar = Grammar("html grammar")
htmlGrammar.add_rule(HTMLTestRule())
htmlGrammar.add_rule(HTMLDisabler())
htmlGrammar.add_rule(HTMLTags())
htmlGrammar.load()
htmlGrammar.disable()

# Unload function which will be called by natlink at unload time.
def unload():
    global htmlGrammar
    if htmlGrammar: htmlGrammar.unload()
    htmlGrammar = None