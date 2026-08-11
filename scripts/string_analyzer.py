import sys

filename = sys.argv[1]

with open(filename, "rb") as file:
    data = file.read()

print("===== STRING ANALYSIS =====")

text = data.decode("utf-8", errors="ignore")

for line in text.splitlines():
    if line.strip():
        print(line)
