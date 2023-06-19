# Open the CAM_table.txt file
with open('CAM_table.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Create a list to store the parsed entries
entries = []

# Iterate over each line in the file
for line in lines:
    # Check if the line contains a MAC address
    if '.' in line:
        # Extract the VLAN ID, MAC address, and interface from the line
        vlan, mac, _, interface = line.split()

        # Convert the VLAN ID to an integer
        vlan = int(vlan)

        # Append the parsed entry to the list
        entries.append((vlan, mac, interface))

# Sort the entries by VLAN number
entries.sort()

# Print the sorted entries
for entry in entries:
    vlan, mac, interface = entry
    print(f"{vlan:<6}{mac:<18}{interface}")
