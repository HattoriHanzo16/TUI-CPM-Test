import curses
from curses.textpad import Textbox, rectangle


# get username as an input


def getName(stdscr, w, h):
    editwin = curses.newwin(2, 7, h//2, w//2-7)
    stdscr.addstr(h//2-10, w//2,
                  """
                                Hey There! 

                          Tell us your name first 
                    
                            and press ctrl + g""")
    rectangle(stdscr, h//2-2, w//2-12, h//2+2, w//2+12)
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
    press s for javascript (default)
""", curses.color_pair(2))
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
