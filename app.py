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
# URI of the Web3 provider (Ganache in this case).
WEB3_PROVIDER_URI='http://127.0.0.1:7545' 

# Ethereum addresses for the smart contracts and deployer wallet.
TOKEN_SMART_CONTRACT_ADDRESS='0xA77cBf5523B3fE13b8cFE6e8E39358070e75CD46'
CROWDSALE_SMART_CONTRACT_ADDRESS='0x52802E705A6c3EbB0d96b49A825406c3e4747217'
REQUESTS_SMART_CONTRACT_ADDRESS='0x888100fb410B4EB5e0FF52f526cf071D119e1C44'
DEPLOYER_WALLET_ADDRESS='0xF6270AA0e9aaA88c20bbCFA63c6C1E258E4C44C8'

# Current Ethereum to USD conversion rate.
ETH_USD = 3560

# Connects to the Ethereum network using Ganache.
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))

# Checks connection to the Ethereum network.
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

# Loads the contracts into variables.
tokenContract = load_token_contract()
crowdsaleContract = load_crowdsale_contract()
requestsContract = load_requests_contract()


#####################################
# Functions related to
# Ethereum accounts.
#####################################
# Creates a dictionary for labeled Ganache accounts.
accounts = w3.eth.accounts
# Names corresponding to the accounts.
names = ["Amazon", "Disney", "OpenAI", "Walmart", "Abby Murphy", "Chris Norman", "Marissa Stwart", "Selma Grant", "Wisdom Johnson", "LinkedCHAIN"]
# Maps account names to their addresses.
options_mapping = dict(zip(names, accounts))
# List of display names for the accounts.
display_names = list(options_mapping.keys())


#####################################
# Set Roles and Menu
#####################################
# Initializes st.session_state.role to None.
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieves the role from session state to initialize the widget.
st.session_state._role = st.session_state.role
def set_role():
    # Callback function to save the role selection to Session State.
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
# Displays the homepage content with welcome messages.
st.markdown(""" 
    <center>
        <h1>
            Welcome to LinkedCHAIN
        </h1>
        <h5>A Blockchain Professional History Management Tool</h5>
    </center>""", unsafe_allow_html=True)

# Adds a header with a rainbow divider.
st.header("",divider='rainbow')

# Fetches and displays token and crowdfunding information.
total_supply_in_wei = tokenContract.functions.totalSupply().call()
total_supply = int(total_supply_in_wei/ 10**18)
available_tokens_in_wei = tokenContract.functions.balanceOf(DEPLOYER_WALLET_ADDRESS).call()
available_tokens = int(available_tokens_in_wei/ 10**18)
weiRaised = crowdsaleContract.functions.weiRaised().call()
value_in_ether = int(Web3.fromWei(weiRaised, 'ether'))
eth_price_usd = ETH_USD
funds_raised_usd = value_in_ether*int(eth_price_usd)

# Displays token supply and fundraising information.
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

# Adds a header with a rainbow divider.
st.header("",divider='rainbow')

# CROWDSALE Call-To-Action (CTA)
# Displays a header for the investment section.
st.header("Invest With Us Today!")

# Creates a button for funding the crowdsale. If clicked, navigates to the crowdsale page.
if st.button(":green[Click to fund]"):
    st.switch_page("pages/crowdsale.py")
