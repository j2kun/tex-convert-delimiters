import sys
from lark import Lark

lark = Lark(r'''
         tex: content+

         ?content: mathmode | text+

         mathmode: OFFSETDOLLAR text+ OFFSETDOLLAR
         | OFFSETOPEN text+ OFFSETCLOSE
         | INLINE text+ INLINE

         INLINE: "$"
         OFFSETDOLLAR.2: "$$"
         OFFSETOPEN: "\\["
         OFFSETCLOSE: "\\]"

         ?text: /./s
         ''', start='tex', parser='lalr')


def join_tokens(tokens):
    return ''.join(x.value for x in tokens)


def handle_mathmode(tree_node):
    '''Switch on the different types of math mode, and convert
       the delimiters to the desired output, and then concatenate the
       text between.'''
    starting_delimiter = tree_node.children[0].type

    if starting_delimiter == 'INLINE':
        return '\\(' + join_tokens(tree_node.children[1:-1]) + '\\)'
    if starting_delimiter == 'OFFSETDOLLAR':
        return '\\[' + join_tokens(tree_node.children[1:-1]) + '\\]'
    if starting_delimiter == 'OFFSETOPEN':
        return '\\[' + join_tokens(tree_node.children[1:-1]) + '\\]'


def handle_content(tree_node):
    '''Each child is a Token node whose text we'd like to concatenate
       together.'''
    return join_tokens(tree_node.children)


input_text = sys.stdin.read()
parsed_doc = lark.parse(input_text)
output_doc = ''

for node in parsed_doc.children:
    if node.data == "content":
        output_doc += handle_content(node)
    if node.data == "mathmode":
        output_doc += handle_mathmode(node)

print(output_doc.rstrip('\n'))
