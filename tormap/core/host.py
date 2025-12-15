"""Simple Host model storing scan information."""

from typing import Dict
class Host:
    def __init__(self, address: str):
        self.address = address
        self.is_up = False
        self.port_results: Dict[int, str] = {}
    def set_up(self, status: bool):
        """Store UP/DOWN status."""
        self.is_up = status
    def set_ports(self, results: Dict[int, str]):
        """Store port scan results."""
        self.port_results = results
