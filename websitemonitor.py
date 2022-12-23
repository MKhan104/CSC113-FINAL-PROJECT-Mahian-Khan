import random
import os
import requests
import time
import sys
from bs4 import BeautifulSoup
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed


class checkStock:

    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    stores = {
        "iBUYPOWER - Gaming Desktop" : 
        [
            "https://www.bestbuy.com/site/ibuypower-slatemr-gaming-desktop-intel-i3-12100f-8gb-ddr4-memory-nvidia-geforce-gtx-1650-4gb-500gb-nvme-ssd-black/6500551.p",
            ".add-to-cart-button",
            "Add to Cart",
            "iBUYPOWER - SlateMR Gaming Desktop - Intel i3-12100F",
            "6500551",
            "$779.99",
        ],

        "PS5 DISC" : 
        [
            "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149",
            ".add-to-cart-button",
            "Add to Cart",
            "Sony - PlayStation 5 Console",
            "6523167",
            "$499.99",
        ],

        "PS5 DIGITAL" : 
        [
            "https://www.bestbuy.com/site/apple-10-9-inch-ipad-latest-model-with-wi-fi-64gb-blue/5200904.p",
            ".add-to-cart-button",
            "Add to Cart",
            "Apple - 10.9-Inch iPad (Latest Model) with Wi-Fi",
            "5200904",
            "$399.00",
        ],

        "3070 Founders GPU" : 
        [
            "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
            ".add-to-cart-button",
            "Add to Cart",
            "NVIDIA GeForce RTX 3070 8GB GDDR6",
            "6429442",
            "$499.99",
        ],

        "Samsung - 55 Class Q70A " : 
        [
            "https://www.bestbuy.com/site/samsung-55-class-q70a-series-qled-4k-uhd-smart-tizen-tv/6452056.p?skuId=6452056",
            ".add-to-cart-button",
            "Add to Cart",
            "Samsung - 55 Class Q70A Series QLED 4K UHD Smart Tizen TV",
            "6452056",
            "$799.99",
        ],
    }

    #Get information from the atc button using a proxy
    def getButton(self, url, selection):
        with open("valid_proxies.txt","r") as f:
            self.proxies = f.read().split("\n")
        self.counter = random.randint(0, len(self.proxies))

        user_agent = random.choice(self.user_agent_list)
        headers = {"User-Agent" : user_agent}
        try:
            print(f"Using the proxy: {self.proxies[self.counter]}")
            req = requests.get(url, headers=headers, proxies = {"http": self.proxies[self.counter],"https": self.proxies[self.counter]})
            soup = BeautifulSoup(req.content, "html.parser")
            return soup.select(selection)
        except:
            print("Proxy failed, attempting new one...")



    def runCheck(self, interval):     
        for key in self.stores:
            myResult = self.getButton(self.stores[key][0], self.stores[key][1])
            if self.stores[key][2] in str(myResult):
                os.system("echo \033[32m" + f'[{datetime.now()}] :: {key}: {self.stores[key][3]}')
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1041284568302489640/qkdvvkFZKymLbuEugu8Ql9U3FI7uwsRN9T7vFVdYOAo6tztuW1mdy1LvCtLVAe3dAfCG', username="Best Buy")
                embed = DiscordEmbed(title= self.stores[key][3], description= "Available NOW", url=self.stores[key][0], color=242424)
                embed.set_author(name='https://www.bestbuy.com/ -- by Mahian', url='', icon_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2Fbestbuy%2F&psig=AOvVaw1xgtOM3y03-F8pbfrLyGJR&ust=1644195619713000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjm95Lw6fUCFQAAAAAdAAAAABAD')
                embed.set_footer(text='Embed Footer Text', url='')
                embed.set_timestamp()
                embed.add_embed_field(name='SKU', value= self.stores[key][4])
                embed.add_embed_field(name='Price', value= self.stores[key][5])
                embed.add_embed_field(name='᲼Proxy', value= self.proxies[self.counter])
                embed.add_embed_field(name='᲼᲼', value='᲼᲼')
                webhook.add_embed(embed)
                response = webhook.execute()
            else:
                os.system("echo \033[31m "+ f'[{datetime.now()}] :: {key}: {self.stores[key][3]}')
            time.sleep(interval)
        self.runCheck(interval)
    

checkStock().runCheck(1.33)




