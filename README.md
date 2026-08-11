# Digital Forensics Investigation & Evidence Integrity Toolkit

## Overview

A Python-based digital forensics toolkit developed in Kali Linux for analyzing digital evidence, verifying evidence integrity, extracting file metadata, performing basic string analysis, and generating forensic investigation reports.

## Objectives

- Calculate SHA-256 hashes for digital evidence
- Verify evidence integrity
- Detect modifications to evidence files
- Extract basic file metadata
- Identify file types
- Perform basic string analysis
- Generate automated forensic reports
- Handle invalid files and incorrect input safely

## Features

### 1. SHA-256 Hashing
Calculates the SHA-256 hash of an evidence file to create a unique digital fingerprint.

### 2. Integrity Verification
Compares the original evidence hash with the current hash.

- Matching hashes → PASS
- Different hashes → FAILED

### 3. Metadata Analysis
Extracts:

- File size
- Last modified time
- Last accessed time
- File type

### 4. String Analysis
Extracts readable text from evidence files for basic forensic investigation.

### 5. Automated Reporting
Generates a forensic investigation report containing the analysis results.

### 6. Error Handling
Handles:

- Missing arguments
- Missing evidence files
- Invalid input

## Project Structure

```text
DigitalForensicsToolkit/
│
├── evidence/
│   ├── suspicious_document.txt
│   ├── unchanged_copy.txt
│   └── altered_copy.txt
│
├── scripts/
│   ├── forensic_toolkit.py
│   ├── hash_checker.py
│   ├── metadata_analyzer.py
│   ├── file_analyzer.py
│   └── string_analyzer.py
│
├── reports/
│   └── forensic_report.txt
│
└── README.md
