list_input= ["192.168.43.54 / 255.255.254.0", "192.168.43.54 / 255.255.255.240"]

dct = dict()



def raw_data(input):
    s = input.split('/')
    addr_lst =[int(i) for i in s[0].split(".")]
    mask_lst = [int(i) for i in s[1].split(".")]

    return addr_lst, mask_lst




def search(address, mask,id):
    bm = [255, 255, 255, 255]
    network = [address[i]&mask[i] for i in range(len(mask))]  
    broadcast = [network[i]+(bm[i]-mask[i]) for i in range(len(mask))]
    network_s = [str(address[i]&mask[i]) for i in range(len(mask))] 
    broadcast_s = [str(network[i]+(bm[i]-mask[i])) for i in range(len(mask))]
    host_min = [str(network[i]) if i != 3 else str(network[i]+1) for i in range(len(mask))]
    host_max = [str(broadcast[i]) if i != 3 else str(broadcast[i]-1) for i in range(len(mask))]
    wildcard = [str((bm[i]-mask[i])) for i in range(len(mask))]


    

    dct[f'network-{id}'] = '.'.join(network_s)
    dct[f'broadcast-{id}'] = '.'.join(broadcast_s)
    dct[f'host_min-{id}'] = '.'.join(host_min)
    dct[f'host_max-{id}'] = '.'.join(host_max)
    dct[f'wildcard-{id}'] = '.'.join(wildcard)
    return dct

    

id = 1    
    
for i in list_input:
    addr_lst, mask_lst = raw_data(i)
    search(addr_lst, mask_lst, id)
    id += 1


print(dct)