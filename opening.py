import curses
from curses.textpad import Textbox, rectangle


# get username as an input
def getName(stdscr):
    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1+5+1, 1+30+1)
    stdscr.refresh()
    box = Textbox(editwin)
    box.edit()
    name = box.gather()
    return name


# menu,to choose the language
def choose_language(stdscr):
    stdscr.erase()
    stdscr.addstr("""
    Choose your language:
    press j for java
    press p for python
    press s for javascript
""")
    key = stdscr.getkey()

    if ord(key) == ord('j'):
        return 'java'
    elif ord(key) == ord('p'):
        return 'python'
    else:
        return 'javaScript'


# intro
def opening(stdscr, name):
    stdscr.erase()
    stdscr.addstr(f"Welcome! {name}", curses.color_pair(2))
    stdscr.addstr("""
    ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | [ | ] | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
| ->| | " | , | . | P | Y | F | G | C | R | L | / | = |  \  |
|-----',--',--',--',--',--',--',--',--',--',--',--',--'-----|
| Caps | A | O | E | U | I | D | H | T | N | S | - |  Enter |
|------'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--------|
|        | ; | Q | J | K | X | B | M | W | V | Z |          |
|------,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
| ctrl |  | alt |                          | alt  |  | ctrl |
'------'  '-----'--------------------------'------'  '------'

    """, curses.color_pair(1))
    stdscr.addstr("\n\n For Exit: Press ESC key", curses.color_pair(2))
    stdscr.addstr("\n For Continue: Press any key", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()
