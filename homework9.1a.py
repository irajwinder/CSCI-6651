def generate_access_config(intf_vlan_mapping, access_template, psecurity=None, port_security_template=None):
    config_list = []
    for interface, vlan in intf_vlan_mapping.items():
        config_list.append(f"interface {interface}")
        for command in access_template:
            if command.endswith("vlan"):
                config_list.append(f"{command} {vlan}")
            else:
                config_list.append(command)
        
        if psecurity and port_security_template:
            config_list.extend(port_security_template)
    
    return config_list


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]
access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

result1 = generate_access_config(access_config, access_mode_template)
result2 = generate_access_config(access_config, access_mode_template, psecurity=True, port_security_template=port_security_template)

print("Configuration without port security:")
for command in result1:
    print(command)

print("\nConfiguration with port security:")
for command in result2:
    print(command)
