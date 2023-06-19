command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

# Extract VLAN numbers from command1
vlan1 = set(command1.split()[-1].split(','))

# Extract VLAN numbers from command2
vlan2 = set(command2.split()[-1].split(','))

# Find the intersection of VLANs
result = list(vlan1.intersection(vlan2))

# Print the result
print(result)