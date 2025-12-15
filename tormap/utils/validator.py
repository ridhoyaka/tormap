"""Simple validation helpers (IP and port checks)."""
import socket

def is_valid_ip(host: str) -> bool:
  try:
    socket.inet_aton(host)
    return True
  except Exception:
    return False
  def is_valid_port(p: int) -> bool:
    return 1 <= p <= 65535