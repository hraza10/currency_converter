# currency_converter

Currency Converter project created using Python and Tkinter library (for GUI from scratch). The currency converter calculates real time exchange rate of 162 distinct currencies using latest exchange rate data from an API. Utilizes Python's Tkinter GUI toolkit to create an interactive GUI to perform conversion between any of the 162 currencies. Allows user to select before and after currencies from dropdown menus and enter amount in entry box.


## currency_converter.py

Reads data from the given API and and performs calculations to convert a given amount in a given currency to the specified currency. The module also takes command line arguments of from_currency, to_currency, and amount for the user to directly obtain converted amount from the terminal.


## converter_user_interface.py

Creates user interface window that the user can interact with using the Python Tkinter GUI toolkit. User can select the initial currency and conversion currency from dropdown menus, and enter the amount to be converted in the entry box. When the user presses the 'CONVERT' button after selecting and entering the required information, the window displays the conversion amount, the currency that the amount was converted to, and the exchange rate's closing date, which is the rate used to perform the conversion.
