"""
Core scanning classes: Scanner base, HostScanner, PortScanner
Simple, synchronous implementations designed to be easy to extend.
"""

import socket
import time
from typing import List, Dict

class Scanner:
    """Base scanner class providing common properties and interface."""
    def __init__(self, host: str, timeout: float = 1.0):
        self.host = host
        self.timeout = timeout
        socket.setdefaulttimeout(self.timeout)
    def scan(self):
        raise NotImplementedError("scan() must be implemented by subclass")
class HostScanner(Scanner):
    """
    Check whether a host is reachable using a TCP connect to port 80.
    Simple implementation (no ICMP).
    """
    def scan(self) -> bool:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.host, 80))
            s.close()
            return True
        except Exception:
            return False
class PortScanner(Scanner):
    """
    Scan multiple TCP ports by attempting a connect().
    Returns: {22: 'open', 80: 'closed'}
    """
    def __init__(self, host: str, ports: List[int], timeout: float = 1.0):
        super().__init__(host, timeout)
        self.ports = ports
    def _scan_port(self, port: int) -> bool:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.host, port))
            s.close()
            return True
        except Exception:
            return False
    def scan(self) -> Dict[int, str]:
        results = {}
        for p in self.ports:
            is_open = self._scan_port(p)
            results[p] = "open" if is_open else "closed"
            time.sleep(0.05)
        return results