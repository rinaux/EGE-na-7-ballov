def bin_ip(ip):
    return '.'.join([bin(x)[2:].zfill(8) for x in map(int, ip.split('.'))])

print(bin_ip('255.255.255.192'))
