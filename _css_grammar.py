# Author:Brandon Lovrien
# This script includes commands used for CSS coding

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule, Choice, Integer, Function)

# Voice command rule for "middle-slash" naming convention.
def middle_slash_format(command):   # Callback when command is spoken.
        textToPrint = command
        someString = str(textToPrint)
        printer = Text(someString.replace(' ', '-'))
        printer.execute()
        
class CSSEnabler(CompoundRule):
    spec = "Enable CSS"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        cssBootstrap.disable()
        cssGrammar.enable()
        print "CSS grammar enabled"

class CSSDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        cssGrammar.disable()
        cssBootstrap.enable()
        print "CSS grammar disabled"


class CSSTestRule(CompoundRule):
    spec = "test CSS"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "CSS grammar tested"

class CSSSelectors(MappingRule):
    mapping = {
                    "ID selector": Text("#idName")+ Key("enter") + Text("{\n\n}"),
                    "class selector": Text(".className")+ Key("enter") + Text("{\n\n}"),
                    "tag selector":   Text("tagName")+ Key("enter") + Text("{\n\n}"),
                    # I know there are more types of selectors in CSS but these are the most common
            }        

class CSSValues(MappingRule):
    mapping = {
                "<value> (pixels | pixel)":    Text("%(value)dpx"),
                "<value> (points | point)":    Text("%(value)dpt"),
             }
    extras = [
            Integer("value", 0, 800),
        ]
class CSSTags(MappingRule):

    mapping  = {
                   "property <command>": Function(middle_slash_format) + Text(":;") + Key("left"),
                   "comment":          Text("/* */"),
                   
               
               }
    extras = [
        Dictation("command"),        
             ]

#  Code for initial setup of the HTML grammar
cssBootstrap = Grammar("css bootstrap")                # Create a grammar to contain the command rule.
cssBootstrap.add_rule(CSSEnabler())
cssBootstrap.load()


cssGrammar = Grammar("css grammar")
cssGrammar.add_rule(CSSTestRule())
cssGrammar.add_rule(CSSDisabler())
cssGrammar.add_rule(CSSValues())
cssGrammar.add_rule(CSSSelectors())
cssGrammar.add_rule(CSSTags())
cssGrammar.load()
cssGrammar.disable()

# Unload function which will be called by natlink at unload time.
def unload():
    global cssGrammar
    if cssGrammar: cssGrammar.unload()
    cssGrammar = None

