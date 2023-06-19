#Task 7.1
# Open the ospf.txt file
with open('ospf.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

for line in lines:
    # Split the line into different fields
    fields = line.split()

    # Extract the required information
    prefix = fields[1]
    ad_metric = fields[2]
    next_hop = fields[4]
    last_update = fields[5]
    outbound_interface = fields[6]

    # Print the information in the desired format
    print("Prefix\t\t\t{}".format(prefix))
    print("AD/Metric\t\t{}".format(ad_metric))
    print("Next-Hop\t\t{}".format(next_hop))
    print("Last update\t\t{}".format(last_update))
    print("Outbound Interface\t{}".format(outbound_interface))
    print()  # Print a blank line between entries
