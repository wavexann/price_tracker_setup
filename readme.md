# Price Tracker Project

This is a simple price tracker script that fetches product prices from an e-commerce website (Beyoung in this case) and stores the data along with the timestamp in a CSV file.

## Features
- Scrapes product details such as name, price, and timestamp.
- Saves the data to a CSV file.
- Can be scheduled to run every day using Task Scheduler on Windows.

- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `schedule`
    
## How to Run
1. Install the required packages:
   ```bash
   pip install requests beautifulsoup4 pandas schedule

2. Clone the repository:
   git clone https://github.com/your-username/price-tracker.git
   cd price-tracker

3. Edit the script (optional):

    If you want to track a different product, change the URL in the script.

4. Run the script:
   python price_tracker.py (This will fetch the product data and save it in a CSV file (product_prices.csv).)

Output
{'product': 'Mauve Pink Revere Neck Full Sleeve Polo', 'price': '₹ 799', 'timestamp': '2024-11-10 21:01:13'}
Data saved to product_prices.csv.

Schedule the task to run automatically:

    Windows Task Scheduler:
        Open Task Scheduler on your computer.
        Create a new task:
            Set the task to run Daily at your desired time.
            Set the Action to run the Python script.
        Save the task and it will run automatically every day.

Notes

    This script tracks the product’s price once a day and logs it.
    The data is saved in a CSV file (product_prices.csv).


    

      

   

    
