import re
from itertools import zip_longest

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

    remote_address = re.compile(r'^\d+(?:[.]\d+){3}|\w+(?:[:]\w*){5,}', re.M)
    request_datetime = re.compile(r'\d{2}[/]\w+[/]\d{4}(?::\d{2}){3} \+\d{4}')
    request_type = re.compile(r'"([A-Z]+\b)')
    requested_resource = re.compile(r'(?:/[a-z]+){2}_\d')
    response_code = re.compile(r'(?<=" )(\d{3}\b)')
    response_size = re.compile(r'\b\d+(?= ")')

    remote_address = remote_address.findall(txt)
    request_datetime = request_datetime.findall(txt)
    request_type = request_type.findall(txt)
    requested_resource = requested_resource.findall(txt)
    response_code = response_code.findall(txt)
    response_size = response_size.findall(txt)
    parsed_file = zip_longest(remote_address, request_datetime, request_type, requested_resource, response_code,
                              response_size, fillvalue=None)
    print(*parsed_file, sep='\n')