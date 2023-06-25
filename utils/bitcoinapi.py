import requests
from decouple import config

async def get_bitcoin_trader():
    import requests
    url = 'https://rest.coinapi.io/v1/trades/latest'
    headers = {'X-CoinAPI-Key' : config('BITCOIN_KEY')}
    response = requests.get(url, headers=headers)

    return response.json()