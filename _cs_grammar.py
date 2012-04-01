# Author:Brandon Lovrien
# This script includes the macros for the C# programming language

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule, Integer)

class CSEnabler(CompoundRule):
    spec = "Enable C sharp"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        csBootstrap.disable()
        csGrammar.enable()
        print "C# grammar enabled"

class CSDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        csGrammar.disable()
        csBootstrap.enable()
        print "C# grammar disabled"        

# This is a test rule to see if the C# grammar is enabled
class CSTestRule(CompoundRule):
    spec = "test C sharp"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "C# grammar tested"

# Handles C# commenting syntax
class CSCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("// "),
                "multiline comment":      Text("/*") + Key("enter") + Key("enter") + Text("*/") + Key("up")
               
               }

# Deals with printing C# datatypes
class CSDataTypes(MappingRule):

    mapping  = {
                "integer":                Text("int "),
                "float":                  Text("float "),
                "float <n>":                Text("float%(n)d "),
                "double":                 Text("double "),
                "boolean":                Text("bool "),
                "char":                   Text("char "),
                "string":                 Text("string "),
                "long":                   Text("long ")
                }
    extras   = [
                Integer("n", 0, 64)
                
               ]

# This rule deals with the C# comparison operators
class CSComparisonOperators(MappingRule):

    mapping  = {
                    "equal to":                     Text("=="),
                    "not equal to":                 Text("!="),
                    "greater than":                 Text(">"),
                    "less than":                    Text("<"),
                    "less than or equal to":        Text("<="),
                    "greater than or equal to":     Text(">="),
               
               }
# This rule deals with the C# Boolean operators
class CSBooleanOperators(MappingRule):

    mapping  = {
                    "logical and":      Text("&&"),
                    "logical or":       Text("||"),
                    "true":             Text("true"),
                    "false":            Text("false"),
                    "not":              Text("!")
                    
               }    
    

class CSControlStructures(MappingRule):
    
    mapping  = {
                    "code block":           Text("{") + Key("enter")+ Key("enter") + Text("}"),
                    "if":                   Text("if() {") + Key("enter")+ Key("enter") + Text("}"),
                    "if else":              Text("if() {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("else {") + Key("enter")+ Key("enter") + Text("}"),
                    "else if":              Text("else if() {") + Key("enter")+ Key("enter") + Text("}"),
                    "while loop":           Text("while() {") + Key("enter")+ Key("enter") + Text("}"),
                    "do while loop":        Text("do {") + Key("enter") + Key("down") + Text("while()"),
                    "for loop":             Text("for(;;) {") + Key("enter")+ Key("enter") + Text("}"),
                    "for each loop":        Text("foreach() {") + Key("enter")+ Key("enter") + Text("}"),
                    "switch statement":     Text("switch() {") + Key("enter")+ Key("enter") + Text("}"),
                    "try catch":            Text("try {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("catch(Exception e) {") + Key("enter")+ Key("enter") + Text("}"),
                    "class":                Text("<access modifier> class ClassName {") + Key("enter")+ Key("enter") + Text("}"),
                    "interface":            Text("<access modifier> interface InterfaceName {") + Key("enter")+ Key("enter") + Text("}"),
                    "enumeration":          Text("<access modifier> enum EnumName {") + Key("enter")+ Key("enter") + Text("}"),
                    "method":               Text("<datatype> methodName() {") + Key("enter") + Key("enter") + Text("}"),
               
               }
# This rule provides some useful method calls in C#
class CSUsefulMethods(MappingRule):

    mapping  = {
                    "print statement":       Text("Console.WriteLine()") + Key("left"),  
               
               }
# This rule deals with some of the C# arithmetic operators
class CSArithmeticOperators(MappingRule):

    mapping  = {
                    "plus plus":        Text("++"),
                    "minus minus":      Text("--"),
                    "multiplied by":    Text("*"),
                    "plus":             Text("+"),
                    "minus":            Text("-"),
                    "divided by":       Text("/"),
                    "modulus":          Text("%") #causes some weird problem in dragonfly so this doesn't work, use "percent sign" instead
               
               }

class CSAssignmentOperators(MappingRule):

    mapping  = {
                    "plus equals":      Text("+="),
                    "minus equals":     Text("-="),
                    "multiply equals":  Text("*="),
                    "divide equals":    Text("/="),
                    
               
               }    

class CSMiscellaneousStuff(MappingRule):

    mapping  = {
                   "equals":        Text(" = "),
                   "new":           Text("new "),
               
               }

class CSAccessModifiers(MappingRule):

    mapping  = {
                    "public":       Text("public "),
                    "private":      Text("private "),
                    "protected":    Text("protected ")
               
               }

class CSEscapeSequences(MappingRule):

    mapping  = {
                    "escape quotes":            Text("\ ")+ Key("left") + Text("\"") + Text("\ ")+ Key("left") + Text("\""),
                    "escape single quotes":     Text("\ ")+ Key("left") + Text("\'") + Text("\ ")+ Key("left") + Text("\'"),
                    "escape line":              Text("\ ")+ Key("left") + Text("n"),
                    "escape tab":               Text("\ ")+ Key("left") + Text("t"), 
                    "escape carriage return":    Text("\ ")+ Key("left") + Text("r"),
                }    

# The main C# grammar rules are activated here
csBootstrap = Grammar("C sharp bootstrap")                
csBootstrap.add_rule(CSEnabler())
csBootstrap.load()

csGrammar = Grammar("C sharp grammar")
csGrammar.add_rule(CSTestRule())
csGrammar.add_rule(CSCommentsSyntax())
csGrammar.add_rule(CSDataTypes())
csGrammar.add_rule(CSComparisonOperators())
csGrammar.add_rule(CSBooleanOperators())
csGrammar.add_rule(CSControlStructures())
csGrammar.add_rule(CSUsefulMethods())
csGrammar.add_rule(CSArithmeticOperators())
csGrammar.add_rule(CSAssignmentOperators())
csGrammar.add_rule(CSMiscellaneousStuff())
csGrammar.add_rule(CSAccessModifiers())
csGrammar.add_rule(CSEscapeSequences())
csGrammar.add_rule(CSDisabler())
csGrammar.load()
csGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global csGrammar
    if csGrammar: csGrammar.unload()
    csGrammar = None