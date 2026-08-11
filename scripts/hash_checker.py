import hashlib
import sys

filename = sys.argv[1]
original_hash = sys.argv[2]

with open(filename, "rb") as file:
    data = file.read()

current_hash = hashlib.sha256(data).hexdigest()

print("File:", filename)
print("Original SHA-256:", original_hash)
print("Current SHA-256 :", current_hash)

if current_hash == original_hash:
    print("INTEGRITY STATUS: PASS")
else:
    print("INTEGRITY STATUS: FAILED")
