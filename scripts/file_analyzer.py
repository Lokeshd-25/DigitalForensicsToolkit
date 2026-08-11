import os
import sys
import mimetypes

filename=sys.argv[1]
file_size=os.path.getsize(filename)
file_type=mimetypes.guess_type(filename)[0]
print("==== FILE ANALYSIS ====")
print("FILE:",filename)
print("Size:",file_size,"bytes")
print("FILE Type:",file_type)
