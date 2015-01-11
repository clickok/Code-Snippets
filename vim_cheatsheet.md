## Common

i == enter insert mode
a == append (go to space after cursor and enter insert mode)
A == go to end of current line and enter insert mode 
o == open a line below cursor and enter insert mode
O == open a line above cursor and enter insert mode

h, j, k, l == left, down, up, right

u == undo the last command
U == perform available undos over a single line
ctrl-r == redo the last command

v (motion) == visual selection
    * Can then use commands to operate on selection
    * e.g., v$ :w FILENAME would write to end of current line to FILENAME

y == copy (yank) selected text
    * can use as an operator, e.g. `y$` to copy until end of line
p == put previously copied/deleted text after the cursor

r (character) == replace the character at the cursor 
R (text) == replace starting at cursor with text
c (motion) == change following the motion

ctrl-g == show location in file and file status
gg == move to start of file
G == move to end of file
(line number) + G == move to the line given by line number

:! COMMAND == execute command in shell

## Searching 

/ + (phrase) == search for phrase
    * type `n` to search for the same phrase again
    * type `N` to search in the opposite direction
? + (phrase) == backwards search
ctrl-o == go back through file movement operations
ctrl-i == go forward through file movement operations

% == find matching parentheses

:s/(old)/(new) == substitute `new` for first `old` in line
:s/(old)/(new)/g == subtitute `new` for all occurences of `old` in line
:#1,#2s/old/new/g == change all occurences of `old` in range from line `#1` to line `#2`
:%s/old/new/g == change every occurence in the entire file
:%s/old/new/gc == find every occurence in the whole file, with prompt to change or not

### Options

* hlsearch, hls == highlight search
* incsearch, is  == incremental search
* ic == ignore case

### Various Commands 

:w FILENAME  == write file to FILENAME


:r FILENAME == insert contents of file at cursor
:r ! COMMAND == insert contents of command at cursor

## Motions

0 == go to start of current line
e == go to end of current word
w == go to start of next word
$ == go to end of current line

### Modifiers

Typing a number before a motion repeats it that many times

x  == delete character under cursor

d  == delete (motion)
de == delete to the end of the current word
dw == delete until start of the next word
dd == delete line
d$ == delete from cursor to end of line

## Setting Options

:set (option) == set the option
    * e.g., `:set ic` sets ignore case for searching
    * unset the option (typically) by prefixing `no` to it
        * e.g., `:set noic`

## Completion

Type something, then
    * ctrl+d == show a list of commands that start with what was typed
    * TAB == cycle through possible completions

## Getting Help

:help 
:help (text)


