# Filename: interface_layout.py

import windows_curses as curses

class InterfaceLayout:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()  # Turn off automatic echoing of keys to the screen
        curses.cbreak()  # React to keys instantly, without requiring the Enter key
        self.screen.keypad(True)  # Let curses handle multibyte escape sequences for special keys
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.screen.bkgd(curses.color_pair(4))
        self.screen.box()
        self.screen.refresh()

    def display_user_input(self, user_input):
        self.screen.erase()
        self.screen.addstr(0, 0, user_input, curses.color_pair(1))
        self.screen.refresh()

    def display_conversation(self, conversation):
        self.screen.erase()
        self.screen.addstr(1, 0, conversation, curses.color_pair(2))
        self.screen.refresh()

    def display_timer(self, time_left):
        self.screen.erase()
        self.screen.addstr(2, 0, f"Time left: {time_left}", curses.color_pair(3))
        self.screen.refresh()

    def __del__(self):
        curses.echo()
        curses.nocbreak()
        self.screen.keypad(False)
        curses.endwin()
