def solution(people, limit):
    boat = 0
    light = 0
    heavy = len(people)-1
    people.sort()
    while (light <= heavy):
        if (people[light] + people[heavy] <= limit):
            light += 1
        heavy -= 1
        boat += 1

    return boat