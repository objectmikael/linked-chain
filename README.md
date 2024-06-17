# LinkedCHAIN
LinkedCHAIN is a blockchain-based professional history management tool that revolutionizes the job application and verification process. It leverages blockchain technology to create a secure, transparent, and efficient system that empowers both the job seeker and employers. 


### Overview 
The project is structured as follows:
- **app.py**: Main Python script for running the application.
- **menu.py**: Menu-related functions.
- **functions.py**: Utility functions. 
- **contracts**: Directory containing compiled contract ABIs.
- **pages**: Directory containing various pages of the application, including:
    - About Us
    - Company Admin
    - Crowdsale
    - LinkedCHAIN Admin
    - Product Roadmap
    - Query
    - User  


### Features 
#### Initial Coin Offering(token crowdsale):
- **Hyrd(HYD) Token**: Implement using the ERC20 protocol.
- **Crowdsale Participants**: Companies participate in a crowdsale to fund the platform, join the ecosystem and mint HYD tokens. 
- **Exchange Rate**: 1 HYD per 0.5 ETH, with a minimum purchase of 100 tokens.
- **Token Storage**: Upon making a transaction via crowdsale, tokens will be stored in a LinkedCHAIN wallet.
- **Admin Role**: Entities that complete a transaction via crowdsale are marked as admins.

#### Token Distribution and Validation:
- **Token Distribution**: The distribution wallet can disperse one HYD token to another wallet/user.
- **Validation Requests**: Users with a HYD token can request validation of employment from an admin wallet.
- **Employment Records**: Must include: Company Name, Start Date, End Date, and Responsibilities.
- **Admin Actions**: Admins can accept or decline validation requests. Accepted requests are added to a user’s record on the blockchain. 
#### Querying Records:
- **Record Query**: User records can be queried based on their wallet.


### Getting Started 
To run the LinkedCHAIN application, follow these steps:
1. Clone the repository to your local machine.
2. Ensure you have Python and required dependencies installed.
3. Navigate to the project directory in your terminal.
4. Open Ganache and run an instance with 10 accounts. 
5. Add all 10 accounts to metamask.
6. Open Remix and connect to the Injected-Metamask environment. 
7. Use Remix to compile and deploy contracts in the following order: deployer, token, crowdsale, requests.
8. Copy each contract address and replace the appropriate variables in `app.py`.
9. Run the `app.py` script: `streamlit run app.py`.
10. Access the application in your web browser at the provided URL.


### Crowdsale Information 
The crowdsale functionality allows companies to purchase Hyrd(HYD) tokens, which are used within the LinkedCHAIN ecosystem to validate and endorse job histories. The exchange rate for the crowdsale is 1 unit to 0.5 Ether. Participants can purchase tokens at this rate and use them to validate employment records.


### Contributing 
We welcome contributions from the community to improve LinkedCHAIN. To contribute, follow these steps:
1. Fork the repository. 
2. Make your changes in a new branch.
3. Test your changes thoroughly. 
4. Submit a pull request with a clear description of your changes. 
