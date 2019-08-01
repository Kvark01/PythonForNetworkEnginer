mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':','')
mac = int(mac,16)

print('{:b}'.format(mac))
