""" Accesses currency exchange rate and date from a public api. 
Performs calculations to convert one currency to another. """

from argparse import ArgumentParser
import sys
import pip._vendor.requests

class CurrencyConverter:
    """ The purpose of this class is to create a object containing information 
    from the currency conversion api, such as rates and exchange rate date. 
    Provides a convert method that performs currency conversions using currency
    exchange rates and dates.

    Attributes:
        data (dict): dictionary that copies the information present in the api. 
            Has a 'rates' key that has another dictionary as a value; its keys 
            are currency codes and their values are exchange rate ratios as 
            compared to USD.
        currencies (dict): the 'rates' dictionary in the data dictionary with keys 
            that are currency codes and their values are exchange rate ratios as 
            compared to USD.
    """
    def __init__(self, url):
        """ Intializes a Currency Converter object.
        
        Args:
            url (str): url of the api containing currency exchange 
                rates and date

        Side effects:
            Intializes data and currencies attributes. 
        """

        # requests.get(url) loads the url page in the program 
        # (Visual Studio Code reuires pip._vendor.requests to import requests)
        # .json() changes it to a json file
        self.data = pip._vendor.requests.get(url).json()
        self.currencies = self.data['rates']
    
    # Method that takes as parameters an intial currency, currency to be
    # converted to, and the amount to be converted
    # Returns the converted amount into the desirable currency
    def convert(self, from_currency, to_currency, amount):
        """ Performs currency conversion using the given amount in a given 
        currency and a currency to be converted to. 
        
        If the base currency of the amount is not USD, converts into USD 
        using the ratios from the api. 

        Args:
            from_currency (str): currency code of the currency that needs 
                to be converted.
            to_currency (str): currency code of the currency that amount is 
                converted to.
            amount (float): given amount of money that needs to be converted.
        
        Returns:
            amount (float): given amount of money that needs to be converted.
        """
        
        if from_currency != 'USD':
            amount = amount/self.currencies[from_currency]
        converted_currency = amount * self.currencies[to_currency]
        amount = round(converted_currency, 2)
        return amount

def parse_args(arglist):
    """ Parses command-line arguments.

    The following optional command-line arguments are defined:

    from_currency (str): currency code of the currency that needs 
        to be converted.
    to_currency (str): currency code of the currency that amount is 
        converted to.
    amount (float): given amount of money that needs to be converted.

    Args:
        arglist (list of str): a list of command-line arguments.

        Returns:
        namespace: a namespace with variables from_currency, to_currency, 
            and amount.
    """

    parser = ArgumentParser()
    parser.add_argument("from_currency", 
                        help="currency code of the currency that needs to "
                             "be converted.")
    parser.add_argument("to_currency", 
                        help="currency code of the currency that amount is "
                             "converted to.")
    parser.add_argument("amount", type=float, 
                        help="given amount of money that needs to be converted.")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    conversion = CurrencyConverter(url)
    result = conversion.convert(args.from_currency, args.to_currency, args.amount)
    print(result)
