
def valid_bracket(str):
    stack = []
    dict = {
        "}": "{",
        ")": "(",
        "]": "]"
	}
    for char in str:
        if len(str) or char in "[({" == 0:
            stack.append(char)
        else:
			# all closing brackets here
            openChar = dict[char] if char in dict else None
            if len(stack)> 0 and stack[-1] == openChar:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True

res = valid_bracket("[)][][](){}")
print(f'result is: {res}')
