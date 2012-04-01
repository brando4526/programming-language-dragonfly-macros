# Author:Brandon Lovrien
# This script includes commands that are useful for the Java programming language

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)

class JavaEnabler(CompoundRule):
    spec = "Enable Java"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        javaBootstrap.disable()
        javaGrammar.enable()
        print "Java grammar enabled"

class JavaDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        javaGrammar.disable()
        javaBootstrap.enable()
        print "Java grammar disabled"        

# This is a test rule to see if the Java grammar is enabled
class JavaTestRule(CompoundRule):
    spec = "test Java"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "Java grammar tested"

# Handles Java commenting syntax
class JavaCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("// "),
                "multiline comment":      Text("/*") + Key("enter") #+ Key("enter") + Text("*/") + Key("up")
               
               }

# Deals with printing Java datatypes
class JavaDataTypes(MappingRule):

    mapping  = {
                "integer":                Text("int "),
                "float":                  Text("float "),
                "double":                 Text("double "),
                "boolean":                Text("boolean "),
                "char":                   Text("char "),
                "string":                 Text("String "),
                "long":                   Text("long ")
                }

# This rule deals with the Java comparison operators
class JavaComparisonOperators(MappingRule):

    mapping  = {
                    "equal to":                     Text("=="),
                    "not equal to":                 Text("!="),
                    "greater than":                 Text(">"),
                    "less than":                    Text("<"),
                    "less than or equal to":        Text("<="),
                    "greater than or equal to":     Text(">="),
               
               }
# This rule deals with the Java Boolean operators
class JavaBooleanOperators(MappingRule):

    mapping  = {
                    "logical and":      Text("&&"),
                    "logical or":       Text("||"),
                    "true":             Text("true"),
                    "false":            Text("false"),
                    "not":              Text("!")
                    
               }    
    

class JavaControlStructures(MappingRule):
    #note: the last curly braces were commented out so that these commands properly work with the auto formatting of the eclipse IDE.
    mapping  = {
                    "code block":           Text("{") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "if":                   Text("if() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "if else":              Text("if() {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("else {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "else if":              Text("else if() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "while loop":           Text("while() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "do while loop":        Text("do {") + Key("enter") + Key("down") + Text("while()"),
                    "for loop":             Text("for(;;) {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "switch statement":     Text("switch() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "try catch":            Text("try {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("catch(Exception e) {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "class":                Text("<access modifier> class ClassName {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "interface":            Text("<access modifier> interface InterfaceName {") + Key("enter")+ Key("enter"), #+ Text("}"),
                    "enumeration":          Text("<access modifier> enum EnumName {") + Key("enter")+ Key("enter"), #+ Text("}")
                    "method":               Text("<datatype> methodName() {") + Key("enter")+ Key("enter"), #+ Text("}"),
               
               }
# This rule provides some useful method calls in Java
class JavaUsefulMethods(MappingRule):

    mapping  = {
                    "print statement":       Text("System.out.println()") + Key("left")   
               
               }
# This rule deals with some of the Java arithmetic operators
class JavaArithmeticOperators(MappingRule):

    mapping  = {
                    "plus plus":        Text("++"),
                    "minus minus":      Text("--"),
                    "multiplied by":    Text("*"),
                    "plus":             Text("+"),
                    "minus":            Text("-"),
                    "divided by":       Text("/"),
                    "modulus":          Text("%") #causes some weird problem in dragonfly so this doesn't work, use "percent sign" instead
               
               }

class JavaAssignmentOperators(MappingRule):

    mapping  = {
                    "plus equals":      Text("+="),
                    "minus equals":     Text("-="),
                    "multiply equals":  Text("*="),
                    "divide equals":    Text("/="),
                    
               
               }    

class JavaMiscellaneousStuff(MappingRule):

    mapping  = {
                   "equals":        Text(" = "),
                   "import":        Text("import ;") + Key("left"),
                   "new":           Text("new "),
               
               }

class JavaAccessModifiers(MappingRule):

    mapping  = {
                    "public":       Text("public "),
                    "private":      Text("private "),
                    "protected":    Text("protected ")
               
               }

class JavaEscapeSequences(MappingRule):

    mapping  = {
                    "escape quotes":            Text("\ ")+ Key("left") + Text("\"") + Text("\ ")+ Key("left") + Text("\""),
                    "escape single quotes":     Text("\ ")+ Key("left") + Text("\'") + Text("\ ")+ Key("left") + Text("\'"),
                    "escape line":              Text("\ ")+ Key("left") + Text("n"),
                    "escape tab":               Text("\ ")+ Key("left") + Text("t"), 
                    "escape carriage return":    Text("\ ")+ Key("left") + Text("r"),
                }    

# The main Java grammar rules are activated here
javaBootstrap = Grammar("java bootstrap")                
javaBootstrap.add_rule(JavaEnabler())
javaBootstrap.load()

javaGrammar = Grammar("java grammar")
javaGrammar.add_rule(JavaTestRule())
javaGrammar.add_rule(JavaCommentsSyntax())
javaGrammar.add_rule(JavaDataTypes())
javaGrammar.add_rule(JavaComparisonOperators())
javaGrammar.add_rule(JavaBooleanOperators())
javaGrammar.add_rule(JavaControlStructures())
javaGrammar.add_rule(JavaUsefulMethods())
javaGrammar.add_rule(JavaArithmeticOperators())
javaGrammar.add_rule(JavaAssignmentOperators())
javaGrammar.add_rule(JavaMiscellaneousStuff())
javaGrammar.add_rule(JavaAccessModifiers())
javaGrammar.add_rule(JavaEscapeSequences())
javaGrammar.add_rule(JavaDisabler())
javaGrammar.load()
javaGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global javaGrammar
    if javaGrammar: javaGrammar.unload()
    javaGrammar = None