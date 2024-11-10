from bs4 import BeautifulSoup
import requests
import pandas as pd
import schedule 
from datetime import datetime
import time 

url = "https://www.beyoung.in/mauve-pink-revere-neck-full-sleeve-polo"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_product_data(url):

	response = requests.get(url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.text,"lxml")

		product = soup.find("h1").text.strip()

		price = soup.find("span", class_= "realprice").text.strip()

		timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		return{
		"product": product,
		"price": price,
		"timestamp": timestamp
		}

	else:
		print("Failed to fetch the page.")
		return None
    

	
product_data = fetch_product_data(url)
print(product_data)
 
def save_to_csv(data, filename = "product_prices.csv"):
	try:
		df = pd.read_csv(filename)
	except FileNotFoundError:
		df = pd.DataFrame(columns=['product','price','timestamp'])

	df = df.append(data, ignore_index = True)
	df.to_csv(filename , index = False)
	print(f"Data saved to {filename}.")


if product_data:
	save_to_csv(product_data)

#scheduling

def job():
	data = fetch_product_data(url)
	if data:
		save_to_csv(data)

schedule.every().day.at('10:00').do(job)

while True:
	schedule.run_pending()
	time.sleep(2)



	

	    

	


	














