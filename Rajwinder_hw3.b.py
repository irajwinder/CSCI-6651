while True:
    ip_address = input("Enter an IP address (e.g., 10.0.1.1): ")
    
    # Split the IP address into octets
    octets = ip_address.split(".")
    
    # Check if the IP address has exactly 4 octets
    if len(octets) != 4:
        print("Invalid IP address")
        continue
    
    # Check if all octets are valid integers in the range from 0 to 255
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            print("Invalid IP address")
            break
    else:
        # Convert octets to integers
        first_octet = int(octets[0])
        
        # Determine the type of IP address
        if ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        elif 1 <= first_octet <= 126:
            print("unicast class A")
        elif 128 <= first_octet <= 191:
            print("unicast class B")
        elif 192 <= first_octet <= 223:
            print("unicast class C")
        elif 224 <= first_octet <= 239:
            print("multicast")
        else:
            print("unused")
        break