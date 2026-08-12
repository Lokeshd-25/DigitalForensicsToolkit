import os
import hashlib
import mimetypes
from datetime import datetime


def calculate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()

    return hashlib.sha256(data).hexdigest()


def analyze_metadata(filename):
    file_size = os.path.getsize(filename)
    file_type = mimetypes.guess_type(filename)[0]

    modified_time = os.path.getmtime(filename)
    access_time = os.path.getatime(filename)

    print("\n===== FILE INFORMATION =====")
    print("File:", filename)
    print("Size:", file_size, "bytes")
    print("File Type:", file_type)

    print("\n===== METADATA =====")
    print("Last Modified:", datetime.fromtimestamp(modified_time))
    print("Last Accessed:", datetime.fromtimestamp(access_time))


def analyze_file(filename):
    file_size = os.path.getsize(filename)
    file_type = mimetypes.guess_type(filename)[0]

    print("\n===== FILE ANALYSIS =====")
    print("File:", filename)
    print("Size:", file_size, "bytes")
    print("File Type:", file_type)


def analyze_strings(filename):
    with open(filename, "rb") as file:
        data = file.read()

    text = data.decode("utf-8", errors="ignore")

    print("\n===== STRING ANALYSIS =====")

    for line in text.splitlines():
        if line.strip():
            print(line)


def generate_report(filename, case_id, evidence_id, original_hash=None):

    file_size = os.path.getsize(filename)
    file_type = mimetypes.guess_type(filename)[0]

    modified_time = os.path.getmtime(filename)
    access_time = os.path.getatime(filename)

    current_hash = calculate_hash(filename)

    with open(filename, "rb") as file:
        data = file.read()

    text = data.decode("utf-8", errors="ignore")

    report = ""

    report += "=" * 50 + "\n"
    report += "       DIGITAL FORENSICS INVESTIGATION REPORT\n"
    report += "=" * 50 + "\n\n"

    report += "===== CASE INFORMATION =====\n"
    report += f"Case ID: {case_id}\n"
    report += f"Evidence ID: {evidence_id}\n"
    report += f"Analysis Date: {datetime.now()}\n\n"

    report += "===== FILE INFORMATION =====\n"
    report += f"File: {filename}\n"
    report += f"Size: {file_size} bytes\n"
    report += f"File Type: {file_type}\n\n"

    report += "===== METADATA =====\n"
    report += f"Last Modified: {datetime.fromtimestamp(modified_time)}\n"
    report += f"Last Accessed: {datetime.fromtimestamp(access_time)}\n\n"

    report += "===== SHA-256 =====\n"
    report += f"Current SHA-256: {current_hash}\n\n"

    if original_hash:

        report += "===== INTEGRITY VERIFICATION =====\n"
        report += f"Original SHA-256: {original_hash}\n"
        report += f"Current SHA-256 : {current_hash}\n"

        if current_hash == original_hash:
            report += "Integrity Status: PASS\n"
        else:
            report += "Integrity Status: FAILED\n"

        report += "\n"

    report += "===== STRING ANALYSIS =====\n"

    for line in text.splitlines():
        if line.strip():
            report += line + "\n"

    report += "\n" + "=" * 50 + "\n"
    report += "           ANALYSIS COMPLETE\n"
    report += "=" * 50 + "\n"

    report_path = "../reports/forensic_report.txt"

    with open(report_path, "w") as report_file:
        report_file.write(report)

    print("\n" + report)
    print("\nReport saved to:", report_path)


def main():

    print("\n" + "=" * 40)
    print("      DIGITAL FORENSICS TOOLKIT")
    print("=" * 40)

    case_id = input("\nEnter Case ID: ")
    evidence_id = input("Enter Evidence ID: ")

    while True:

        print("\n" + "=" * 40)
        print("      DIGITAL FORENSICS TOOLKIT")
        print("=" * 40)

        print("\n1. Calculate SHA-256")
        print("2. Verify Evidence Integrity")
        print("3. Analyze File Metadata")
        print("4. Analyze File Type")
        print("5. String Analysis")
        print("6. Generate Forensic Report")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "7":
            print("\nExiting toolkit...")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\nInvalid choice. Please try again.")
            continue

        filename = input("\nEnter evidence file path: ")

        if not os.path.isfile(filename):
            print("\nERROR: Evidence file not found.")
            continue

        if choice == "1":

            hash_value = calculate_hash(filename)

            print("\n===== SHA-256 HASH =====")
            print(hash_value)

        elif choice == "2":

            original_hash = input("\nEnter original SHA-256 hash: ")

            current_hash = calculate_hash(filename)

            print("\n===== INTEGRITY VERIFICATION =====")
            print("Original SHA-256:", original_hash)
            print("Current SHA-256 :", current_hash)

            if current_hash == original_hash:
                print("Integrity Status: PASS")
            else:
                print("Integrity Status: FAILED")

        elif choice == "3":

            analyze_metadata(filename)

        elif choice == "4":

            analyze_file(filename)

        elif choice == "5":

            analyze_strings(filename)

        elif choice == "6":

            original_hash = input(
                "\nEnter original SHA-256 hash (press Enter to skip): "
            )

            if original_hash.strip() == "":
                original_hash = None

            generate_report(
                filename,
                case_id,
                evidence_id,
                original_hash
            )


if __name__ == "__main__":
    main()
