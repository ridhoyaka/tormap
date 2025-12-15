"""Optional executor that can call nmap (if installed) via python-nmap.
This file is kept optional; the rest of the package does not require python-nmap.
"""

try:
    import nmap
except Exception:
    nmap = None
class NmapExecutor:
    def __init__(self):
        if nmap is None:
            raise RuntimeError("python-nmap is not installed or nmap binary is missing")
        self._nm = nmap.PortScanner()
    def simple_scan(self, host: str, ports: str):
        return self._nm.scan(hosts=host, ports=ports)
