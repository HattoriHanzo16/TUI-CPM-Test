import curses
from curses import wrapper
import time
from GetText import get


def opening(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome!", curses.color_pair(2))
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


def display(stdscr, target, current, wpm=0):
    stdscr.addstr(2, 0, target)
    stdscr.addstr(0, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if correct_char != char:
            color = curses.color_pair(2)

        stdscr.addstr(2, i, char, color)


def wpm_test(stdscr):
    target_text = get()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_end = max(time.time() - start_time, 1)

        wpm = round((len(current_text) / (time_end/60))/5)

        stdscr.erase()
        display(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        joined_text = "".join(current_text)
        if joined_text == (target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if len(key) == 1 and ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    opening(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.erase()
        stdscr.addstr(
            4, 4, "Finished! Press ESC key to Exit.\nPress any key to continue...")
        key1 = stdscr.getkey()
        if ord(key1) == 27:
            break


wrapper(main)
