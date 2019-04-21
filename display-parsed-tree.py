import sys
from lark import Lark

lark = Lark(r'''
         tex: content+

         ?content: mathmode | text+

         mathmode: OFFSETDOLLAR text+ OFFSETDOLLAR
         | OFFSETOPEN text+ OFFSETCLOSE
         | INLINEOPEN text+ INLINECLOSE
         | INLINE text+ INLINE

         INLINE: "$"
         INLINEOPEN: "\\("
         INLINECLOSE: "\\)"
         OFFSETDOLLAR: "$$"
         OFFSETOPEN: "\\["
         OFFSETCLOSE: "\\]"

         ?text: /./s
         ''', start='tex', parser='lalr')


input_text = sys.stdin.read()
parsed_doc = lark.parse(input_text)
print(parsed_doc)
