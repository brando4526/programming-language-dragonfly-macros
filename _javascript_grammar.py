# Author:Brandon Lovrien
# This script includes commands that are to be used for JavaScript programming

from dragonfly import (Grammar, CompoundRule, Dictation, RuleRef, DictList, DictListRef, Text, Key, AppContext, MappingRule, Function, Sequence, Mimic)

def doSomethingToCommand(command):
    newCommand = Sequence(command)
    newCommand.execute()

class JavaScriptEnabler(CompoundRule):
    spec = "Enable JavaScript"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        JavaScriptBootstrap.disable()
        JavaScriptGrammar.enable()
        print "JavaScript grammar enabled"

class JavaScriptDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        JavaScriptGrammar.disable()
        JavaScriptBootstrap.enable()
        print "JavaScript grammar disabled"        


class JavaScriptTestRule(CompoundRule):
    spec = "test JavaScript"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "JavaScript grammar tested"

class JavaScriptControlStructures(MappingRule):

    mapping  = {
                  "variable":               Text("var "),
                  "function":               Text("function functionName() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "code block":             Text("{") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "if":                     Text("if() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "if else":                Text("if() {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("else {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "else if":                Text("else if() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "while loop":             Text("while() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "do while loop":          Text("do {") + Key("enter") + Key("down") + Text("while()"),
                  "for loop":               Text("for(;;) {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  "switch statement":       Text("switch() {") + Key("enter")+ Key("enter"), #+ Text("}"),
                  
               
               }
    

class JavaScriptCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("// "),
                "multiline comment":      Text("/*") + Key("enter") #+ Key("enter") + Text("*/") + Key("up")
               
               }

class JavaScriptMiscellaneousStuff(MappingRule):

    mapping  = {
                   "equals":        Text(" = "),               
                   "new":           Text("new "),
               
               }

class JavaScriptComparisonOperators(MappingRule):

    mapping  = {
                   "equal to":                   Text("=="),               
                   "exactly equal to":           Text("==="),
                   "not equal to":               Text("!="),
                   "greater than":               Text(">"),
                   "less than":                  Text("<"),
                   "greater than or equal to":   Text(">="),
                   "less than or equal to":      Text("<="),
               
               }

class JavaScriptArithmeticOperators(MappingRule):

    mapping  = {
                   "plus plus":                   Text("++"),               
                   "minus minus":               Text("--"),
               
               }

class JavaScriptAssignmentOperators(MappingRule):

    mapping  = {
                   "plus equals":                   Text("+="),               
                   "minus equals":                  Text("-="),
                   "multiply equals":               Text("*="),
                   "divide equals":                 Text("/="),
                   "modulus equals":                Text("%="),
               
               }       

        

JavaScriptBootstrap = Grammar("JavaScript bootstrap")                # Create a grammar to contain the command rule.
JavaScriptBootstrap.add_rule(JavaScriptEnabler())
JavaScriptBootstrap.load()

JavaScriptGrammar = Grammar("JavaScript grammar")
JavaScriptGrammar.add_rule(JavaScriptTestRule())
JavaScriptGrammar.add_rule(JavaScriptControlStructures())
JavaScriptGrammar.add_rule(JavaScriptCommentsSyntax())
JavaScriptGrammar.add_rule(JavaScriptMiscellaneousStuff())
JavaScriptGrammar.add_rule(JavaScriptComparisonOperators())
JavaScriptGrammar.add_rule(JavaScriptArithmeticOperators())
JavaScriptGrammar.add_rule(JavaScriptAssignmentOperators())
JavaScriptGrammar.add_rule(JavaScriptDisabler())
JavaScriptGrammar.load()
JavaScriptGrammar.disable()

# Unload function which will be called by natlink at unload time.
def unload():
    global JavaScriptGrammar
    if JavaScriptGrammar: JavaScriptGrammar.unload()
    JavaScriptGrammar = None
