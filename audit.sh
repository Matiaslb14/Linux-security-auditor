#!/bin/bash

# Colores para mejor visual en consola
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

echo -e "${GREEN}Iniciando Auditoría de Seguridad Linux...${NC}"

# Crear carpeta temporal para outputs
TMPDIR="./tmp"
mkdir -p "$TMPDIR"

echo -e "${GREEN}Obteniendo lista de servicios activos...${NC}"
systemctl list-units --type=service --state=running > "$TMPDIR/services.txt"

echo -e "${GREEN}Detectando puertos abiertos...${NC}"
ss -tuln > "$TMPDIR/ports.txt"

echo -e "${GREEN}Listando usuarios con shell...${NC}"
grep -E '/bin/bash|/bin/sh' /etc/passwd > "$TMPDIR/users.txt"

echo -e "${GREEN}Buscando archivos con permisos 777...${NC}"
find / -perm 0777 -type f 2>/dev/null > "$TMPDIR/perms.txt"

echo -e "${GREEN}Chequeando configuración SSH root login...${NC}"
grep PermitRootLogin /etc/ssh/sshd_config > "$TMPDIR/ssh_root_login.txt"

echo -e "${GREEN}Estado del firewall (ufw)...${NC}"
ufw status > "$TMPDIR/firewall.txt" 2>&1

echo -e "${GREEN}Ejecutando análisis Python...${NC}"
python3 analyze_service.py "$TMPDIR/services.txt"
python3 check_permissions.py "$TMPDIR/perms.txt"
python3 report_generator.py "$TMPDIR"

echo -e "${GREEN}Auditoría completada. Revisa el reporte en reports/ \n${NC}"
