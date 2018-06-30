# Loops

people = ['John', 'Sara', 'Tim', 'Bob']

for person in people:
    print('Current person ' + person)

for i in range(len(people)):
    print('Current person ' + people[i])

for i in range(0, 10):
    print(i)

count = 0
while count <= 10:
    print('Count ', count)
    if count == 5:
        break
    count += 1




