import requests

TROY_OZ_TO_GRAMS = 31.1034768
gp_url = "https://api.gold-api.com/price/XAU"

try:
    response = requests.get(gp_url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        
        if "price" in data:
            usd_per_ounce = data["price"]
            usd_per_gram = usd_per_ounce / TROY_OZ_TO_GRAMS
            print(f"Gold Price (1g): {usd_per_gram}")
        else:
            print("Error: Key 'price' not found in response. Received:", data)
    else:
        print(f"Request failed with status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")
except ValueError:
    print("Error: Response was not valid JSON.")
