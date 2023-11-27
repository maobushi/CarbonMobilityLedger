// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MobilityCarbonCredit is ERC20 {
    uint256 private constant SCALE = 100; // 2桁までの小数を扱う
    uint256 constant RR = 1; // 車購入時のリターン率
    uint256 constant CR = 100; // 充電レベルの比率
    uint256 constant DR = 10; // 走行キロメーターの比率
    uint256 constant LR = 10; // レベルアップの比率

    mapping(address => uint256) private carLevel;
    mapping(address => uint256) private totalDistanceDriven;

    event CarPurchased(address indexed user, uint256 amount);
    event BatteryCharged(address indexed user, uint256 amount);
    event CarDriven(address indexed user, uint256 distance);
    event TreePlanted(address indexed user, uint256 amount);
    event Summary(address indexed user, uint256 totalBalance, uint256 totalCarLevel, uint256 totalDistance);

    constructor(uint256 initialSupply) ERC20("CarBon Token", "CBT") {
        _mint(msg.sender, initialSupply);
        carLevel[msg.sender] = 1;
    }

    function buyCar(uint256 yenAmount) public {
        // 日本円での価格の1%をCBTとして計算
        // 100円で1 CBTが付与されるようにする
        uint256 cbtAmount = yenAmount / 100;

        // CBTの量をトークンの最小単位（Wei単位）に変換
        // 1 CBT = 1e18 Wei
        cbtAmount = cbtAmount * 1e18;

        // CBTをユーザーに付与
        _mint(msg.sender, cbtAmount);
        emit CarPurchased(msg.sender, cbtAmount);
        emitSummary();
    }

    function chargeBattery(uint256 getAmount, uint256 useAmount) public {
        uint256 cbtAmount = ((getAmount * CR * carLevel[msg.sender])* 1e18) / SCALE;
        _burn(msg.sender, useAmount);
        _mint(msg.sender, cbtAmount);
        emit BatteryCharged(msg.sender, cbtAmount);
        emitSummary();
    }

    function driveCar(uint256 distance) public {
        uint256 cbtAmount = ((distance * DR * carLevel[msg.sender])* 1e18) / SCALE;
        totalDistanceDriven[msg.sender] += distance;
        _mint(msg.sender, cbtAmount);
        emit CarDriven(msg.sender, distance);
        emitSummary();
    }

    function plantTree(uint256 amount) public {
        _burn(msg.sender, amount);
        uint256 levelIncrease = ((amount * LR)** 1e18) / SCALE;
        carLevel[msg.sender] += levelIncrease;
        emit TreePlanted(msg.sender, amount);
        emitSummary();
    }   
     function getDistance(address user) public view returns (uint256) {
        return totalDistanceDriven[user];
    }


    function getCarLevel(address user) public view returns (uint256) {
        return carLevel[user];
    }

    function emitSummary() internal {
        emit Summary(msg.sender, balanceOf(msg.sender), carLevel[msg.sender], totalDistanceDriven[msg.sender]);
    }
}
