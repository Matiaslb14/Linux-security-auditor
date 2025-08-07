import sys

# Servicios inseguros que queremos detectar (puedes ampliar esta lista)
blacklist = [
    'telnet.service',
    'ftp.service',
    'rsh.service',
    'tftp.service',
    'avahi-daemon.service'
]

def analizar_servicios(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    print("\n[!] Servicios activos inseguros detectados:")
    found = False
    for servicio in blacklist:
        for linea in lines:
            if servicio in linea:
                print(f" - {servicio}")
                found = True
    if not found:
        print(" - Ninguno")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python analyze_services.py <ruta_archivo_servicios>")
        sys.exit(1)

    analizar_servicios(sys.argv[1])
