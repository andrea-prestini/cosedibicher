#!/usr/bin/python3


class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome

    @property
    def cane(self):
        return self.animale

    @cane.setter
    def cane(self, value):
        self.animale = value


class Animale:

    def __init__(self, razza):
        self.razza = razza


io = Persona("andrea", "prestini")
tu = Persona("mario", "mometto")
io.animale = "buffy"
tu.animale = "penelope"
print(io.animale)
print(tu.animale)

"""ctrl-o ctrl-i ctrl-] ctrl-t
map something mapped only for this session of vim
g; g, cycle through changes
:arga filename create a buffer with filename
:edit filename create a buffer and switch to it
:20vs . create a 20caracters windows split with dirs
vimgrep parola % + cdo s/.. sostituisce le occorrenze di vimgrep
cw view list of result command vimgrep
cdo :normal gUiw modifica tutte le occorenze trovate
argdo %s/pattern/replace/ge | update
:copen apre finestra args
argdo edit! reverse all changes before saving
argdo update for write all files in one step
vimgrep /pattern/ ## search in arglist load in quickfix
dip delete all paragraph: a paragraph is lines before an empty line!
g// list of lines that results of search
install ctags; run ctags -R create file tags... CTRL] to find original object
:\v(...) tutto quello che segue viene eseguito come caratteri ASCII
"""
