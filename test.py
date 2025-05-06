from BinaryOptionsTools import pocketoption
import os
from dotenv import load_dotenv
load_dotenv()

ssid = os.getenv("SSID")
demo = True
#ssid = input("Enter your ssid: ")
api = pocketoption(ssid, demo)

data = api.GetCandles("EURUSD_otc", 5)
print(data)
print(f"GET BALANCE: {api.GetBalance()}")
#api.Put(1, "EURUSD_otc", 60, False)

