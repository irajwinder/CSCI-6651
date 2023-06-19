def generate_access_config(intf_vlan_mapping, access_template):
    config_list = []  # Create an empty list to store the configuration commands
    for intf, vlan in intf_vlan_mapping.items():  # Iterate over the interface-VLAN mapping dictionary
        config_list.append(f"interface {intf}")  # Add the interface command to the configuration list
        for command in access_template:  # Iterate over each command in the access template
            if command.endswith('access vlan'):  # Check if the command is for setting the VLAN
                config_list.append(f"{command} {vlan}")  # Add the VLAN number to the command and append to the list
            else:
                config_list.append(command)  # Add the command as it is to the configuration list
    return config_list  # Return the list of configuration commands


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

result = generate_access_config(access_config, access_mode_template)
for command in result:
    print(command)

access_config_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107
}

result = generate_access_config(access_config_2, access_mode_template)
for command in result:
    print(command)
