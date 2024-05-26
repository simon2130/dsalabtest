def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    result = ''
    while len(stack) > 0:
        result += stack.pop()
    return result
print (reverse_string("helloworld!"))