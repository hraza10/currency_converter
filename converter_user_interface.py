""" Creates a user interface that performs currency conversions. """

import tkinter as tk
from tkinter import *
from tkinter import ttk
from currency_converter import CurrencyConverter
    

class UserInterface(tk.Tk):
    """ The purpose of this class is to create a user interface which 
    a user can interact with to convert a specified currency to another. 
    The user interface will include objects such as Entry, Label, Button, 
    and Combobox.

    Attributes:
        currency_converter (CurrencyConverter): object containing information 
            from the currency conversion api, such as rates and exchange rate 
            date.
        window_title (Label): title name of the converter user interface.
        from_amount (Entry): entry box where the user enters the initial currency 
            that needs to be converted.
        to_amount (Entry): entry box where the user enters the currency that their 
            currency needs to be converted to.
        from_currency_menu (StringVar): variable containing the string that appears 
            in the from_dropdown menu before it is clicked.
        to_currency_menu (StringVar): variable containing the string that appears 
            in the to_dropdown menu before it is clicked.
        from_dropdown (ttk.Combobox): dropdown menu that provides options for acceptable 
            currencies that can be converted to another.
        to_dropdown (ttk.Combobox): dropdown menu that provides options for acceptable 
            currencies that a currency can be converted to.
        convert_button (Button): the button user clicks when they want the conversion to 
            occur. 
    """

    def __init__(self, converter):
        """ Utilizes the tk.Tk __init__() method to create a tk.Tk 
        object. 

        Args:
            converter (CurrencyConverter): given object containing information 
                from the currency conversion api, such as rates and exchange 
                rate date.
        Side effects:
            Initializes currency_converter, window_title, from_amount, to_amount, 
                from_currency_menu, from_dropdown, to_currency_manu, from_dropdown, 
                to_dropdown, and convert_button attributes.
        """

        # utilizes tk.Tk constructor
        super().__init__()
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

    def press_convert(self):
        """ When the 'CONVERT' button on the screen is pressed, the currency conversion 
        takes place. From-currency amount is converted into to-currency amount using 
        the convert() method from Currency Converter. """
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

def main():
    """ Establishes the url of the api that the data will be accessed from. Intializes a 
    CurrencyConverter object to pull information from the api. Creates a window as a 
    UserInterface object that the user can interact with. Utilizes mainloop() function 
    to let the window run until the user closes it. """

    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    window = UserInterface(converter)
    window.mainloop()


if __name__ == '__main__':
    main()
