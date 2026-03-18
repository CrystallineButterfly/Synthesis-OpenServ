// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

import { OpenServJobBoard } from "src/OpenServJobBoard.sol";

contract Deploy is Script {
    function run() external returns (OpenServJobBoard deployed) {
        address admin = vm.envAddress("ADMIN_WALLET_ADDRESS");
        address operator = vm.envAddress("OPERATOR_WALLET_ADDRESS");

        vm.startBroadcast();
        deployed = new OpenServJobBoard(admin, operator);
        vm.stopBroadcast();

        console2.log("Deployed OpenServJobBoard at", address(deployed));
    }
}
