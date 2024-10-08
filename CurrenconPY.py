#Importing important libraries
import requests

#Function to get real-time exchange rates:
def  get_exchange_rate(api_key, base_currency, target_currency):
    url=  f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response=requests.get(url)
    
    if response.status_code==200:
        data=response.json()
        return data['conversion_rate']
    else:
        raise  Exception(f"Failed to retrieve exchange rate. Status code: {response.status_code}")
    
#Function to perform  currency conversion:
def  convert_currency(api_key, base_currency, target_currency, amount):
    rate=get_exchange_rate(api_key, base_currency, target_currency)
    converted_amount=amount*rate
    return converted_amount

#Main program
def main():
    api_key="21531ecbe04a7e5fa222fcb6" #API key from exchangerate-api.com
    print("Welcome to Currency converter!")
    
    #Taking user input
    base_currency=input("Enter the base currency (example: USD): ").upper()
    target_currency=input("Enter the target currency (example: INR): ").upper()
    amount=float(input("Enter the amount to convert: "))
    
    try:
        # Convert currency
        converted_amount = convert_currency(api_key, base_currency, target_currency, amount)
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
