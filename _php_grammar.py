# Author:Brandon Lovrien
# This script includes commands that are to be used for programming in the PHP programming language

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)


class PHPEnabler(CompoundRule):
    spec = "Enable PHP"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        phpBootstrap.disable()
        phpGrammar.enable()
        print "PHP grammar enabled"

class PHPDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        phpGrammar.disable()
        phpBootstrap.enable()
        print "PHP grammar disabled"        


class PHPTestRule(CompoundRule):
    spec = "test PHP"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "PHP grammar tested"

# Deals with printing PHP datatypes
class PHPDataTypes(MappingRule):

    mapping  = {
                "integer":                Text("int"),
                "float":                  Text("float"),
                "boolean":                Text("boolean"),
                "string":                 Text("string"),
                "object":                 Text("object"),
                "null":                   Text("NULL")
                }

class PHPVariableDeclarations(MappingRule):

    mapping  = {
                "variable":                Text("$")
                                   
                }

# Handles PHP commenting syntax
class PHPCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("// "),
                "multiline comment":      Text("/*") + Key("enter") + Key("enter") + Text("*/") + Key("up")
               
               }

class PHPSuperGlobals(MappingRule):

    mapping  = {
                "globals":              Text("$GLOBALS['']"),
                "post":                 Text("$_POST['']"),
                "get":                  Text("$_GET['']"),
                "files":                Text("$_FILES['']"),
                "cookie":               Text("$_COOKIE['']"),
                "session":              Text("$_SESSION['']"),
                "request":              Text("$_REQUEST['']"),
                "environment":          Text("$_ENV['']")
               }

class PHPControlStructures(MappingRule):

    mapping  = {
                "code block":               Text("{") + Key("enter")+ Key("enter") + Text("}"),
                "if":                   Text("if() {") + Key("enter")+ Key("enter") + Text("}"),
                "if else":                  Text("if() {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("else {") + Key("enter")+ Key("enter") + Text("}"),
                "else if":                  Text("elseif() {") + Key("enter")+ Key("enter") + Text("}"),
                "for loop":                 Text("for(;;) {") + Key("enter")+ Key("enter") + Text("}"),
                "for each loop":            Text("for(<array> as [<value> |<key> => <value>]) {") + Key("enter")+ Key("enter") + Text("}"),
                "while loop":               Text("while() {") + Key("enter")+ Key("enter") + Text("}"),
                "do while loop":            Text("do {") + Key("enter") + Key("down") + Text("while()"),
                "switch statement":         Text("switch() {") + Key("enter")+ Key("enter") + Text("}"),
                "try catch":                Text("try {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("catch(<ExceptionClass> e) {") + Key("enter")+ Key("enter") + Text("}"),
                "function":                 Text("function functionName() {") + Key("enter")+ Key("enter") + Text("}"),
                "class":                    Text("class ClassName {") + Key("enter")+ Key("enter") + Text("}")
                   
               }    

class PHPAccessModifiers(MappingRule):

    mapping  = {
                    "public":       Text("public "),
                    "private":      Text("private "),
                    "static":       Text("static ")
               
               }

class PHPUsefulMethods(MappingRule):

    mapping  = {
                    "print statement":       Text("echo \"\"") + Key("left")   
               
               }

class PHPLogicalOperators(MappingRule):

    mapping  = {
                "logical and":              Text("&&"),
                "logical or":               Text("||"),
                "true":                     Text("true"),
                "false":                    Text("false"),
                "not":                      Text("!"),  
                "logical exclusive or":     Text("xor")
               }

class PHPAssignmentOperators(MappingRule):

    mapping  = {
                    "plus equals":      Text("+="),
                    "minus equals":     Text("-="),
                    "multiply equals":  Text("*="),
                    "divide equals":    Text("/="),
                    ".equals":          Text(".=")
               }    

class PHPArithmeticOperators(MappingRule):

    mapping  = {
                    "multiplied by":    Text("*"),
                    "plus":             Text("+"),
                    "minus":            Text("-"),
                    "divided by":       Text("/"),
                    "modulus":          Text("%") #causes some weird problem in dragonfly so this doesn't work, use "percent sign" instead
                }


class PHPEscapeSequences(MappingRule):

    mapping  = {
                    "escape quotes":            Text("\ ")+ Key("left") + Text("\"") + Text("\ ")+ Key("left") + Text("\""),
                    "escape single quotes":     Text("\ ")+ Key("left") + Text("\'") + Text("\ ")+ Key("left") + Text("\'"),
                    "escape line":              Text("\ ")+ Key("left") + Text("n"),
                    "escape tab":               Text("\ ")+ Key("left") + Text("t"), 
                    "escape carriage return":    Text("\ ")+ Key("left") + Text("r"),
                }

class PHPComparisonOperators(MappingRule):

    mapping  = {
                    "equal to":                         Text("=="),
                    "not equal to":                     Text("!="),
                    "equal to type comparison":         Text("==="),
                    "not equal to type comparison":     Text("!=="),
                    "greater than":                     Text(">"),
                    "less than":                        Text("<"),
                    "less than or equal to":            Text("<="),
                    "greater than or equal to":         Text(">="),
               
               }

class PHPMiscellaneousStuff(MappingRule):

    mapping  = {
                   "PHP block":     Text("<?php  ?>"),
        
                   
                   "require":       Text("require ('');"),
                   "require once":  Text("require_once ('');"),
                   "include":       Text("include ('');"),
                   "include once":  Text("require_once ('');"),
                   "equals":        Text(" = "),
               
               }    

phpBootstrap = Grammar("php bootstrap")                # Create a grammar to contain the command rule.
phpBootstrap.add_rule(PHPEnabler())
phpBootstrap.load()

phpGrammar = Grammar("php grammar")
phpGrammar.add_rule(PHPTestRule())
phpGrammar.add_rule(PHPDataTypes())
phpGrammar.add_rule(PHPVariableDeclarations())
phpGrammar.add_rule(PHPCommentsSyntax())
phpGrammar.add_rule(PHPSuperGlobals())
phpGrammar.add_rule(PHPControlStructures())
phpGrammar.add_rule(PHPAccessModifiers())
phpGrammar.add_rule(PHPUsefulMethods())
phpGrammar.add_rule(PHPLogicalOperators())
phpGrammar.add_rule(PHPAssignmentOperators())
phpGrammar.add_rule(PHPArithmeticOperators())
phpGrammar.add_rule(PHPEscapeSequences())
phpGrammar.add_rule(PHPComparisonOperators())
phpGrammar.add_rule(PHPMiscellaneousStuff())
phpGrammar.add_rule(PHPDisabler())
phpGrammar.load()
phpGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global phpGrammar
    if phpGrammar: phpGrammar.unload()
    phpGrammar = None