command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
list1 = list(command1[command1.find('1'):].replace(',',''))
list2 = list(command2[command2.find('1'):].replace(',',''))
list3 = set(list1) & set(list2)
print(list(list3))
