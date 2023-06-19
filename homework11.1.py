def parse_cdp_neighbors(command_output):
    output = {}
    for line in command_output.split("\n"):
        line = line.strip()
        columns = line.split()
        #print(line)
        if ">" in line:
            hostname = line.split(">")[0]
        elif len(columns) >= 5 and columns[1]=='Eth':

            #print(columns)
            host = columns[0]
            localeth = columns[1]
            interfacenumber = columns[2]
            other = columns[3:-2]
            platform = columns[-2]
            porteth = columns[-1]
            #print(host,)

            key = (hostname, localeth + interfacenumber)
            print(type(key))
            value = (host, platform + porteth)
            output[key] = value

    return output


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        g=parse_cdp_neighbors(f.read())
        for key, value in g.items():
            print(f"{key} : {value}")