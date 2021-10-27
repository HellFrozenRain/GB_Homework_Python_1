import re

def email_parse(email):
    my_dict = {'username':'', 'domain':''}
    pattern = re.compile(r'([a-z0-9-_\.]+)@([a-z0-9]+\.[a-z]+)', re.IGNORECASE)
    check_list = pattern.findall(email)
    if check_list:
        name, domain = check_list[0]
        my_dict['username'] = name
        my_dict['domain'] = domain

    else:
        raise ValueError (f'wrong email: {email}')
    return my_dict


my_mail = input('enter mail')
print(email_parse(my_mail))


