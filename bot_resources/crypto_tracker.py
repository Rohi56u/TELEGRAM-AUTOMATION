# Crypto Price Tracker
import requests
import time

def get_crypto_price(crypto='bitcoin'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd,inr'
    response = requests.get(url)
    data = response.json()
    
    usd_price = data[crypto]['usd']
    inr_price = data[crypto]['inr']
    
    print(f"💰 {crypto.upper()}")
    print(f"   USD: ${usd_price:,.2f}")
    print(f"   INR: ₹{inr_price:,.2f}")
    return usd_price, inr_price

# Track multiple cryptos
cryptos = ['bitcoin', 'ethereum', 'dogecoin']
for crypto in cryptos:
    get_crypto_price(crypto)
    time.sleep(1)
