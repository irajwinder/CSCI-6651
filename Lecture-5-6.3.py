trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan_list in trunk.items():
    print("interface FastEthernet " + intf)
    for command in trunk_template:
        if command.endswith("trunk allowed vlan"):
            action = vlan_list[0]
            vlans = ",".join(vlan_list[1:])
            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
        else:
            print(f" {command}")
    print()
    
