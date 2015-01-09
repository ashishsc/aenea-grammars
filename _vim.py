# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Vim
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    Dictation,
    IntegerRef,
    Text,
    Choice
)
import dragonfly

from _generic_edit import pressKeyMap

vim_context = aenea.ProxyCustomAppContext(executable="gnome-terminal")
grammar = dragonfly.Grammar('vim', context=vim_context)

surroundCharsMap = {
    'quotes': '"',
    'parens': "(",
    'brackets': "[",
    'braces': "{",
}


def goto_line(n):
    for c in str(n):
        Key(c).execute()
    Key("G").execute()

def yank_lines(n, n2):
    goto_line(n)
    Key("V").execute()
    goto_line(n2)
    Key("y").execute()

def delete_lines(n, n2):
    goto_line(n)
    Key("V").execute()
    goto_line(n2)
    Key("d").execute()


basics_mapping = aenea.configuration.make_grammar_commands('vim', {
    'vim': Text("vim"),

    # ctrl p
    '(fuzzy find|open fuzzy)': Key("escape, c-p"),
    ' fuzzy split-horizontal': Key('c-s'),
    ' fuzzy split-vertical': Key('c-v'),

    # Moving between splits
    'split-left': Key("escape, c-h"),
    'split-right': Key("escape, c-l"),
    'split-up': Key("escape, c-k"),
    'split-down': Key("escape, c-j"),
    'split-close': Key("escape, colon, q, enter"),
    'open [in] split': Key("s"),
    'open [in] tab': Key("t"),
    'split-vertical': Key('escape, c-w,v'),
    'split-horizontal': Key('escape, c-w,s'),

    # Moving viewport
    'bund': Key("escape, 2, 0, c-y"),
    'fund': Key("escape, 2, 0, c-e"),
    'screen down': Key("escape, c-f"),
    'screen up': Key("escape, c-b"),

    # Code folding
    'fold all': Key("escape, z, M"),
    'unfold all': Key("escape, z, R"),
    'fold': Key("escape, z, c"),
    'fold deep': Key("escape, z, C"),
    'unfold': Key("escape, z, o"),
    'unfold deep': Key("escape, z, O"),

    # Code fold motions
    'fold up': Key("escape, z, k"),
    'fold down': Key("escape, z, j"),

    # Center on line
    'center': Key("escape, z, z"),

    # Append to line
    'noop <n>': Key("escape") + Function(goto_line) + Key("A, enter"),
    'noop': Key("escape, A, enter"),
    'nope': Key("escape, A"),
    'nope <n>': Key("escape") + Function(goto_line) + Key("A"),

    'prepend': Key("escape, I"),
    'insert': Key("i"),
    'insert below': Key("escape, o"),
    'insert above': Key("escape, O"),
    'undo': Key("escape, u, i"),
    'scratch': Key("escape, u, i"),
    'escape': Key("escape"),
    'filename': Key("escape, c-g"),
    'save': Key("escape, colon, w, enter"),
    'save and quit': Key("escape, colon, w, q, enter"),
    'quit all': Key("escape, colon, q, a, enter"),
    'discard': Key("escape, colon, q, exclamation"),
    'vim tab <n>': Key("escape, comma, %(n)d"),
    'comma': Key("comma"),
    'comes': Key("comma, space"),
    'listed': Key("escape, s-a, comma, enter"),
    'cause': Key("colon, space"),

    # Finding text
    'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),
    'clear search': Key("escape, colon, n, o, h, enter"),

    # Character operations
    'dart': Key("escape, x"),
    'dart <n>': Key("escape, x:%(n)d"),
    'replace letter': Key("r"),
    'replace mode': Key("R"),
    'change case': Key("escape, right, s-backtick, i, left"),
    'change case back': Key("escape, b, s-backtick, e, a"),

    # Word operations
    '(doord|doored|gord)': Key("right, escape, d, i, w, i"),
    '(doord|doored|gord) back': Key("right, escape, b, d, w, i"),
    '(doord|doored|gord) <n>': Key("right, escape, %(n)d, d, w, i"),
    '(doord|doored|gord) back <n>': Key("right, escape, %(n)d, b, %(n)d, d, w, i"),
    'chord': Key("right, escape, c, i, w"),
    'chord <n>': Key("escape, c, %(n)d, w"),
    'sword': Key("escape, v, e"),
    'sword <n>': Key("escape, v, e:%(n)d"),
    'forward':  Key("escape,  w, i"),
    'forward <n>': Key("escape, %(n)d, w, i"),
    'backward': Key("escape, b, i"),
    'backward <n>': Key("escape, %(n)d, b, i"),
    'stripword': Key("escape, b, left, del, e, a"),

    # Line operations
    'dine': Key("escape, d:2"),
    'dine <n>': Key("escape") + Function(goto_line) + Key("d:2"),
    'dine <n> (thru|through|to) <n2>': Key("escape") + Function(delete_lines),
    'yine': Key("escape, y:2"),
    'yine <n>': Key("escape") + Function(goto_line) + Key("y:2"),
    'yine <n> (thru|through|to) <n2>': Key("escape") + Function(yank_lines),
    'yine system': Key("escape, dquote, plus, y:2"),
    'yine mouse': Key("escape, dquote, asterisk, y:2"),

    'select until <pressKey>': Key("escape, v, t") + Text("%(pressKey)s"),
    'select including <pressKey>': Key("escape, v, f") + Text("%(pressKey)s"),
    'dell until <pressKey>': Key("escape, d, t") + Text("%(pressKey)s"),
    'dell including <pressKey>': Key("escape, d, f") + Text("%(pressKey)s"),

    # Copy and Paste
    'yank': Key("escape, y"),
    'extract': Key("escape, x"), # FIXME: Same as dart?
    'glue': Key('escape, p'),

    # Movement
    'up <n> (lines|line)': Key("%(n)d, up"),
    'down <n> (lines|line)': Key("%(n)d, down"),
    'go to [line] <n>': Key("escape") + Function(goto_line),
    'jump top': Key("escape, g,g"),
    'jump bottom': Key("escape, G"),
    'jump out': Key("c-o"),
    'jump in': Key("c-i"),
    'jump high|hi': Key('H'),
    'jump mid|middle': Key('M'),
    'jump low': Key('L'),
    'matching': Key("escape, percent"),
    '(boop|easy motion)': Key("escape, comma, comma, s"),
    })


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [
        Dictation('text'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
        Choice("pressKey", pressKeyMap),
        Choice("surroundChar", surroundCharsMap),
    ]

grammar.add_rule(Basics())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
