# Author: Ashish

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Function
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise




#if "tmux-prefix" not in config:
    #print("Missing required 'tmux-prefix' in config file")
#tmux_prefix = config["tmux-prefix"]
## TODO: Add more support for various prefix keys
#if tmux_prefix == "space":
    #tmux_prefix = "space"
#else:
    #tmux_prefix = "b" # default tmux prefix
#tmux_prefix = "c-" + tmux_prefix
#tmux_grammar.add_rule(Mapping(tmux_prefix))

class Mapping (dragonfly.MappingRule):
    tmux_prefix = "c-space"
    mapping = aenea.configuration.make_grammar_commands('tmux', {
        'pane left': Key("c-h"),
        'pane right': Key("c-l"),
        'pane down': Key("c-j"),
        'pane up': Key("c-k"),
        'session': Key(tmux_prefix + "-s")
    })
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
        dragonfly.IntegerRef('appnum', 1, 99),
    ]


tmux_context = aenea.ProxyCustomAppContext(executable='tmux')
tmux_grammar = dragonfly.Grammar('tmux', context=tmux_context)
tmux_grammar.add_rule(Mapping(tmux_prefix))
tmux_grammar.load()
