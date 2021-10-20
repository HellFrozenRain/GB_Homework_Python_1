with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        ip_address = line.split()[0]
        my_dict.setdefault(ip_address, 0)
        my_dict[ip_address] = my_dict[ip_address] + 1


my_dict_reversed = {v: k for k, v in my_dict.items()}
number = max(my_dict_reversed)
spammer_ip = my_dict_reversed[number]
print(f"The spammer's IP address: {spammer_ip}")
print(f"The number of requests sent to him: {number}")