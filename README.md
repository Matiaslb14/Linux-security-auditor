# Linux Security Auditor - Proyecto 04

Auditoría de seguridad para sistemas Linux que automatiza la recolección y análisis de configuraciones críticas, con generación de reportes completos.

---

## Descripción

Este proyecto consiste en un conjunto de scripts Bash y Python que ejecutan una auditoría integral del sistema Linux, revisando:

- Servicios activos y posibles riesgos asociados  
- Puertos abiertos y en escucha  
- Usuarios con acceso shell  
- Archivos con permisos inseguros (777)  
- Configuración de acceso SSH root  
- Estado del firewall (UFW)  

El resultado es un reporte detallado que permite identificar rápidamente vulnerabilidades y configuraciones inseguras en entornos Linux.

---

## Estructura del proyecto

├── audit.sh # Script principal en Bash que ejecuta la auditoría
├── analyze_service.py # Script Python que analiza servicios inseguros
├── check_permissions.py # Script Python que detecta archivos con permisos 777
├── report_generator.py # Script Python que genera reportes de auditoría
├── final_report.py # (Opcional) Script para consolidar reportes
├── tmp/ # Carpeta con archivos temporales generados durante la auditoría
└── reports/ # Carpeta donde se guardan los reportes finales

## Requisitos

- Linux (preferible Kali Linux u otra distribución para auditoría)  
- Python 3.7+  
- UFW instalado (para chequeo del firewall)  
- Permisos de ejecución para scripts Bash y Python  

Dale permisos de ejecución al script principal:

chmod +x audit.sh

Ejecuta la auditoría:

./audit.sh

Revisa el reporte generado en:

reports/audit_report.txt
