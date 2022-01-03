import curses
from curses import wrapper
from getSnippet import getSnippet
from opening import *
from getSnippet import getSnippet
import time


def display(stdscr, target, current, w, wpm=0,):
    stdscr.addstr(5, 4, target)
    stdscr.addstr(1, w//2-5, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if correct_char != char:
            color = curses.color_pair(2)

        stdscr.addstr(5, i+4, char, color)


# code per minute counter. choice is programming language


def cpm_test(stdscr, choice, width):

    target_text = getSnippet(choice)
    while len(target_text) > width:
        target_text = getSnippet(choice)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_end = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_end/60))/5)

        stdscr.erase()
        display(stdscr, target_text, current_text, width, wpm)
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

        # Handling deleting characters
        if key in ("KEY_BACKSPACE"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)


# main method
def main(stdscr):
    height, width = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    name = getName(stdscr, width, height)
    lang = choose_language(stdscr)
    opening(stdscr, name)

    while True:
        cpm_test(stdscr, lang, width)
        stdscr.erase()
        stdscr.addstr(
            5, 5, "Finished! Press ESC key to Exit.\nPress any key to continue...")

        key1 = stdscr.getkey()
        if ord(key1) == 27:
            break


wrapper(main)
