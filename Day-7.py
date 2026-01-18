def buildArray(target, n):
    result = []
    item = 0
    for pointer in range (1,n+1):
        result.append("Push")
        if pointer == target[item]:
            item +=1
            if item == len(target):
                break
        else:
            result.append("Pop")
    return result

target = [2,3,4]
n = 4
output = buildArray(target,n)
print(output)