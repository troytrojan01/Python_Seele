import requests

request = requests.get('https://api.seelescan.net/api/v1/account?address=YOUR_ADDRESS')
results = request.json()

address = results['data'] ['address']
balance = results['data'] ['balance']
shardnumber = results['data'] ['shardnumber']
txcount = results['data'] ['txcount']

balance_string = '{:}'.format(balance)[:6]
txcount_string = '{:,}'.format(txcount)

print('My current balance is ' + balance_string + ' with ' + txcount_string + ' transactions.')
