ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route.replace('O','OSPF')
ospf_route = ospf_route.split()


print(ospf_route)
template = '''
Protocol:           {proto:<20}
Prefix:             {pref:<20} 
AD/Metric:          {dist:<20} 
Next-Hope:          {hop:<20} 
Last update:        {LU:<20} 
Outbound Interface  {OI:<20} 
''' 

print(template.format(proto=ospf_route[0], pref=ospf_route[1], dist=ospf_route[2].strip('[]'), hop=ospf_route[4].strip(","), LU=ospf_route[5].strip(","), OI=ospf_route[6]))
