duration = int(input('time ?'))
if duration < 60:
    print("{} seconds".format(duration))
elif duration >= 60 and duration < 3600:
    minutes = duration // 60
    sec = duration % 60
    print("{} minutes {} seconds".format(minutes, sec))
elif duration >= 3600 and duration < 86400:
    hours = duration // 3600
    minutes = duration % 3600 // 60
    sec = duration % 3600 % 60
    print("{} hours {} minutes {} seconds".format(hours, minutes, sec))
elif duration >= 86400 and duration < 31536000:
     days = duration // 86400
     hours = duration % 24
     minutes = duration % 3600 // 60
     sec = duration % 3600 % 60
     print("{} days {} hours {} minutes {} seconds".format(days, hours, minutes, sec))
else:
    print('see you next time')