config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(config[config.find('1')::])
