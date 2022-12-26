def make_readable(seconds):
    hours = 0
    minutes = 0

    for i in range(1, int(seconds)+1):
        # print('i', i)
        seconds = seconds%60
        if i%60 == 0:
            minutes += 1
            # seconds = 0
            # print('m', minutes)
            if minutes%60 == 0:
                minutes = 0
                # seconds = 0
                hours += 1

    # print('h', hours, 'm', minutes, 's', seconds)
    result = '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)
    # print(result)


    return result

# print(make_readable(0))         #"00:00:00"
# print(make_readable(5))          #"00:00:05")
# print(make_readable(60))        #"00:01:00")
# print(make_readable(86399))     #"23:59:59"
print(make_readable(359999))    #"99:59:59"