"""Small UI helpers: spinner context manager and colored print.
Uses simple console tricks for portability.
"""

import sys
import threading
import itertools
import time
from colorama import Fore, Style, init
from contextlib import contextmanager

init(autoreset=True)

def print_colored(text: str, color: str = 'white') -> None:
    """Print colored text using colorama."""
    mapping = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
    }
    col = mapping.get(color.lower(), Fore.WHITE)
    print(col + text + Style.RESET_ALL)

class _Spinner:
    """Simple terminal spinner animation."""
    def __init__(self, text='working'):
        self.text = text
        self._running = False
        self._thread = None

    def _spin(self):
        for ch in itertools.cycle(['|', '/', '-', '\\']):
            if not self._running:
                break
            sys.stdout.write(f'\r{self.text} {ch}')
            sys.stdout.flush()
            time.sleep(0.12)

        # clear line after stop
        sys.stdout.write('\r' + ' ' * (len(self.text) + 3) + '\r')
        sys.stdout.flush()

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(0.2)
@contextmanager
def spinner(text='processing...'):
    """Context manager for spinner animation."""
    s = _Spinner(text)
    try:
        s.start()
        yield s
    finally:
        s.stop()