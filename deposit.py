from utils import balance, transaction
import datetime as dt

def deposit(amount):
    global balance
    balance[0] += amount
    transaction[dt.datetime.now()] = f'+{amount}'
    print(f'Amount deposited successfully. Current balance: {balance}')
