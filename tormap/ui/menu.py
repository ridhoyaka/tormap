"""Main interactive menu for TORMAP."""
from tormap.ui.effects import spinner, print_colored
from tormap.core.scanner import HostScanner, PortScanner
from tormap.core.host import Host
from tormap.core.report import format_report, export_json
import subprocess

def run_arp_scan():
    print("\nMenjalankan arp-scan untuk mendeteksi host aktif di jaringan...")
    try:
        output = subprocess.check_output(
            ["sudo", "arp-scan", "-l"],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        print("\n=== HASIL ARP-SCAN ===\n")
        print(output)

    except FileNotFoundError:
        print("Error: arp-scan belum terinstall.")
        print("Install dengan: sudo apt install arp-scan")

    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat menjalankan arp-scan:")
        print(e.output)

def main_menu():
    last_result = None 

    while True:
        print_colored('\nMenu TORMAP :', 'cyan')
        print_colored(' [1] Host Discovery', 'yellow')
        print_colored(' [2] Port Scanning (Basic)', 'yellow')
        print_colored(' [3] Fast Scan (Top Ports)', 'yellow')
        print_colored(' [4] Export last result to JSON', 'yellow')
        print_colored(' [5] Scan LAN Active Hosts (arp-scan)', 'yellow')
        print_colored(' [0] Exit', 'yellow')

        choice = input('\nPilih menu : ').strip()

        # =====================================
        # 1. HOST DISCOVERY
        # =====================================
        if choice == '1':
            addr = input('Masukkan IP/Host : ').strip()
            h = Host(addr)

            with spinner('Checking host...'):
                hs = HostScanner(addr)
                up = hs.scan()
                h.set_up(up)

            print('\n' + format_report(h.address, h.is_up, {}))
            last_result = (h.address, h.is_up, {})

        # =====================================
        # 2. BASIC PORT SCAN
        # =====================================
        elif choice == '2':
            addr = input('Masukkan IP/Host: ').strip()
            ports_raw = input('Masukkan port (pisah spasi, contoh: 22 80 443): ').strip()

            try:
                ports = [int(p) for p in ports_raw.split()]
            except ValueError:
                print_colored('Input port tidak valid. Kembali ke menu.', 'red')
                continue

            h = Host(addr)

            with spinner('Scanning host...'):
                hs = HostScanner(addr)
                h.set_up(hs.scan())

            with spinner('Scanning ports...'):
                ps = PortScanner(addr, ports)
                res = ps.scan()
                h.set_ports(res)

            print('\n' + format_report(h.address, h.is_up, h.port_results))
            last_result = (h.address, h.is_up, h.port_results)

        # =====================================
        # 3. FAST SCAN
        # =====================================
        elif choice == '3':
            addr = input('Masukkan IP/Host: ').strip()
            top_ports = [22, 80, 443, 8080, 3306]

            h = Host(addr)

            with spinner('Fast scan in progress...'):
                hs = HostScanner(addr)
                h.set_up(hs.scan())
                ps = PortScanner(addr, top_ports)
                res = ps.scan()
                h.set_ports(res)

            print('\n' + format_report(h.address, h.is_up, h.port_results))
            last_result = (h.address, h.is_up, h.port_results)

        # =====================================
        # 4. EXPORT TO JSON
        # =====================================
        elif choice == '4':
            if last_result is None:
                print_colored('Belum ada hasil scan. Lakukan scan terlebih dahulu.', 'red')
                continue

            path = input('Masukkan nama file JSON (misal: result.json): ').strip()
            addr, is_up, ports = last_result

            export_json(path, addr, is_up, ports)
            print_colored(f'Hasil berhasil diexport ke "{path}".', 'green')
        # =====================================
        # 5. Scan LAN Active
        # =====================================
        elif choice == "5":
            run_arp_scan()

        # =====================================
        # EXIT
        # =====================================
        elif choice == '0':
            print_colored('\nThanks for using TORMAP!', 'green')
            break

        # =====================================
        # INVALID CHOICE
        # =====================================
        else:
            print_colored('Pilihan tidak valid. Coba lagi.', 'red')