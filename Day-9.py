def exclusiveTime(n, logs):
    result = [0] * n
    stack = []
    prevtime = 0

    for log in logs:
        parts = log.split(":")
        function_id = int(parts[0])
        event_type = parts[1]
        time = int(parts[2])

        if event_type == "start":
            if stack:
                current_function = stack[-1] # peeking at the last element in stack
                result[current_function] += time - prevtime

            stack.append(function_id)
            prevtime = time

        else:  
            finished_function = stack.pop()
            result[finished_function] += time - prevtime + 1 # adding 1 because it is inclusive 
            prevtime = time + 1

    return result

n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
output = exclusiveTime(n,logs)
print(output)

