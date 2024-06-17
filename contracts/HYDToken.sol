
pragma solidity ^0.5.0; // Solidity compiler version compatible with 0.5.0.


/////////////
// IMPORTS //
/////////////
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol"; // ERC-20 token standard implementation
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol"; // Detailed token information (name, symbol, and decimals)
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol"; // Allow minting functionality


///////////////////////
// HYDTOKEN CONTRACT //
///////////////////////
contract HYDToken is ERC20, ERC20Detailed, ERC20Mintable {    
    // Define a constructor that accepts parameters for the token's name, symbol, and initial supply.
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
    // Initialize the token with the provided name, symbol and 18 decimals.
    ERC20Detailed(name, symbol, 18) public {}

    function transfer(address recipient, uint256 amount) public returns (bool) {  // Override the transfer function to add a check if the recipient already has a token.
        require(balanceOf(recipient) + amount <= 1 * (10 ** uint256(decimals())), "Recipient already has a token");  // Check if the recipient already has tokens
        return super.transfer(recipient, amount);  // Perform the transfer if the recipient's balance does not exceed one token
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {  // Override the transferFrom function to apply the same logic as transfer.
        require(balanceOf(recipient) + amount <= 1 * (10 ** uint256(decimals())), "Recipient already has a token");  // Check if the recipient already has tokens
        return super.transferFrom(sender, recipient, amount); // Perform the transfer if the recipient's balance does not exceed one token
    }
}


