

input_str = "hannah"

def is_palindrome(str=""):
    size = len(str)
    if size <= 1:
        return True

    for i, char in enumerate(str):
        if char!=str[size -i -1]:
            return False

    return True


res = is_palindrome(input_str + "1")
print("is_palindrome:", res)
