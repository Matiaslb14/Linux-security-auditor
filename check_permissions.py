import sys

def check_permissions(file_path):
    with open(file_path, 'r') as f:
        files = f.readlines()

    if not files:
        print("\n[✓] No se encontraron archivos con permisos 777. Perfecto.")
        return

    print("\n[!] Archivos con permisos 777 detectados (¡riesgo de seguridad!):")
    for file in files:
        print(f" - {file.strip()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python check_permissions.py <ruta_archivo_permisos>")
        sys.exit(1)

    check_permissions(sys.argv[1])
