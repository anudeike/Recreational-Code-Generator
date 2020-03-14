import json
from parsimonious.grammar import Grammar, NodeVisitor

"""
"some literal"	Used to quote literals. Backslash escaping and Python conventions for "raw" and Unicode strings help support fiddly characters.
[space]	Sequences are made out of space- or tab-delimited things. a b c matches spots where those 3 terms appear in that order.
a / b / c	Alternatives. The first to succeed of a / b / c wins.
thing?	An optional expression. This is greedy, always consuming thing if it exists.
&thing	A lookahead assertion. Ensures thing matches at the current position but does not consume it.
!thing	A negative lookahead assertion. Matches if thing isn't found here. Doesn't consume any text.
things*	Zero or more things. This is greedy, always consuming as many repetitions as it can.
things+	One or more things. This is greedy, always consuming as many repetitions as it can.
~r"regex"ilmsuxa	Regexes have ~ in front and are quoted like literals. Any flags follow the end quotes as single chars. Regexes are good for representing character classes ([a-z0-9]) and optimizing for speed. The downside is that they won't be able to take advantage of our fancy debugging, once we get that working. Ultimately, I'd like to deprecate explicit regexes and instead have Parsimonious dynamically build them out of simpler primitives.
(things)	Parentheses are used for grouping, like in every other language.
"""

# call a subclass of NodeVisitor -> from the grammar
class IniVisitor(NodeVisitor):
    def visit_expr(self, node, visited_children):
        """ Returns the overall output. """
        output = {}
        for child in visited_children:
            output.update(child[0])
        return output

    def visit_entry(self, node, visited_children):
        """ Makes a dict of the section (as key) and the key/value pairs. """
        key, values = visited_children
        return {key: dict(values)}

    def visit_section(self, node, visited_children):
        """ Gets the section name. """
        _, section, *_ = visited_children
        return section.text

    def visit_pair(self, node, visited_children):
        """ Gets each key/value pair, returns a tuple. """
        key, _, value, *_ = node.children
        return key.text, value.text

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node

class VeraVisitor(NodeVisitor):
    def visit_expr(self, node, visited_children):
        # should return the overall output
        #print(str(node))

        output = {}
        for child in visited_children:
            output.update(child[0])

        return output

    def visit_start(self, node, visited_children):
        """ Gets the start """
        _, start, *_ = visited_children
        return start.text

    def visit_entry(self, node, visited_children):
        """ Makes a dict of the section (as a key and the k/v pairs"""
        key, values = visited_children
        return {key: dict(values)}

    def visit_definition(self, node, visited_children):
        """ gets the definition pair"""

        # format is let ws key = value
        # since we only care about the key and the value, those are the things we extract
        let, _, key, _, value, *_ = node.children
        print("Key: " + str(key))
        print("Value: " + str(value))
        print("Value Type: " + str(value.text) + "\n")
        return key.text, value.text

    def generic_visit(self, node, visited_children):
        """ generic visit overloaded"""
        return visited_children or node


data = """#start#
let a = 5
let b = 9
let c = 8
let d = "a string"
"""

# works so far!
grammar = Grammar( r"""
    expr        = (entry / emptyline)*
    entry       = start definition*

    start       = ws "#start#" ws
    definition  = "let" ws key assign value ws?
    key         = word+
    value       = (number / word / quoted)+ 
    number      = ~"[0-9]"+
    word        = ~r"[-\w]+"
    quoted      = ~'"[^\"]+"'
    assign       = ws? "=" ws?
    lpar        = "["
    rpar        = "]"
    ws          = ~"\s*"
    emptyline   = ws+
    """)

# create the abstract syntax tree.
tree = grammar.parse(data)

va = VeraVisitor()
out = va.visit(tree)
print(out)

#print(tree)

