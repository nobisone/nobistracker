#Nobis Exodus

import requests
import json
import tkinter as tk
import webbrowser

API_ENDPOINT = "https://api.coinmarketcap.com/v2/ticker/?convert=USD"

def refresh_prices(table):
    # Get the current prices of all cryptocurrencies from CoinMarketCap.
    response = requests.get(API_ENDPOINT)
    data = json.loads(response.content)
    # Update the prices of the cryptocurrencies that have changed.
    for row in table.winfo_children():
        symbol = row.config('text')[-1].split()[0]
        if symbol in data["data"]:
            price = data["data"][symbol]["quotes"]["USD"]["price"]
            row.config(text=symbol + " - " + price)

# Get the current prices of all cryptocurrencies from CoinMarketCap.
response = requests.get(API_ENDPOINT)
data = json.loads(response.content)

# Create the window.
window = tk.Tk()

# Add the logo and branding.
logo = tk.PhotoImage(file:"https://github.com/nobisone/nobistracker/blob/b5fea7f0062c2e51d13674cb5a1f7755e47b9dbc/Nobis%20One%20logo.png")
logo = logo.subsample(2) # Resize the image to fit the label.
brand = tk.Label(window, text="Nobis Exodus", image=logo)
brand.pack()
Nobis One logo.png
# Add the table.
table = tk.Frame(window)
for currency in data["data"].values():
    row = tk.Label(table, text=currency["symbol"] + " - " + currency["quotes"]["USD"]["price"])
    row.pack()
table.pack()

# Add the link to the website.
website = tk.Label(window, text="Visit our website: https://www.nobis1.com", fg="blue", cursor="hand2")
website.pack()
website.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.nobis1.com"))

# Add the button to refresh the prices.
refresh_button = tk.Button(window, text="Refresh Prices", command=lambda: refresh_prices(table))
refresh_button.pack()

# Start the main loop.
window.mainloop()
