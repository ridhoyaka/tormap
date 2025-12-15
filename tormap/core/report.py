"""Report helpers: produce readable summaries and export capability."""
import json
from typing import Dict

def format_report(address: str, is_up: bool, ports: Dict[int, str]) -> str:
    lines = []
    lines.append(f"Host: {address}")
    lines.append(f"Status: {'UP' if is_up else 'DOWN'}")
    lines.append("Ports:")
    if not ports:
        lines.append(" (no ports scanned)")
    else:
        for p, s in sorted(ports.items()):
            lines.append(f" {p:5d} : {s}")
    return "\n".join(lines)
def export_json(path: str, address: str, is_up: bool, ports: Dict[int, str]):
    payload = {
        'address': address,
        'is_up': is_up,
        'ports': ports,
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)