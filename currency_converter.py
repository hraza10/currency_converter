import pip._vendor.requests
from tkinter import *
from tkinter import ttk
import tkinter as tk

class CurrencyConverter:
    
    # Constructor that takes the url with currency exchange rates as argument
    def __init__(self, url):
        
        # requests.get(url) loads the url page in the program 
        # (Visual Studio Code reuires pip._vendor.requests to import requests)
        # and .json() changes it to a json file
        self.data = pip._vendor.requests.get(url).json()
        self.currencies = self.data['rates']
    
    # Method that takes as parameters an intial currency, currency to be
    # converted to, and the amount to be converted
    # Returns the converted amount into the desirable currency
    def convert(self, from_currency, to_currency, amount):
        
        # if the base currency of the amount is not USD, converts into 
        # USD using the ratios from the url
        if from_currency != 'USD':
            amount = amount/self.currencies[from_currency]
        converted_currency = amount * self.currencies[to_currency]
        amount = round(converted_currency, 2)
        return amount  
    
    


class UserInterface(tk.Tk):
    
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.currency_converter = converter
    
        # Window Intialization
        self.geometry("1000x500")
        self.title("Currency Converter")
    
    
        # Fonts
        small_size = ("Courier", 20, "bold")
        large_size = ("Courier", 40, "bold")

        # Labels

        # Title
        self.window_title = Label(self, text = "REAL TIME CURRENCY CONVERTER")
        self.window_title.place(relx = .5, rely = .1, anchor = CENTER)
        self.window_title.configure(font = large_size)


        # From currency amount entry box
        self.from_amount = Entry(self, borderwidth = 5)
        self.from_amount.place(relx = .3, rely = .35, anchor = CENTER)

        # To currency amount entry box
        self.to_amount = Label(self, text = '', fg = 'black', bg = 'white', relief = SUNKEN, width = 17, borderwidth = 5)
        self.to_amount.place(relx = .7, rely = .35, anchor = CENTER)

        # Dropdown Menus

        # Currency options in the dropdown menus
        currencies = ["USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL" ,"GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]

        # From currency dropdown menu
        self.from_currency_menu = StringVar()
        self.from_currency_menu.set("- SELECT CURRENCY -")
        self.from_dropdown = ttk.Combobox(self, textvariable = self.from_currency_menu, values = currencies, font = small_size)
        self.from_dropdown.place(relx = .3, rely = .25, anchor = CENTER)
        self.from_dropdown['state'] = 'readonly'

        # To currency dropdown menu
        self.to_currency_menu = StringVar()
        self.to_currency_menu.set("- SELECT CURRENCY -")
        self.to_dropdown = ttk.Combobox(self, textvariable = self.to_currency_menu, values = currencies, font = small_size)
        self.to_dropdown.place(relx = .7, rely = .25, anchor = CENTER)
        self.to_dropdown['state'] = 'readonly'


        # Buttons

        # 'CONVERT' button
        self.convert_button = Button(self, text = "CONVERT", command = self.press_convert, font = large_size)
        self.convert_button.place(relx = .5, rely = .85, anchor = CENTER, height = 100, width = 200)


    # When the 'CONVERT' button on the screen is pressed, the currency conversion takes place
    # From-currency amount is converted into to-currency amount
    def press_convert(self):
        font = ("Courier", 20, "bold")
        initial_amount = float(self.from_amount.get())
        from_currency = self.from_dropdown.get()
        to_currency = self.to_dropdown.get()
        
        converted_amount = self.currency_converter.convert(from_currency, to_currency, initial_amount)
        self.converted_amount_label = Label(self, text = f"{initial_amount} {from_currency} equals {converted_amount} {to_currency}", font = font)
        self.converted_amount_label.place(relx = .5, rely = .5, anchor = CENTER)
        self.converted_date_label = Label(self, text = f"Date: {self.currency_converter.data['date']}", font = font)
        self.converted_date_label.place(relx = .5, rely = .6, anchor = CENTER)
        self.to_amount.configure(text = str(converted_amount))

    



if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    window = UserInterface(converter)
    window.mainloop()
