# import requests

# url = "https://rest.coinapi.io/" 
# api_key = "3F69B3CB-B2C2-4B1A-B175-BBF449C1938D"

# params = {"key": api_key}
# headers = {
#     "Accept": "application/json",
#     "Accept-Encoding": "deflate, gzip"
# }


# response = requests.get(url, headers=headers, params=params)


# if response.status_code == 200:  
#     data = response.json()  

#     print(data)
# else:
#     print("Request failed with status code:", response)
import requests

async def get_bitcoin_trader():
    import requests
    url = 'https://rest.coinapi.io/v1/trades/latest'
    headers = {'X-CoinAPI-Key' : '3F69B3CB-B2C2-4B1A-B175-BBF449C1938D'}
    response = requests.get(url, headers=headers)

    return response.json()
