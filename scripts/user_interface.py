# Filename: data/scripts/user_interface.py
import curses

class InterfaceLayout:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.start_color()
        self._init_colors()
        self.screen.bkgd(curses.color_pair(4))
        self.screen.box()
        self.max_y, self.max_x = self.screen.getmaxyx()
        self._init_windows()

    def _init_colors(self):
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)    # User input
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Conversation
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Timer
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Game state

    def _init_windows(self):
        # Main layout areas
        self.header_win = self.screen.subwin(1, self.max_x, 0, 0)
        self.conversation_win = self.screen.subwin(self.max_y-4, self.max_x, 1, 0)
        self.status_win = self.screen.subwin(3, self.max_x, self.max_y-3, 0)
        self._refresh_all()

    def _refresh_all(self):
        self.screen.noutrefresh()
        self.header_win.noutrefresh()
        self.conversation_win.noutrefresh()
        self.status_win.noutrefresh()
        curses.doupdate()

    def display_header(self, text):
        self.header_win.erase()
        self.header_win.addstr(0, 0, text[:self.max_x-2], curses.color_pair(1))
        self._refresh_all()

    def display_conversation(self, text):
        self.conversation_win.erase()
        wrapped_text = self._wrap_text(text, self.max_x-2)
        for i, line in enumerate(wrapped_text[:self.max_y-5]):
            self.conversation_win.addstr(i, 0, line, curses.color_pair(2))
        self._refresh_all()

    def display_status(self, time_left, location, score):
        self.status_win.erase()
        status_line = f"Time: {time_left} | Location: {location} | Score: {score}"
        self.status_win.addstr(0, 0, status_line[:self.max_x-2], curses.color_pair(3))
        self._refresh_all()

    def display_input_prompt(self):
        input_win = self.screen.subwin(1, self.max_x, self.max_y-1, 0)
        input_win.erase()
        input_win.addstr(0, 0, "> ", curses.color_pair(4))
        input_win.refresh()

    def _wrap_text(self, text, width):
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 > width:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word) + 1

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def __del__(self):
        curses.echo()
        curses.nocbreak()
        self.screen.keypad(False)
        curses.endwin()