# Task 1 Многострочный текст

## Task1.1: Переменная определелена глобально

config = """

#
bridge-domain 555
 vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
 vxlan vni 10555
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target 64512:10555 export-extcommunity
  vpn-target 64512:10555 import-extcommunity
 arp broadcast-suppress enable
#
 
"""

## Task1.2: Переменная определена внутри блока

from textwrap import dedent

if True:
    config = dedent("""

    #
    bridge-domain 555
     vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
     vxlan vni 10555
     #
     evpn
      route-distinguisher 192.168.43.34:10555
      vpn-target 64512:10555 export-extcommunity
      vpn-target 64512:10555 import-extcommunity
     arp broadcast-suppress enable
    #
 
    """)

print(config)

### Task2: Преобразовании числа в строку

bd_id = 555

bd_id_str1 = str(bd_id)
bd_id_str2 = '{0}'.format(bd_id)
bd_id_str3 = f"{bd_id}"

# Task3: Работа с байтовой последовательностью

## Task3.1: Преобразование в utf-8

output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"


s = output.decode('UTF8')

## Task3.2: Возврат каретки (CR)

s1 = s.replace("\n", "")

## Task3.3: Пробельные символы

s2 = s1.lstrip()


# Task4: Форматирование строк

## Task4.1: Простейший шаблон

bd_id = '555'
intf_start =  '10GE1/0/1'
intf_end = '10GE1/0/48'
rid = '192.168.43.34'
bgp_as = '64512'
rd = '1'+bd_id.zfill(4)


template = dedent(f'''

#
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni {rd}
 #
 evpn
  route-distinguisher {rid}:{rd}
  vpn-target {bgp_as}:{rd} export-extcommunity
  vpn-target {bgp_as}:{rd} import-extcommunity
 arp broadcast-suppress enable
#
''')

bd_id = '2541'
intf_start =  '10GE1/0/1'
intf_end = '10GE1/0/48'
rid = '192.168.43.34'
bgp_as = '64512'
rd = '1'+bd_id.zfill(4)


template1 = dedent(f'''

#
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni {rd}
 #
 evpn
  route-distinguisher {rid}:{rd}
  vpn-target {bgp_as}:{rd} export-extcommunity
  vpn-target {bgp_as}:{rd} import-extcommunity
 arp broadcast-suppress enable
#
''')

bd_id = '84'
intf_start =  '10GE1/0/1'
intf_end = '10GE1/0/48'
rid = '192.168.43.34'
bgp_as = '64512'
rd = '1'+bd_id.zfill(4)


template2 = dedent(f'''

#
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni {rd}
 #
 evpn
  route-distinguisher {rid}:{rd}
  vpn-target {bgp_as}:{rd} export-extcommunity
  vpn-target {bgp_as}:{rd} import-extcommunity
 arp broadcast-suppress enable
#
''')



## Task4.2: Преобразование в двоичную систему - 1


format(42, 'b')

format(32, 'b')

format(255, 'b')


## Task4.3: Преобразование в двоичную систему - 2


format(42, 'b').zfill(8)

format(32, 'b')

format(255, 'b')


## Task4.4: Преобразование в двоичную систему - 3

ip = "10.23.43.234"

ip_bin = ''.join([format(int(o), 'b').zfill(8) for o in ip.split('.')])


## Task4.5: RTP запись

ip = "77.88.55.242"


s = ip[::-1] + '.in-addr.arpa'


## Task4.5: Доработка задания по числам


s = input('Введите адрес и маску в формате ip/mask: ') # ["192.168.43.54 / 255.255.254.0", "192.168.43.54 / 255.255.255.240"]

dct = dict()



def raw_data(input):
    s = input.split('/')
    addr_lst =[int(i) for i in s[0].split(".")]
    mask_lst = [int(i) for i in s[1].split(".")]

    return addr_lst, mask_lst




def search(address, mask):
    bm = [255, 255, 255, 255]
    network = [address[i]&mask[i] for i in range(len(mask))]  
    broadcast = [network[i]+(bm[i]-mask[i]) for i in range(len(mask))]
    network_s = [str(address[i]&mask[i]) for i in range(len(mask))] 
    broadcast_s = [str(network[i]+(bm[i]-mask[i])) for i in range(len(mask))]
    host_min = [str(network[i]) if i != 3 else str(network[i]+1) for i in range(len(mask))]
    host_max = [str(broadcast[i]) if i != 3 else str(broadcast[i]-1) for i in range(len(mask))]
    wildcard = [str((bm[i]-mask[i])) for i in range(len(mask))]


    

    dct[f'network'] = '.'.join(network_s)
    dct[f'broadcast'] = '.'.join(broadcast_s)
    dct[f'host_min'] = '.'.join(host_min)
    dct[f'host_max'] = '.'.join(host_max)
    dct[f'wildcard'] = '.'.join(wildcard)
    return dct

     
    
addr_lst, mask_lst = raw_data(s)
search(addr_lst, mask_lst)




print(dct)



## Task4.6: Удаление символов в строке


output = """
Local Interface         Exptime(s) Neighbor Interface            Neighbor Device
-------------------------------------------------------------------------------------
100GE1/0/1                    107  100GE1/0/1                    spine1.pod1.stg
10GE1/0/1                     105  10GE1/0/1                     test-server.stg
""".strip()

istart = output.find('\n')
iend = output.find('100')
s = output[istart+1:iend]
s1 = output.replace(s, '')


## Task4.7: Нормализация имен интерфейсов

if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Тen4/3"

if_name1 = if_name1.replace('Eth', 'Ethernet')
if_name2 = if_name2.replace('GE', 'GigabitEthernet')
if_name3 = if_name3.replace('Ten', 'TenGigabitEthernet')