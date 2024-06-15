#####################################
# Main Python script for
# running the application.
#####################################

# Imports Dependencies
import json
from pathlib import Path
from web3 import Web3
import streamlit as st
from menu import menu

#####################################
# Variables.
#####################################
WEB3_PROVIDER_URI='http://127.0.0.1:7545'
TOKEN_SMART_CONTRACT_ADDRESS='0xa9ff0c76f0f1610E4B908a0Bff0482aC08c2A4e6'
CROWDSALE_SMART_CONTRACT_ADDRESS='0xc335fd7319DB619F01BD43070C091caE27bF5dC6'
REQUESTS_SMART_CONTRACT_ADDRESS='0xc0da2A9C1a4c42cb01E152C3A55fF281eA6dcE2F'
DEPLOYER_SMART_CONTRACT_ADDRESS='0xc8Cde4E9a8a289afF86Aa92239de7D38743ca196'
ETH_USD = 3560

# Connects to Ganache.
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))

# Checks connection to Ganache.
if w3.isConnected():
    st.success("Connected to Ethereum via Ganache")
else:
    st.error("Failed to connect to Ethereum")

#####################################
# Functions for loading
# contract functions.
#####################################
# Caches the contract on load.
# @st.cache(allow_output_mutation=True)

# Defines function to load the HYDToken contract.
def load_token_contract():
    with open(Path('./contracts/compiled/token_abi.json')) as f:
        contract_abi = json.load(f)
    token_contract = w3.eth.contract(address=TOKEN_SMART_CONTRACT_ADDRESS, abi=contract_abi)
    return token_contract

# Defines function to load the HYDCrowdsale contract.
def load_crowdsale_contract():
    with open(Path('./contracts/compiled/crowdsale_abi.json')) as f:
        contract_abi = json.load(f)
    crowdsale_contract = w3.eth.contract(address=CROWDSALE_SMART_CONTRACT_ADDRESS, abi=contract_abi)
    return crowdsale_contract

# Defines function to load the HYDValidation contract.
def load_requests_contract():
    with open(Path('./contracts/compiled/requests_abi.json')) as f:
        contract_abi = json.load(f)
    requests_contract = w3.eth.contract(address=REQUESTS_SMART_CONTRACT_ADDRESS, abi=contract_abi)
    return requests_contract

# Loads contracts to a variable.
tokenContract = load_token_contract()
crowdsaleContract = load_crowdsale_contract()
requestsContract = load_requests_contract()


#####################################
# Functions related to
# Ethereum accounts.
#####################################
# Creates a dictionary for labeled Ganache accounts. 
accounts = w3.eth.accounts
names = ["Amazon", "Disney", "OpenAI", "Walmart", "Andy Murray", "Chuck Norris", "Martha Stewart", "Snoop Dogg", "Walter White", "LinkedCHAIN"]
options_mapping = dict(zip(names, accounts))
display_names = list(options_mapping.keys())


#####################################
# Set Roles and Menu
#####################################
# Initializes st.session_state.role to None.
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieves the role from session state to initialize the widget
st.session_state._role = st.session_state.role
def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role

# Creates selectbox to choose role.
st.selectbox(
    "Select your role:",
    [None, "user", "company-admin", "linkedchain-admin"],
    key="_role",
    on_change=set_role
)

# Renders the dynamic menu!
menu() 


#####################################
# Homepage
#####################################
st.markdown(""" 
    <center>
        <h1>
            Welcome to LinkedCHAIN
        </h1>
        <h5>A Blockchain Professional History Management Tool</h5>
    </center>""", unsafe_allow_html=True)

st.header("",divider='rainbow')

total_supply_in_wei = tokenContract.functions.totalSupply().call()
total_supply = int(total_supply_in_wei/ 10**18)
available_tokens_in_wei = tokenContract.functions.balanceOf(DEPLOYER_SMART_CONTRACT_ADDRESS).call()
available_tokens = int(available_tokens_in_wei/ 10**18)
weiRaised = crowdsaleContract.functions.weiRaised().call()
value_in_ether = int(Web3.fromWei(weiRaised, 'ether'))
eth_price_usd = ETH_USD
funds_raised_usd = value_in_ether*int(eth_price_usd)

st.markdown(f"""
    <center>
        <div style="display: inline-block;">
            <h4>Tokens Minted</h4>
            <h6>{total_supply}</h6>
        </div>
        <div style="display: inline-block;">
            <h4>Available Tokens</h4>
            <h6>{available_tokens}</h6>
        </div>
        <div style="display: inline-block;">
            <h4>Total Funds Raised</h4>
            <h6>{value_in_ether} ETH (${funds_raised_usd})</h6>
        </div>
    </center>
""", unsafe_allow_html=True)

st.header("",divider='rainbow')

# CROWDSALE CTA
st.header("Invest With Us Today!")
if st.button(":green[Click to fund]"):
    st.switch_page("pages/crowdsale.py")
