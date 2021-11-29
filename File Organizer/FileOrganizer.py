# Programmed by - Abdullah Tanveer
# date - August 12-2021
# Automation Script for organizing files automatically according file type 
import os
import collections

# get destination path, where files will be moved
# dest_path = input("Enter Destination Path -> ").replace("\\", "\\\\")

# get user downloads folder path
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

file_mappings = collection.defaultdict()
for filename in os.listdir(downloads_path):
    # extract files extension
    file_type = filename.split('.')[-1].upper()
    file_mappings.setdefault(file_type, []).append(filename)

