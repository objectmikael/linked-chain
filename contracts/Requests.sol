pragma solidity ^0.5.0;  // Solidity compiler version compatible with 0.5.0.
pragma experimental ABIEncoderV2; // Enable the experimental ABIEncoderV2 feature, allowing the contract to return structs in public and external functions.


interface IHYDToken {
    function balanceOf(address account) external view returns (uint256);
}

///////////////////////
// REQUESTS CONTRACT //
///////////////////////
contract Requests {
    enum RequestStatus { Pending, Approved, Rejected } // Define three states of a request.

    struct Request {  // Struct to represent a request.
        uint256 id;
        string companyName;
        string startDate;
        string endDate;
        string title;
        string responsibility;
        address approver;
        RequestStatus status;
    }

    mapping(address => Request[]) public requests;  // Mapping to store requests by requester address.
    mapping(uint256 => Request) public allRequests;  // Mapping to store all requests by ID.
    mapping(uint256 => address) public requestToRequester;  // Mapping to store requester address by request ID.
    uint256 public totalRequests;  // Total number of requests.

    IHYDToken public tokenContract; // Reference to the HYDToken contract

    event RequestCreated(  // Event to be emitted when a new request is created.
        uint256 indexed id,
        address indexed requester,
        string companyName,
        string startDate,
        string endDate,
        string title,
        string responsibility,
        address indexed approver
    );

    event RequestApproved(uint256 indexed id);  // Event to be emitted when a request is approved.

    constructor(address tokenAddress) public {  // Constructor to set the address of the HYDToken contract
        tokenContract = IHYDToken(tokenAddress);
    }

    function createRequest(  // Function to create a new request.
        string memory companyName,
        string memory startDate,
        string memory endDate,
        string memory title,
        string memory responsibility,
        address approver
    ) public {
        require(approver != address(0), "Approver address cannot be the zero address");
        require(tokenContract.balanceOf(msg.sender) >= 1 * (10 ** uint256(18)), "Must have a token to create a request");

        Request memory newRequest = Request({ // Update mappings and increments the total number of requests.
            id: totalRequests + 1,
            companyName: companyName,
            startDate: startDate,
            endDate: endDate,
            title: title,
            responsibility: responsibility,
            approver: approver,
            status: RequestStatus.Pending
        });
        requests[msg.sender].push(newRequest); // Track requests.
        allRequests[newRequest.id] = newRequest; // Store request by ID.
        requestToRequester[newRequest.id] = msg.sender; // Map request ID to requester address
        totalRequests++;

        emit RequestCreated(  // Emit event.
            newRequest.id,
            msg.sender,
            companyName,
            startDate,
            endDate,
            title,
            responsibility,
            approver
        );
    }

    function approveRequest(uint256 requestId) public {  // Function to approve a request.
        Request storage request = allRequests[requestId];
        require(request.status == RequestStatus.Pending, "Request is not pending");
        request.status = RequestStatus.Approved; // Update the status in the allRequests mapping.

        address requester = requestToRequester[requestId]; 
        Request[] storage requesterRequests = requests[requester];
        for (uint256 i = 0; i < requesterRequests.length; i++) {  // Find the corresponding request in the requests mapping and update its status
            if (requesterRequests[i].id == requestId) {
                requesterRequests[i].status = RequestStatus.Approved;
                break;
            }
        }  
        emit RequestApproved(requestId);  // Emit event
    }

    function getRequestsByAccount(address account) public view returns (Request[] memory) {  // Function to retrieve requests by account (requester address)

        Request[] memory allRequestsForAccount = requests[account];
        uint256 approvedCount = 0;

        for (uint256 i = 0; i < allRequestsForAccount.length; i++) {  // Count the number of approved requests
            if (allRequestsForAccount[i].status == RequestStatus.Approved) {
                approvedCount++;
            }
        }

        Request[] memory approvedRequests = new Request[](approvedCount);  // Array for approved requests
        uint256 index = 0;

        for (uint256 i = 0; i < allRequestsForAccount.length; i++) {  // Add approved requests
            if (allRequestsForAccount[i].status == RequestStatus.Approved) {
                approvedRequests[index] = allRequestsForAccount[i];
                index++;
            }
        }
        
        return approvedRequests;
    }

}
