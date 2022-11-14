"""
5 1
10 9 8 7 3 7 5 5 0 0 12 11 9 8 7 7 7 5 5 11 44 41 8
"""
chart = []
while True:
    try:
        line = input()
    except EOFError:
        break
    chart.append(line)

firstRaw = chart[0].split()
secondRaw = chart[-1].split()

all_participants = int(firstRaw[0])
participant = int(firstRaw[-1])
participantScore = int(secondRaw[participant-1])

# print('Participant #', participant, 'earns', participantScore, 'points')

flag = 0
# print('Number of all participants',all_participants)

for i in range(all_participants):
    value = int(secondRaw[i])
    if value >= participantScore and value > 0:
        flag += 1

print(flag)
