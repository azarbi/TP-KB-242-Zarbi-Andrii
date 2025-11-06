import requests
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

allowed = ["USD", "EUR", "PLN"]
currency = input("Enter currency (USD, EUR, PLN): ").upper()

if (currency not in allowed):
    print("Error: enter USD, EUR or PLN")
    exit()

amount = float(input("Enter amount of choiced currency: "))

rate = None

for elem in response.json():            
    if (elem["cc"] == currency):
        rate = elem["rate"]
        break

if rate is None:
    print("Error: currency rate not found.")
    exit()

result = rate * amount
print(f"Currency: {currency} \nRate in UAH: {rate} \nAmount: {amount} \nResult in UAH: {result}")