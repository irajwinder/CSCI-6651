mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

result = []
for address in mac:
    cisco_format = address.replace(":", ".")
    result.append(cisco_format)

print(result)
