# LinkedCHAIN
LinkedCHAIN is a blockchain-based professional history management tool that revolutionizes the job application and verification process. It leverages blockchain technology to create a secure, transparent, and efficient system that empowers both the job seeker and employers. 


### Overview 
The project is structured as follows:
- **app.py**: Main Python script for running the application.
- **contracts**: Directory containing compiled contract ABIs.
- **pages**: Directory containing various pages of the application, including:
    - About Us
    - Admin
    - Crowdsale
    - Query
    - Super Admin
    - User
- **utility**: Directory containing utility functions for interacting with the blockchain, including:
    - `accounts.py`: Functions related to Ethereum accounts.
    - `functions.py`: Miscellaneous utility functions. 
    - `load_contract_functions`: Functions for loading contract functions.
    - `menu.py`: Menu-related functions.
      

### Features 
#### Initial Coin Offering(token crowdsale):
- **Hyrd(HYD) Token**: Implement using the ERC20 protocol.
- **Crowdsale Participants**: Companies can participate in the crowdsale to recieve HYD tokens and join the ecosystem.
- **Exchange Rate**: 1 HYD per 0.5 ETH, with a minimum purchase of 100 tokens.
- **Token Storage**: Upon making a transaction via crowdsale, tokens will be stored in a LinkedCHAIN wallet.
- **Admin Role**: Entities that complete a transaction via crowdsale are marked as admins.

#### Token Distribution and Validation:
- **Token Distribution**: The distribution wallet can disperse one HYD token to another wallet/user.
- **Validation Requests**: Users with a HYD token can request validation of employment from an admin wallet.
- **Employment Records**: Must include: Company Name, Start Date, End Date, and Responsibilities.
- **Admin Actions**: Admins can accept or decline validation requests. Accepted requests are added to the blockchain.

#### Querying Records:
- **Record Query**: User records can be queried based on their wallet.


### Getting Started 
To run the LinkedCHAIN application, follow these steps:
1. Clone the repository to your local machine.
2. Ensure you have Python and required dependencies installed.
3. Navigate to the project directory in your terminal.
4. Run the `app.py` script: `streamlit run app.py`.
5. Access the application in your web browser at the provided URL.


### Crowdsale Information 
The crowdsale functionality allows companies to purchase Hyrd(HYD) tokens, which are used within the LinkedCHAIN ecosystem to validate and endorse job histories. The exchange rate for the crowdsale is 1 unit to 0.5 Ether. Participants can purchase tokens at this rate and use them to validate employment records.


### Contributing 
We welcome contributions from the community to improve LinkedCHAIN. To contribute, follow these steps:
1. Fork the repository. 
2. Make your changes in a new branch.
3. Test your changes thoroughly. 
4. Submit a pull request with a clear description of your changes. 
