def print_network_details(ip_networks):
    network, mask = ip_networks.split('/')
    octets = network.split('.')
    mask = int(mask)

    # Validate IP network format
    if len(octets) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in octets):
        print("Invalid IP network format")
        return

    # Print Network
    print("Network:")
    print(' '.join(f'{int(part):<10}' for part in octets))
    print(' '.join(f'{int(part):08b}' for part in octets))
    print()

    # Print Mask
    binary_mask = "1" * mask + "0" * (32 - mask)
    print("Mask:")
    print(f"/{mask}")
    print(' '.join(f'{int(binary_mask[i:i+8], 2):<10}' for i in range(0, 32, 8)))
    print(' '.join(binary_mask[i:i+8] for i in range(0, 32, 8)))


ip_network = input("Enter the IP network (e.g., 10.1.1.0/24): ")
print_network_details(ip_network)