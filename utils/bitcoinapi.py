import requests

async def get_bitcoin_trader():
    import requests
    url = 'https://rest.coinapi.io/v1/trades/latest'
    headers = {'X-CoinAPI-Key' : '3F69B3CB-B2C2-4B1A-B175-BBF449C1938D'}
    response = requests.get(url, headers=headers)

    return response.json()