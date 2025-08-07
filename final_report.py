import os

def read_file(path):
    if not os.path.exists(path):
        return "Archivo no encontrado."
    with open(path, 'r') as f:
        return f.read()

def generate_full_report(tmp_folder, output_file):
    sections = {
        "Servicios activos": "services.txt",
        "Puertos abiertos": "ports.txt",
        "Usuarios con shell": "users.txt",
        "Archivos con permisos 777": "perms.txt",
        "Intentos de login root via SSH": "ssh_root_login.txt",
        "Reglas del Firewall (iptables)": "firewall.txt",
    }

    with open(output_file, 'w') as report:
        report.write("=== Auditoría Completa de Seguridad Linux ===\n\n")
        for title, filename in sections.items():
            report.write(f"--- {title} ---\n")
            content = read_file(os.path.join(tmp_folder, filename))
            report.write(content + "\n\n")

    print(f"[✓] Reporte completo generado en {output_file}")

if __name__ == "__main__":
    tmp_folder = "tmp"
    output_file = "reports/full_audit_report.txt"
    generate_full_report(tmp_folder, output_file)
