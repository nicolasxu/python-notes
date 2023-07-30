



balance = 333

while True:
    try:
        deposit = float(input("enter deposit: "))
        break
    except ValueError:
        print(f'Please enter valid amount')
balance += deposit
print(f'Total balance is {balance}')