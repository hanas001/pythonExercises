def likes(names):
    ln = len(names)
    if ln == 0:
        answer = 'no one likes this'
    elif ln == 1:
        answer = str(names[0]) + ' likes this'
    elif ln == 2:
        answer = str(names[0]) + ' and ' + str(names[1]) + ' like this'
    elif ln == 3:
        answer = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like this'
    elif ln >= 4:
        answer = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(ln - 2) + ' others like this'

    return answer

# print(likes([]))    #'no one likes this'
# print(likes(['Peter'])) #'Peter likes this'
# print(likes(['Jacob', 'Alex'])) #'Jacob and Alex like this'
# print(likes(['Max', 'John', 'Mark']))   #'Max, John and Mark like this'
# print(likes(['Alex', 'Jacob', 'Mark', 'Max'])) #'Alex, Jacob and 2 others like this'
print(likes(['Nene Romanova', 'Nigel', 'Quincy Rosenkreutz', 'Macky Stingray', 'Anri', 'Galatea', 'Priscilla S. Asagiri', 'Linna Yamazaki', 'Largo', 'Leon McNichol']))