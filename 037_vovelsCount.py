def get_count(sentence):
    counter = 0
    vowels = 'aeiou'
    for i in sentence:
        if i in vowels:
            counter +=1
    return counter


print(get_count('aeiou'))
print(get_count('bcdfghjklmnpqrstvwxz y'))
print(get_count(''))
print(get_count('abracadabra'))