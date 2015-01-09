# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with terminal and desktop environment
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

terminal_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('terminal', context=terminal_context)

tmux_prefix = "c-space"
terminal_mapping = aenea.configuration.make_grammar_commands('terminal', {
    # Terminal commands
    # dir is hard to say and recognize. Use something else
    'deer up': Text("cd ..") + Key("enter"),
    'deer list': Text("ls") + Key("enter"),
    'deer list all': Text("ls -lha") + Key("enter"),
    'deer list details': Text("ls -lh") + Key("enter"),
    'deer into': Text("cd "),

    '(terminal|term) clear': Text("clear") + Key("enter"),
    '(terminal|term) left': Key("c-pgup"),
    '(terminal|term) right': Key("c-pgdown"),
    '(terminal|term) new [tab]': Key("cs-t"),
    '(terminal|term) new cinnamon': Key("cs-n"),

    # Common words
    '(pseudo|sudo|pseudo-)': Text("sudo "),
    '(apt|app) get': Text("sudo apt-get "),
    '(apt|app) get install': Text("sudo apt-get install "),

    # tmux
    'pane left': Key("c-h"),
    'pane right': Key("c-l"),
    'pane-split-vertical': Key(tmux_prefix + ", l"),
    'pane down': Key("c-j"),
    'pane-split-horizontal': Key(tmux_prefix + ", j"),
    '(pane-kill|pane-close)': Key(tmux_prefix + ", x"),
    'pane up': Key("c-k"),
    'session': Key(tmux_prefix + ", s"),
    'pane new': Key(tmux_prefix + ", c"),
    'pane next': Key(tmux_prefix + ",  n"),
    'pane zoom': Key(tmux_prefix + ", z"),
})


class Mapping(dragonfly.MappingRule):
    mapping = terminal_mapping
    extras = []

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
