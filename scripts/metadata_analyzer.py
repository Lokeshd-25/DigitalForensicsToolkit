import os
import sys
from datetime import datetime

filename = sys.argv[1]

file_size = os.path.getsize(filename)
modified_time = os.path.getmtime(filename)
access_time = os.path.getatime(filename)

print("===== FILE METADATA =====")
print("File:", filename)
print("Size:", file_size, "bytes")
print("Last Modified:", datetime.fromtimestamp(modified_time))
print("Last Accessed:", datetime.fromtimestamp(access_time))
