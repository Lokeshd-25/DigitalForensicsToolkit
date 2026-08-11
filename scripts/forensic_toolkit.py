import os
import sys
import hashlib
import mimetypes
from datetime import datetime

if len(sys.argv) != 3:
    print("Usage:")
    print("python3 forensic_toolkit.py <evidence_file> <original_hash>")
    sys.exit(1)

filename = sys.argv[1]
original_hash = sys.argv[2]

if not os.path.isfile(filename):
    print("ERROR: Evidence file not found.")
    print("File:", filename)
    sys.exit(1)

file_size = os.path.getsize(filename)
file_type = mimetypes.guess_type(filename)[0]

modified_time = os.path.getmtime(filename)
access_time = os.path.getatime(filename)

with open(filename, "rb") as file:
    data = file.read()

current_hash = hashlib.sha256(data).hexdigest()

text = data.decode("utf-8", errors="ignore")

if current_hash == original_hash:
    integrity_status = "PASS"
else:
    integrity_status = "FAILED"

report = ""

report += "=" * 50 + "\n"
report += "       DIGITAL FORENSICS INVESTIGATION REPORT\n"
report += "=" * 50 + "\n\n"

report += "===== FILE INFORMATION =====\n"
report += f"File: {filename}\n"
report += f"Size: {file_size} bytes\n"
report += f"File Type: {file_type}\n\n"

report += "===== METADATA =====\n"
report += f"Last Modified: {datetime.fromtimestamp(modified_time)}\n"
report += f"Last Accessed: {datetime.fromtimestamp(access_time)}\n\n"

report += "===== INTEGRITY VERIFICATION =====\n"
report += f"Original SHA-256: {original_hash}\n"
report += f"Current SHA-256 : {current_hash}\n"
report += f"Integrity Status: {integrity_status}\n\n"

report += "===== STRING ANALYSIS =====\n"

for line in text.splitlines():
    if line.strip():
        report += line + "\n"

report += "\n" + "=" * 50 + "\n"
report += "           ANALYSIS COMPLETE\n"
report += "=" * 50 + "\n"

print(report)

report_path = "../reports/forensic_report.txt"

with open(report_path, "w") as report_file:
    report_file.write(report)

print("Report saved to:", report_path)
