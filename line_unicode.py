import time, curses

def main(win):
    win.hline(0, 1, "-", 1000)
    win.vline(0, 0, "|", 1000)
    message = u"hello わたし!┌┌┌┌"
    win.addstr(0, 0, message.encode("utf-8"), curses.A_BLINK)
    win.refresh()
    time.sleep(3)


curses.wrapper(main)