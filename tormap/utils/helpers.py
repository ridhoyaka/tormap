"""Generic helpers used across TORMAP."""

import socket
import ipaddress
from typing import Optional

def is_valid_ip(target: str) -> bool:
    """Return True if the string is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False
def resolve_hostname(host: str) -> Optional[str]:
    """Try to resolve hostname to IP. Returns None if failed."""
    try:
        return socket.gethostbyname(host)
    except Exception:
        return None
def normalize_target(target: str) -> str:
    """Normalize input target into a valid IP if possible."""
    if is_valid_ip(target):
        return target
    resolved = resolve_hostname(target)
    return resolved if resolved else target
def check_reachability(host: str, timeout: float = 1.0) -> bool:
    """
    Quick reachability check using socket.
    Not fully accurate like ping, but fast and portable.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, 80))  # try port 80
        sock.close()
        return result == 0
    except Exception:
        return False
