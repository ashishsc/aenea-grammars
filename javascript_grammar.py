# Author: Ashish
import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    IntegerRef,
    Text,
    Dictation,
)

from format import format_snake_case, format_pascal_case, format_camel_case
import dragonfly

def create_anon_function(text):
    Text('function() {\n}').execute()

def create_named_function(text):
    Text('var %s = function(){\n}' % format_camel_case(text)).execute()

javascript_mapping = aenea.configuration.make_grammar_commands('javascript', {
    'var': Text("var "),
    'new (function|func)': Function(create_anon_function)
})

class Javascript (dragonfly.MappingRule):
    mapping = javascript_mapping
    extras = [
        Dictation('text'),
        Dictation('text2'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
    ]


def get_grammar(context):
    javascript_grammar = dragonfly.Grammar('javascript', context=context)
    javascript_grammar.add_rule(Javascript())
    return javascript_grammar
