// SPDX-License-Identifier: MIT
/*                                                                                                                      
        ,----,                                                                                                 
      ,/   .`|                                                                                      ,----..    
    ,`   .'  :                                                          ,---,       ,---,          /   /   \   
  ;    ;     /                                                        .'  .' `\    '  .' \        /   .     :  
.'___,/    ,'                    ,--,  __  ,-.   ,---.              ,---.'     \  /  ;    '.     .   /   ;.  \ 
|    :     |                   ,'_ /|,' ,'/ /|  '   ,'\   .--.--.   |   |  .`\  |:  :       \   .   ;   /  ` ; 
;    |.';  ;  ,--.--.     .--. |  | :'  | |' | /   /   | /  /    '  :   : |  '  |:  |   /\   \  ;   |  ; \ ; | 
`----'  |  | /       \  ,'_ /| :  . ||  |   ,'.   ; ,. :|  :  /`./  |   ' '  ;  :|  :  ' ;.   : |   :  | ; | ' 
    '   :  ;.--.  .-. | |  ' | |  . .'  :  /  '   | |: :|  :  ;_    '   | ;  .  ||  |  ;/  \   \.   |  ' ' ' : 
    |   |  ' \__\/: . . |  | ' |  | ||  | '   '   | .; : \  \    `. |   | :  |  ''  :  | \  \ ,''   ;  \; /  | 
    '   :  | ," .--.; | :  | : ;  ; |;  : |   |   :    |  `----.   \'   : | /  ; |  |  '  '--'   \   \  ',  /  
    ;   |.' /  /  ,.  | '  :  `--'   \  , ;    \   \  /  /  /`--'  /|   | '` ,/  |  :  :          ;   :    /   
    '---'  ;  :   .'   \:  ,      .-./---'      `----'  '--'.     / ;   :  .'    |  | ,'           \   \ .'    
           |  ,     .-./ `--`----'                        `--'---'  |   ,.'      `--''              `---`     
            `--`---'                                                '---'                                    
*/ 
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


// interface Tauros {
//     function mint(address recipient, uint256 amount) external; 
// }

// interface LiquidityPool {
//     function recieveFunds(address _funder, uint256 _amount) external;
// }

contract dAIsyStaking is ERC20, ERC20Burnable,Ownable, ReentrancyGuard {
    // Staker info
    struct Staker {
        uint256 deposited;

        // Last time of details update for Deposit
        uint256 timeOfLastUpdate;

        uint256 unclaimedRewards;
    }
    using SafeMath for uint256;
    address TaurosToken;
    address liquidity;
    uint256 feePercent;

    uint256 public s_maxSupply = 10000000 * 10**decimals();
    // Rewards per hour. A fraction calculated as x/10.000.000 to get the percentage
    uint256 public rewardsPerHour = 285; // 0.00285%/h or 25% APR

    // Minimum amount to stake
    uint256 public minStake = 1000;

    // Compounding frequency limit in seconds
    uint256 public compoundFreq = 30; //30 seconds
    // uint256 public compoundFreq = 43200; //12 hours


    // Mapping of address to Staker info
    mapping(address => Staker) internal stakers;

    // Constructor function
    constructor(string memory _name, string memory _symbol)
        ERC20(_name, _symbol)
    {
        _mint(msg.sender, s_maxSupply);
    }

    function setTokenAddress(address _address) public onlyOwner {
        TaurosToken = _address;
    }

    function setFeeRecipient(address _address) public onlyOwner {
        liquidity = _address;
    }

    // If address has no Staker struct, initiate one. If address already was a stake,
    // calculate the rewards and add them to unclaimedRewards, reset the last time of
    // deposit and then add _amount to the already deposited amount.
    
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount >= minStake, "Amount smaller than minimimum deposit");
        require(
            balanceOf(msg.sender) >= _amount,
            "Can't stake more than you own"
        );
        if (stakers[msg.sender].deposited == 0) {
            stakers[msg.sender].deposited = _amount;
            stakers[msg.sender].timeOfLastUpdate = block.timestamp;
            stakers[msg.sender].unclaimedRewards = 0;
        } else {
            uint256 rewards = calculateRewards(msg.sender);
            stakers[msg.sender].unclaimedRewards += rewards;
            stakers[msg.sender].deposited += _amount;
            stakers[msg.sender].timeOfLastUpdate = block.timestamp;
        }
        _burn(msg.sender, _amount);
    }

    // Compound the rewards and reset the last time of update for deposit info
    function stakeRewards() external nonReentrant {
        require(stakers[msg.sender].deposited > 0, "You have no deposit");
        require(
            compoundRewardsTimer(msg.sender) == 0,
            "Tried to compound rewards too soon"
        );
        uint256 rewards = calculateRewards(msg.sender) +
            stakers[msg.sender].unclaimedRewards;
        stakers[msg.sender].unclaimedRewards = 0;
        stakers[msg.sender].deposited += rewards;
        stakers[msg.sender].timeOfLastUpdate = block.timestamp;
    }

    // Mints rewards for user
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender) +
            stakers[msg.sender].unclaimedRewards;
        require(rewards > 0, "You have no rewards");
        stakers[msg.sender].unclaimedRewards = 0;
        stakers[msg.sender].timeOfLastUpdate = block.timestamp;
        _mint(msg.sender, rewards);
    }

    // Withdraw specified amount of staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        require(
            stakers[msg.sender].deposited >= _amount,
            "Can't withdraw more than you have"
        );
        uint256 _rewards = calculateRewards(msg.sender);
        stakers[msg.sender].deposited -= _amount;
        stakers[msg.sender].timeOfLastUpdate = block.timestamp;
        stakers[msg.sender].unclaimedRewards = _rewards;
        _mint(msg.sender, _amount);
    }

    // Withdraw all stake and rewards and mints them to the msg.sender
    function withdrawAll() external nonReentrant {
        require(stakers[msg.sender].deposited > 0, "You have no deposit");
        uint256 _rewards = calculateRewards(msg.sender) +
            stakers[msg.sender].unclaimedRewards;
        uint256 _deposit = stakers[msg.sender].deposited;
        stakers[msg.sender].deposited = 0;
        stakers[msg.sender].timeOfLastUpdate = 0;
        uint256 _amount = _rewards + _deposit;
        _mint(msg.sender, _amount);
    }

    // Function useful for fron-end that returns user stake and rewards by address
    function getDepositInfo(address _user)
        public
        view
        returns (uint256 _stake, uint256 _rewards)
    {
        _stake = stakers[_user].deposited;
        _rewards =
            calculateRewards(_user) +
            stakers[msg.sender].unclaimedRewards;
        return (_stake, _rewards);
    }

    // Utility function that returns the timer for restaking rewards
    function compoundRewardsTimer(address _user)
        public
        view
        returns (uint256 _timer)
    {
        if (stakers[_user].timeOfLastUpdate + compoundFreq <= block.timestamp) {
            return 0;
        } else {
            return
                (stakers[_user].timeOfLastUpdate + compoundFreq) -
                block.timestamp;
        }
    }

    // Calculate the rewards since the last update on Deposit info
    function calculateRewards(address _staker)
        internal
        view
        returns (uint256 rewards)
    {
        return (((((block.timestamp - stakers[_staker].timeOfLastUpdate) *
            stakers[_staker].deposited) * rewardsPerHour) / 3600) / 10000000);
    }

    function setFeePercent(uint256 fee) public onlyOwner {
        feePercent = fee;        
    }

    function _setValues(uint256 _amount) public view returns(uint256, uint256, uint256) {
        uint256 fee = feePercent * _amount / 100;
        uint256 newValue = _amount - fee;
        uint256 tokenValue = newValue / 1e15;
        return(fee, newValue, tokenValue);
    }

  function transferFrom(address from, address to, uint256 amount) public virtual override returns (bool) { 
    uint256 percentageFee = (amount.mul(feePercent)).div(10000);
    address spender = _msgSender();
    _spendAllowance(from, spender, amount);
    uint256 total = amount.sub(percentageFee);
    // Transfer fee to liquidity
    transfer(address(liquidity), percentageFee);
    transfer(to ,total);
    return true;
  }
}
