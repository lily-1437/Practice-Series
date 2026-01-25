from collections import deque

def timeRequiredToBuy(tickets, k):
    queue = deque(range(len(tickets)))  # store indices
    time = 0

    while True:
        person = queue.popleft()
        tickets[person] -= 1
        time += 1

        if tickets[person] == 0:
            if person == k:
                return time
        else:
            queue.append(person)


tickets = [2, 3, 2]
k = 2
output = timeRequiredToBuy(tickets, k)
print(output)
