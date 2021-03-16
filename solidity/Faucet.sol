// "SPDX-License-Identifier: UNLICENSED"
pragma solidity ^0.7.2;

contract Owned {
  address payable owner;

  constructor () {
    owner = msg.sender;
  }

  modifier onlyOwner {
    require(msg.sender == owner, "Only the contract owner can call this function");
    _;
  }
}

contract Mortal is Owned {
  function destroy() public onlyOwner {
    selfdestruct(owner);
  }
}

contract Faucet is Mortal {
  event Withdrawal(address indexed to, uint amount);
  event Deposit(address indexed from, uint amount);

  function withdraw(uint withdraw_amount) public {
    require(withdraw_amount <= 0.1 ether, "Must withdraw at most 0.1 Eth");
    require(address(this).balance >= withdraw_amount, "Insufficient ballance in faucet for withdrawal request");

    msg.sender.transfer(withdraw_amount);
    emit Withdrawal(msg.sender, withdraw_amount);
  }

  receive () external payable {
    emit Deposit(msg.sender, msg.value);
  }
}
