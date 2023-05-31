from faker import Faker
import random
import pandas as pd
fake = Faker()


def generate_accounts(n):
    data = []

    for _ in range(n):
        account_number = fake.ean(8)
        balance = round(random.uniform(0, 200000), 2)
        data.append({
            'accountNumber': account_number,
            'balance': balance
        })

    return pd.DataFrame(data).drop_duplicates(subset=['accountNumber'])


def generate_transactions(n, accounts):
    data = []
    i = 0

    while i < n:
        transfer_amount = round(random.uniform(50, 25000), 2)
        from_account_number = accounts.sample(1).accountNumber.iloc[0]
        to_account_number = accounts.sample(1).accountNumber.iloc[0]

        if from_account_number != to_account_number:
            data.append({
                'fromAccountNumber': from_account_number,
                'toAccountNumber': to_account_number,
                'transferAmount': transfer_amount
            })
            i += 1

            # if transfer_amount > accounts.loc[accounts.accountNumber == from_account_number].balance.iloc[0]:
            #    print('INVALID')

    return pd.DataFrame(data)


if __name__ == '__main__':
    accounts = generate_accounts(450000)
    transactions = generate_transactions(100000, accounts)
    accounts.to_csv('accounts.csv', index=False)
    transactions.to_csv('transactions.csv', index=False)
