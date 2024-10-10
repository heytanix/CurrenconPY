# Importing the requests library to handle HTTP requests
import requests

# Function to get real-time exchange rates:
# This function takes in the API key, base currency, and target currency as inputs,
# makes a request to the ExchangeRate API, and returns the conversion rate between the two currencies.
def get_exchange_rate(api_key, base_currency, target_currency):
    # Constructing the API URL to get the exchange rate between the base and target currencies
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    
    # Making a GET request to the API
    response = requests.get(url)
    
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # If successful, extract the exchange rate from the API response in JSON format
        data = response.json()
        return data['conversion_rate']
    else:
        # If not successful, raise an exception with the error status code
        raise Exception(f"Failed to retrieve exchange rate. Status code: {response.status_code}")
    
# Function to perform currency conversion:
# This function takes in the API key, base currency, target currency, and amount to convert,
# calculates the converted amount using the exchange rate, and returns the result.
def convert_currency(api_key, base_currency, target_currency, amount):
    # Get the exchange rate between the base and target currencies
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    
    # Multiply the amount by the exchange rate to get the converted amount
    converted_amount = amount * rate
    return converted_amount

# Main program function to handle user interaction and conversion process
def main():
    api_key = "21531ecbe04a7e5fa222fcb6"  # API key from exchangerate-api.com
    print("Welcome to Currency converter!")
    
    # Taking input from the user: base currency, target currency, and amount to convert
    base_currency = input("Enter the base currency (example: USD): ").upper()
    target_currency = input("Enter the target currency (example: INR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    try:
        # Convert the entered amount using the provided currencies
        converted_amount = convert_currency(api_key, base_currency, target_currency, amount)
        
        # Display the converted amount to the user
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    
    except Exception as e:
        # If there's an error (such as an issue with the API request), print the error message
        print(e)

# This ensures that the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
