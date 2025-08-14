# 🛡️ Linux Security Auditor
Security auditing tool for Linux systems that automates the collection and analysis of critical configurations, generating comprehensive reports.

📌 Description

This project is a set of Bash and Python scripts that perform a complete security audit on Linux systems, checking:

Active services and potential security risks

Open and listening ports

Users with shell access

Files with insecure permissions (777)

SSH root access configuration

Firewall (UFW) status

The result is a detailed report that allows quick identification of vulnerabilities and insecure configurations in Linux environments.

📂 Project Structure

├── audit.sh               # Main Bash script that runs the audit  

├── analyze_service.py     # Python script to analyze insecure services  

├── check_permissions.py   # Python script to detect files with 777 permissions  

├── report_generator.py    # Python script to generate audit reports  

├── final_report.py        # (Optional) Script to consolidate reports  

├── tmp/                   # Temporary files generated during the audit  

└── reports/               # Final reports are stored here  

⚙️ Requirements

Linux (Kali Linux or other security-focused distribution recommended)

Python 3.7+

UFW installed (for firewall check)

Execution permissions for Bash and Python scripts

▶️ Usage

Grant execution permissions to the main script:

chmod +x audit.sh

Run the audit:

./audit.sh

Check the generated report in:

reports/audit_report.txt
