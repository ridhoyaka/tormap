# TORMAP

TORMAP is a simple CLI-based network scanning tool built with Python.  
It helps users discover active hosts, scan open ports, and identify devices within the same local network.

This project is created mainly for learning, experimentation, and basic network analysis.

---

## Features

- Host discovery (check whether a host is up or down)
- Basic port scanning (default or custom ports)
- Fast scan using common ports
- Scan active devices on the same local network (ARP scan)
- Export scan results to JSON
- Clean and interactive terminal interface

---

## Screenshots

![Preview](tormap/preview.png)

---

## Requirements

- Python 3.8 or higher
- Linux / Windows / macOS
- `arp-scan` (optional, Linux only)

---

## Installation (Linux)

Clone the repository :
```bash
git clone https://github.com/yourusername/tormap.git
cd tormap
pip install -r requirements.txt
sudo apt install arp-scan
```

---

## Usage

```bash
python3 main.py
```
