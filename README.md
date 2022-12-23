# BestBuy Monitor - Mahian Khan
This Python script automates the process of checking the availability of certain products on the Best Buy website and sending notifications to a Discord channel when the availability of a product changes.


## Features

- Tracks the availability of multiple products on the Best Buy website
- Sends notifications to a Discord channel when the availability of a product changes
- Uses HTTP and HTTPS proxies to optimize performance
- Utilizes multithreading and a queue to efficiently check the availability of products
- Includes a checkStock class to organize and reuse code



## Requirements
- Python 3
- The following Python modules:
    - requests
    - bs4 (Beautiful Soup)
    - discord_webhook
## Setup
    1. Clone or download this repository
    2. Install the required Python modules: pip install -r requirements.txt
    3. Edit the checkStock class in the product_availability_tracker.py script to specify the products you want to track and the Discord webhook URL
    4. Paste a set of non-authenticated proxies to the 'valid_proxies.txt' file.
    5. Run the script: python product_availability_tracker.py
