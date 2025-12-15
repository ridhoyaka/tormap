"""Helpers to print results in a nicer table; minimal dependency approach."""
from typing import Dict


def print_table(address: str, is_up: bool, ports: Dict[int, str]):
    print(f"\nResult for: {address}")
    print(f"Status: {'UP' if is_up else 'DOWN'}")
    print('-' * 40)

    if not ports:
        print('No ports scanned')
        return

    print(f"{'PORT':>6} | STATUS")
    print('-' * 40)

    for p, s in sorted(ports.items()):
        print(f"{p:6d} | {s}")
