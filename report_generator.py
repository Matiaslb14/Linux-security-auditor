import sys
import os

def generate_report(tmp_dir):
    report_path = 'reports/audit_report.txt'
    os.makedirs('reports', exist_ok=True)

    # Leer archivos con info
    def read_file(file):
        try:
            with open(os.path.join(tmp_dir, file), 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "Archivo no encontrado."

    with open(report_path, 'w') as report:
        report.write("=== Auditoría de Seguridad Linux ===\n\n")

        report.write("Servicios activos:\n")
        report.write(read_file('services.txt') + "\n\n")

        report.write("Puertos abiertos:\n")
        report.write(read_file('ports.txt') + "\n\n")

        report.write("Usuarios con shell:\n")
        report.write(read_file('users.txt') + "\n\n")

        report.write("Archivos con permisos 777:\n")
        report.write(read_file('perms.txt') + "\n\n")

        report.write("Configuración SSH root login:\n")
        report.write(read_file('ssh_root_login.txt') + "\n\n")

        report.write("Estado Firewall (ufw):\n")
        report.write(read_file('firewall.txt') + "\n\n")

    print(f"\n[✓] Reporte generado en {report_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python report_generator.py <ruta_tmp>")
        sys.exit(1)

    generate_report(sys.argv[1])
