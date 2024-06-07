#####################################
# Functions related to
# Ethereum accounts.
#####################################

# Imports dependencies.
import os
from web3 import Web3
from dotenv import load_dotenv

# Loads env variables.
load_dotenv()

# Connects to Ganache.
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Creates a dictionary for labeled Ganache accounts. 
accounts = w3.eth.accounts
names = ["Amazon", "Disney", "OpenAI", "Walmart", "Andy Murray", "Chuck Norris", "Martha Stewart", "Snoop Dogg", "Walter White", "LinkedCHAIN"]
options_mapping = dict(zip(names, accounts))
display_names = list(options_mapping.keys())
