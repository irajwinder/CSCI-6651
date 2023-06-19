#Task 7.3
# Open the CAM_table.txt file
with open('CAM_table.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Iterate over each line in the file
for line in lines:
    # Check if the line contains a MAC address
    if '.' in line:
        # Extract the VLAN ID and MAC address from the line
        vlan, mac, _, interface = line.split()

        # Print the VLAN ID, MAC address, and corresponding interface
        print(f"{vlan:<6}{mac:<18}{interface}")
