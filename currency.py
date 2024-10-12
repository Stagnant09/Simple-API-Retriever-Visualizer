"""
This Python script retrieves data from https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}
and modifies index.html accordingly to display the current prices.
"""

import requests
import json

date = 'latest'
apiVersion = 'v1'
endpoint = 'currencies/eur.json'

# Create the request
url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}'

# Send the request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Extract the exchange rates
    exchange_rates = data['eur']
    # Modify the index.html file
    with open('index.html', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if '<div id="root">' in line:
                # Clear the line
                lines[i+4] = ''
                for j in range(0, len(exchange_rates)):
                    currency = list(exchange_rates.keys())[j]
                    rate = list(exchange_rates.values())[j]
                    lines[i+4] += f'<tr><td>{currency}</td><td>{rate}</td></tr>'
                break
    with open('index.html', 'w') as f:
        f.writelines(lines)
    print('Exchange rates updated successfully!')
else:
    print(f'Error: {response.status_code}')
