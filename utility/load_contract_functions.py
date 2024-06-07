#####################################
# Functions for loading
# contract functions.
#####################################

# Import Dependencies
import streamlit as st
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from web3 import Web3

# Loads env variables.
load_dotenv()

# Connects to Ganache.
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Caches the contract on load.
@st.cache(allow_output_mutation=True)

# Defines function to load the HYDToken contract.
def load_token_contract():
    with open(Path('./contracts/compiled/token_contract_abi.json')) as f:
        contract_abi = json.load(f)
    contract_address = os.getenv("TOKEN_SMART_CONTRACT_ADDRESS")
    token_contract = w3.eth.contract(address=contract_address,abi=contract_abi)
    return token_contract

# Defines function to load the HYDCrowdsale contract.
def load_crowdsale_contract():
    with open(Path('./contracts/compiled/crowdsale_contract_abi.json')) as f:
        contract_abi = json.load(f)
    contract_address = os.getenv("CROWDSALE_SMART_CONTRACT_ADDRESS")
    crowdsale_contract = w3.eth.contract(address=contract_address,abi=contract_abi)
    return crowdsale_contract

# Defines function to load the HYDValidation contract.
def load_validation_contract():
    with open(Path('./contracts/compiled/validation_contract_abi.json')) as f:
        contract_abi = json.load(f)
    contract_address = os.getenv("VALIDATION_SMART_CONTRACT_ADDRESS")
    validation_contract = w3.eth.contract(address=contract_address,abi=contract_abi)
    return validation_contract

# Loads contracts to a variable.
tokenContract = load_token_contract()
crowdsaleContract = load_crowdsale_contract()
validationContract = load_validation_contract()
