# Author:Brandon Lovrien
# this script includes the macros for C++ programming

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule, Integer)


class CPPEnabler(CompoundRule):
    spec = "Enable CPP"                  # note: this command couldn't be "enable C++" because it causes problems with the grammar engine due to complexity.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        CPPBootstrap.disable()
        CPPGrammar.enable()
        print "C++ grammar enabled"

class CPPDisabler(CompoundRule):
    spec = "switch language"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        CPPGrammar.disable()
        CPPBootstrap.enable()
        print "C++ grammar disabled"        


# test rule to see if this script is working
class CPPTestRule(CompoundRule):
    spec = "test CPP"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "C++ grammar tested"

#Rules for implementing control structures in C++
class CPPControlStructures(MappingRule):
    
    mapping  = {
                    "code block":           Text("{") + Key("enter")+ Key("enter") + Text("}"),
                    "if":                   Text("if()") + Key("enter")+ Key("enter") + Text("}"),
                    "if else":              Text("if() {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("else {") + Key("enter")+ Key("enter") + Text("}"),
                    "else if":              Text("else if() {") + Key("enter")+ Key("enter") + Text("}"),
                    "while loop":           Text("while() {") + Key("enter")+ Key("enter") + Text("}"),
                    "do while loop":        Text("do {") + Key("enter") + Key("enter") + Text("} while();"),
                    "for loop":             Text("for(;;) {") + Key("enter")+ Key("enter") + Text("}"),
                    "switch statement":     Text("switch() {") + Key("enter")+ Key("enter") + Text("}"),
                    "try catch":            Text("try {") + Key("enter")+ Key("enter") + Text("}") + Key("enter") + Text("catch() {") + Key("enter")+ Key("enter") + Text("}"),
                                  
               
               }

#Some syntax rules for functions, classes, etc. in C++
class CPPFunctionsAndClassesSyntax(MappingRule):
    
    mapping  = {
                    #function syntax stuff        
                    "function prototype":           Text("returnType functionName();"),
                    "function":                     Text("returnType functionName() {")+Key("enter")+ Key("enter")+ Text("}"),
                    #miscellaneous syntax stuff
                    "struct":               Text("struct structName {") + Key("enter")+ Key("enter") + Text("};"),
                    "union":                        Text("union unionName {") + Key("enter")+ Key("enter") + Text("};"),
                    "enumeration":                  Text("enum enumerationName {") + Key("enter")+ Key("enter") + Text("};"),
                    "type definition":              Text("typedef existingDatatype name;"),
                    "create namespace":             Text("namespace namespaceName {") + Key("enter")+ Key("enter") + Text("}"),
                    #class syntax stuff
                    "class":                        Text("class ClassName {") + Key("enter")+ Text("public:")+ Key("enter") + Key("enter") + Text("};"),
                    "constructor":                  Text("();") + Key("left")+ Key("left")+ Key("left"),
                    "destructor":                   Text("~();") + Key("left")+ Key("left")+ Key("left"),
                                  
               
               }


class CPPOperators(MappingRule):
    
    mapping  = {
                  "scope operator":                 Text("::"),
                  
                  "plus plus":                      Text("++"),
                  "minus minus":                    Text("--"),
                  "plus":                           Text("+"),
                  "minus":                          Text("-"),
                  "divided by":                     Text("/"),
                  "address of":                     Text("&"),
                  "left shift":                     Text(" << "),
                  "right shift":                    Text(" >> "),
                  "equals":                         Text("="),
                  "greater than":                   Text(">"),
                  "less than":              Text("<"),
                  "greater than or equal to":        Text(">="),
                  "less than or equal to":          Text("<="),
                  "equals equals":                      Text("=="),
                  "not equal to":                   Text("!="),
                  "logical and":      Text("&&"),
                    "logical or":       Text("||"),
                  "plus equals":            Text("+="),
                  "minus equals":               Text("-="),
                  
               
               }    

#Handles the C++ commenting syntax
class CPPCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("// "),
                "multiline comment":      Text("/*") + Key("enter") + Key("enter") + Text("*/") + Key("up")
               
               }

#Some useful miscellaneous C++ functions
class CPPUsefulFunctions(MappingRule):

    mapping  = {
                    "print statement":       Text("cout << ;") + Key("left"),
                    "input statement":       Text("cin >> ;") + Key("left"),
                    "end line":             Text("endl"),
            
               
               }

#Syntax for preprocessor directives in C++
class CPPPreprocessorDirectives(MappingRule):

    mapping  = {
                    "directive include":            Text("#include "),
                    "directive pragma":             Text("#pragma "),
                    "directive if":                 Text("#if "),
                    "directive else":               Text("#else"),
                    "directive else if":            Text("#elif "),
                    "directive if defined":         Text("#ifdef "),
                    "directive if not defined":     Text("#ifndef "),
                    "directive end if":             Text("#endif"),
                    "directive define":             Text("#define "),
                    "directive undefine":           Text("#undef "),
                    "directive error":              Text("#error"),
                    "directive line":               Text("#line ")
               
               }


#C++ datatypes
class CPPDataTypes(MappingRule):

    mapping  = {
                "integer":                  Text("int "),
                "float":                    Text("float "),
                "double":                   Text("double "),
                "boolean":                  Text("bool "),
                "char":                     Text("char "),
                "string":                   Text("string "),
                "long":                     Text("long "),
                "long double":              Text("long double "),
                "wide character":           Text("wchar_t "),
                "short":                    Text("short "),
                "constant":                 Text("const "),
                "null":                     Text("NULL"),

                #my attempt at a C++ script for shortcut float notation                
                "<n> point <n2> float":                Text("%(n)d.%(n2)d") + Text("f"),
                "<n> point <n2> <n3> float":                Text("%(n)d.%(n2)d%(n3)d") + Text("f"),
                "<n> point <n2> <n3> <n4> float":                Text("%(n)d.%(n2)d%(n3)d%(n4)d") + Text("f"),
                }
    extras   = [
                Integer("n", -1000, 1000),
                Integer("n2", 0, 1000),
                Integer("n3", 0, 1000),
                Integer("n4", 0, 1000)
                ]

class CPPEscapeSequences(MappingRule):

    mapping  = {
                    "escape quotes":            Text("\ ")+ Key("left") + Text("\"") + Text("\ ")+ Key("left") + Text("\""),
                    "escape single quotes":     Text("\ ")+ Key("left") + Text("\'") + Text("\ ")+ Key("left") + Text("\'"),
                    "escape line":              Text("\ ")+ Key("left") + Text("n"),
                    "escape tab":               Text("\ ")+ Key("left") + Text("t"), 
                    "escape carriage return":    Text("\ ")+ Key("left") + Text("r"),
                }     

    

CPPBootstrap = Grammar("C++ bootstrap")                # Create a grammar to contain the command rule.
CPPBootstrap.add_rule(CPPEnabler())
CPPBootstrap.load()

CPPGrammar = Grammar("C++ grammar")
CPPGrammar.add_rule(CPPTestRule())
CPPGrammar.add_rule(CPPControlStructures())
CPPGrammar.add_rule(CPPCommentsSyntax())
CPPGrammar.add_rule(CPPUsefulFunctions())
CPPGrammar.add_rule(CPPPreprocessorDirectives())
CPPGrammar.add_rule(CPPOperators())
CPPGrammar.add_rule(CPPEscapeSequences())
CPPGrammar.add_rule(CPPFunctionsAndClassesSyntax())
CPPGrammar.add_rule(CPPDataTypes())
CPPGrammar.add_rule(CPPDisabler())
CPPGrammar.load()
CPPGrammar.disable()

# Unload function which will be called by natlink at unload time.
def unload():
    global CPPGrammar
    if CPPGrammar: CPPGrammar.unload()
    CPPGrammar = None