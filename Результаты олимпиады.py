class Participant:
    a = ''
    points = 0


b = int(input())

participants = []

for i in range(b):
    c = list(input().split())
    p = Participant()
    p.secondName = c[0]
    p.points = int(c[1])
    participants.append(p)

participants.sort(key=lambda part: -part.points)

for p in participants:
    print(p.a)
