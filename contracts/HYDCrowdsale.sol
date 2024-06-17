
pragma solidity ^0.5.0; // Solidity compiler version compatible with 0.5.0.


/////////////
// IMPORTS //
/////////////
import "./HYDToken.sol"; // Import the HYDToken contract functionality.
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol"; // Crowdsale functionality.
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol"; // Mint tokens during the crowdsale.
import "./Requests.sol"; // Import the Requests contract functionality


///////////////////////////
// HYDCROWDSALE CONTRACT //
///////////////////////////
contract HYDCrowdsale is Crowdsale, MintedCrowdsale {
    address public beneficiary;  // Declare a state variable to store the beneficiary address

    // Define a constructor that accepts parameters for the rate(tokens per wei), the wallet to receive ETH, the HYDToken contract address, the beneficiary of token/eth address
    constructor(
        uint256 rate,
        address payable wallet,
        HYDToken token,
        address beneficiaryAddress
    )
    // Initialize the crowdsale with the provided parameters.
    Crowdsale(rate, wallet, token) public {

        // Checks that the beneficiaryAddress provided as an argument to the contract constructor is not the zero address 
        require(beneficiaryAddress != address(0), "Beneficiary address cannot be the zero address");
        beneficiary = beneficiaryAddress;
    }

    // Override the _preValidatePurchase function to enforce a minimum purchase amount of 50 ETH or 100 tokens.
    function _preValidatePurchase(address buyer, uint256 weiAmount) internal view {
        require(weiAmount >= 50 ether, "Minimum purchase is 50 ETH(100 tokens).");
        super._preValidatePurchase(buyer, weiAmount);
    }
}


///////////////////////////
// HYDDEPLOYER CONTRACT ///
///////////////////////////
contract HYDDeployer {
    address public hydtoken_address;  // Declare a variable to store the HYDToken deployed contract address.
    address public hydcrowdsale_address;  // Declare a variable to store the HYDCrowdsale deployed contract address.
    address public requests_address; // Declare a variable to store the Requests deployed contract address.

    // Define a constructor that accepts parameters for the token's name, symbol, and the wallet to receive ETH.
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
    public 
    {
        HYDToken token = new HYDToken(name, symbol, 0);  // Deploy a new instance of HYDToken with the provided name, symbol, and initial supply of 0.
        hydtoken_address = address(token);  // Define hydtoken_address to store the deployed contract.

        HYDCrowdsale crowdsale = new HYDCrowdsale(2, wallet, token, msg.sender);  // Deploy a new instance of HYDCrowdsale with a rate of 2, the wallet address, the HYDToken contract address, the deployer of the contract
        hydcrowdsale_address = address(crowdsale);  // Define hydcrowdsale_address to store the deployed contract

        token.addMinter(hydcrowdsale_address);  // Grant the HYDCrowdsale contract the permission to mint new tokens by adding it as a minter.
        token.renounceMinter();  // Renounce the deployer's minter role, ensuring that only the crowdsale contract can mint new tokens.

        Requests requests = new Requests(hydtoken_address); // Deploy a new instance of Requests. hydtoken_address
        requests_address = address(requests); // Define requests_address to store the deployed contract.
    }
}
