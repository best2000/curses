import time
import curses

def main(stdscr):
    curses.echo(True)
    curses.cbreak(True)

    stdscr.addstr(5, 10, "Hello, world!")
    x = stdscr.getstr(0,0, 10) #dont care cbreak

    stdscr.refresh()

    stdscr.addstr(7, 10, x)
    stdscr.refresh()
    time.sleep(3)

    stdscr.clear()


curses.wrapper(main)