#####################################
# Functions For Streamlit
#####################################
import streamlit as st
import time
from web3 import Web3
import requests
from web3.gas_strategies.time_based import medium_gas_price_strategy
from app import tokenContract, crowdsaleContract, requestsContract, w3


def approve_request(company_address, request_id):
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    # Get current gas price
    gasPrice = w3.eth.gasPrice
    # Get nonce
    nonce = w3.eth.getTransactionCount(company_address)
    try:
        # Build and send transaction to request validation
        transaction = requestsContract.functions.approveRequest(request_id).buildTransaction({
            "from": company_address, 
            "gas": 800000,
            "gasPrice": gasPrice,
            "nonce": nonce
        })

        # Send the transaction
        tx_hash = w3.eth.sendTransaction(transaction)

        # Wait for the transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        st.success(f"Validation accepted successfully!")
        # st.write(tx_receipt)
        time.sleep(3)
        # Remove the approved request from the pending_validations list
        index_to_remove = None
        for i, request in enumerate(st.session_state.pending_validations): 
            if request["request_id"] == request_id:
                index_to_remove = i
                st.write(index_to_remove)
                break
        if index_to_remove is not None:
            st.session_state.pending_validations.pop(index_to_remove)  

        st.switch_page("app.py")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")


def make_a_request(user_address, company_name, start_date, end_date, title, responsibility, company_address):
    data = company_name+start_date+end_date+title+responsibility+user_address
    record_hash = Web3.keccak(text=data)
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    # Get current gas price
    gasPrice = w3.eth.gasPrice
    # Get nonce
    nonce = w3.eth.getTransactionCount(user_address)
    try:
        # Build and send transaction to request validation
        transaction = requestsContract.functions.createRequest(company_name, start_date, end_date, title, responsibility, company_address).buildTransaction({
            "from": user_address, 
            "gas": 500000,
            "gasPrice": gasPrice,
            "nonce": nonce
        })
        # Send the transaction
        tx_hash = w3.eth.sendTransaction(transaction)

        # Wait for the transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        
        # # Filter events emitted by the contract
        event_filter = requestsContract.events.RequestCreated().createFilter(fromBlock='latest')

        # # Get all events matching the filter
        events = event_filter.get_all_entries()

        # # Extract additional information from the event
        event_data = events[-1]  # Assuming the latest event is the one we're interested in
        record = event_data.args
        
        if "pending_validations" not in st.session_state:
            st.session_state.pending_validations = []
        st.session_state.pending_validations.append({
            "record_hash": record_hash.hex(),
            "user_address": record.requester,
            "request_id": record.id,
            "company_name": record.companyName,
            "start_date": record.startDate,
            "end_date": record.endDate,
            "title": record.title,
            "responsibility": record.responsibility,
            "approver_address": record.approver
        })
        st.success(f"Validation request submitted successfully!")
        time.sleep(3)
        st.switch_page("app.py")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")



def purchase_tokens(purchaser_address, beneficiary_address, amount):
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    # Calculate amount in Wei based on the desired amount of tokens and rate
    rate = 2 # 2 tokens per 1 ETH, so 1 token = 0.5 ETH
    eth_amount = amount / rate # Convert token amount to ETH
    amount_in_wei = w3.toWei(eth_amount, "ether")  # Convert ETH to Wei
    # Get gas estimate
    # gasEstimate = w3.eth.estimateGas(
    #     {"to": beneficiary_address, "from": purchaser_address, "value": amount_in_wei+100000}
    # )
    gasEstimate = 800000
    # Get current gas price
    gasPrice = w3.eth.gasPrice
    # Get nonce
    nonce = w3.eth.getTransactionCount(purchaser_address)

    try:
        # Build the transaction
        transaction = crowdsaleContract.functions.buyTokens(beneficiary_address).buildTransaction({
            "from": purchaser_address,
            "value": amount_in_wei,
            "gas": gasEstimate,
            "gasPrice": gasPrice,
            "nonce": nonce
        })
        # Send the transaction
        tx_hash = w3.eth.sendTransaction(transaction)

        # Wait for the transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        st.success(f"Tokens purchased successfully!")
        st.balloons()
        time.sleep(3)
        st.switch_page("app.py")
    except Exception as e:
        st.error(f"Error occured: {str(e)}")


def transfer_tokens(sender_address, receiver_address, amount):
    try:        
        token_in_wei = int(amount * (10 ** 18))  # Convert ETH to Wei

        # Build and send transaction to transfer tokens
        tx_hash = tokenContract.functions.transfer(receiver_address, token_in_wei).transact({"from": sender_address})

        # Wait for the transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        st.success(f"Tokens transferred successfully!")
        time.sleep(3)
        st.switch_page("app.py")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        

def query_approved_requests(account):
    try:
        requests = requestsContract.functions.getRequestsByAccount(account).call()
        return requests
    except Exception as e:
        st.error(f"Error querying approved requests: {e}")
        return []