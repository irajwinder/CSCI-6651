#Task HW4:
import sys

# Check if the filename argument is provided
if len(sys.argv) < 2:
    print("Please specify file name as: python homework.py config_sw1.txt")
    sys.exit(1)

filename = sys.argv[1]

# Open the file and read its contents
with open(filename, 'r') as file:
    # Read each line and process it
    for line in file:
        # Strip whitespace characters from the beginning and end of the line
        line = line.strip()
        
        # Exclude lines that start with '!'
        if not line.startswith('!') and line != "":
            print(line)

#Task HW4a:
print("\nTask HW4a: ")
# Check if the filename argument is provided
if len(sys.argv) < 3:
    print("Please specify file name as: python homework.py config_sw1.txt filtered_config_sw1.txt")
    sys.exit(1)

filename = sys.argv[1]

ignore = ["duplex", "alias", "configuration"]

# Open the file and read its contents
with open(filename, 'r') as file:
    # Read each line and process it
    for line in file:
        # Strip whitespace characters from the beginning and end of the line
        line = line.strip()
        
        # Exclude lines that start with '!'
        if line.startswith('!') or line == "":
            continue
        
        # Exclude lines that contain words from the ignore list
        if any(word in line for word in ignore):
            continue
        
        print(line)

#Task HW4b:
print("\nTask HW4b: ")
destination_filename = sys.argv[2]

ignore = ["duplex", "alias", "configuration"]

# Open the source file for reading
with open(filename, 'r') as source_file:
    # Read the source file contents
    lines = source_file.readlines()

# Open the destination file for writing
with open(destination_filename, 'w') as destination_file:
    # Process each line from the source file
    for line in lines:
        # Strip whitespace characters from the beginning and end of the line
        line = line.strip()
        
        # Exclude lines that start with '!'
        if line.startswith('!') or line == "":
            continue
        
        # Exclude lines that contain words from the ignore list
        if any(word in line for word in ignore):
            continue
        
        # Write the filtered line to the destination file
        destination_file.write(line + '\n')