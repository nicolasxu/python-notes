

numbers = range(1, 500) # iterable
the_list = list(numbers) # takes an iterable and make an list
# print(the_list)



#
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


odd_number = filter(is_odd, numbers) # return is filter object, iterable
# you need to pass it to a list constructor
print(list(odd_number))