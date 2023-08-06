

input_str = "hannah"

def is_palindrome(str=""):
    size = len(str)
    if size <= 1:
        return True

    for i, char in enumerate(str):
        if char!=str[size -i -1]:
            return False

    return True

def is_palindrome2(str=""):
    size = len(str)
    if size <=1:
        return True

    for i in range(size//2):
        if (str[i] != str[size -i -1]):
            return False

    return True


res = is_palindrome2(input_str )
print("is_palindrome:", res)
