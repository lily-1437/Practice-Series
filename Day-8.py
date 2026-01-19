# Reverse Polish Notation
def evalRPN(tokens):
    empty_list = []
    for i in tokens:
        if(i in { "+","-","*","/"}):
            value1 = empty_list.pop()
            value2 = empty_list.pop()
            if (i == "+"):
                empty_list.append(value1 + value2)
            if (i == "-"):
                empty_list.append(value2 - value1)
            if (i == "*"):
               empty_list.append(value1 * value2)
            if (i == "/"):
               empty_list.append(int(value2/value1))
        else: 
            empty_list.append(int(i))
    return empty_list[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output = evalRPN(tokens)
print(output)