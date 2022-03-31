-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 31. Mar, 2022 15:02 PM
-- Tjener-versjon: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ski_equipment_manufacturer`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `customer`
--

CREATE TABLE `customer` (
  `customerID` int(20) NOT NULL,
  `customerName` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `address` varchar(40) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `customer`
--

INSERT INTO `customer` (`customerID`, `customerName`, `startDate`, `endDate`, `address`) VALUES
(1, 'Sang', '2022-05-01', '2022-05-29', 'Ringkollen 1F'),
(2, 'Daniel', '2022-06-01', '2022-06-29', 'Maries vei 45'),
(3, 'Lars', '2022-07-01', '2022-07-29', 'Merkantveien xx'),
(4, 'Mats', '2022-08-01', '2022-08-29', 'Merkantveien xx');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `employee`
--

CREATE TABLE `employee` (
  `employeeNumber` int(20) NOT NULL,
  `name` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `department` varchar(40) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `employee`
--

INSERT INTO `employee` (`employeeNumber`, `name`, `department`) VALUES
(1, 'Lars', 'Sales'),
(2, 'Mats', 'Management');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `franchise`
--

CREATE TABLE `franchise` (
  `customerID` int(20) NOT NULL,
  `negotiatedPrice` varchar(60) COLLATE utf8_danish_ci NOT NULL,
  `information` varchar(200) COLLATE utf8_danish_ci DEFAULT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `orders`
--

CREATE TABLE `orders` (
  `customerID` int(20) NOT NULL,
  `orderNumber` int(20) NOT NULL,
  `quantity` int(2) NOT NULL,
  `totalPrice` int(11) NOT NULL,
  `state` enum('new','open','available','cancelled','ready','shipped') COLLATE utf8_danish_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `orders`
--

INSERT INTO `orders` (`customerID`, `orderNumber`, `quantity`, `totalPrice`, `state`, `date`) VALUES
(1, 1, 10, 1000, 'new', '2022-03-31 13:00:05'),
(1, 2, 20, 2000, 'open', '2022-03-31 13:00:05'),
(1, 3, 30, 3000, 'ready', '2022-03-31 13:00:05'),
(1, 4, 40, 4000, 'available', '2022-03-31 13:00:05'),
(2, 5, 50, 5000, 'cancelled', '2022-03-31 13:00:05'),
(2, 6, 60, 6000, 'shipped', '2022-03-31 13:00:05');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `productionplan`
--

CREATE TABLE `productionplan` (
  `employeeNumber` int(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `typeID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `productionplan`
--

INSERT INTO `productionplan` (`employeeNumber`, `quantity`, `typeID`, `startDate`, `endDate`) VALUES
(1, 1000, 1, '2022-05-01', '2022-05-29'),
(1, 1100, 2, '2022-06-01', '2022-06-29'),
(2, 1200, 1, '2022-07-01', '2022-07-29'),
(2, 1300, 2, '2022-08-01', '2022-08-29');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `shipment`
--

CREATE TABLE `shipment` (
  `shipmentNumber` int(20) NOT NULL,
  `orderNumber` int(20) NOT NULL,
  `transporterID` int(20) NOT NULL,
  `shippingAddress` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `pickUpDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `state` enum('ready','shipped') COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `shipment`
--

INSERT INTO `shipment` (`shipmentNumber`, `orderNumber`, `transporterID`, `shippingAddress`, `pickUpDate`, `state`) VALUES
(1, 3, 2, 'Ringkollen 1F', '2021-12-31 23:00:00', 'ready');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `ski`
--

CREATE TABLE `ski` (
  `productID` int(20) NOT NULL,
  `typeID` int(11) NOT NULL,
  `length` enum('142','147','152','157','162','167','172','177','182','187','192','197','202','207') COLLATE utf8_danish_ci NOT NULL,
  `reserved` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `ski`
--

INSERT INTO `ski` (`productID`, `typeID`, `length`, `reserved`) VALUES
(1, 1, '142', 0),
(2, 1, '147', 0),
(3, 1, '152', 0),
(4, 1, '157', 0),
(5, 1, '162', 0),
(6, 1, '167', 0),
(7, 1, '172', 0),
(8, 1, '177', 0),
(9, 1, '182', 0),
(10, 1, '187', 0),
(11, 1, '192', 0),
(12, 1, '197', 0),
(13, 1, '202', 0),
(14, 1, '207', 0),
(15, 2, '142', 0),
(16, 2, '147', 0),
(17, 2, '152', 0),
(18, 2, '157', 0),
(19, 2, '162', 0),
(20, 2, '167', 0),
(21, 2, '172', 0),
(22, 2, '177', 0),
(23, 2, '182', 0),
(24, 2, '187', 0),
(25, 2, '192', 0),
(26, 2, '197', 0),
(27, 2, '202', 0),
(28, 2, '207', 0);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `skitype`
--

CREATE TABLE `skitype` (
  `typeID` int(11) NOT NULL,
  `type` enum('classic','skate','doublePole') COLLATE utf8_danish_ci NOT NULL,
  `model` enum('active','activePro','endurance','intrasonic','racePro','raceSpeed','redline') COLLATE utf8_danish_ci NOT NULL,
  `description` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `historical` tinyint(1) DEFAULT NULL,
  `url` varchar(255) COLLATE utf8_danish_ci NOT NULL,
  `msrp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `skitype`
--

INSERT INTO `skitype` (`typeID`, `type`, `model`, `description`, `historical`, `url`, `msrp`) VALUES
(1, 'classic', 'activePro', 'Classic Active Pro series skii made for athletes that wants to get their socks wet!', NULL, 'https://www.xxl.no/', 1000),
(2, 'classic', 'active', 'Classic Active series skii made for athletes that wants to get their socks dry!', NULL, 'https://www.xxl.no/', 800),
(3, 'classic', 'redline', 'These are good for performance!', NULL, 'https://madshus.com/no-no/p/redline-3-0-f3', 7700),
(4, 'skate', 'active', 'These are good for stability!', NULL, 'https://madshus.com/no-no/p/nordic-pro-skin', 4000);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `store`
--

CREATE TABLE `store` (
  `customerID` int(20) NOT NULL,
  `price` int(11) NOT NULL,
  `address` varchar(30) COLLATE utf8_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `teamskier`
--

CREATE TABLE `teamskier` (
  `customerID` int(20) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `club` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `numSkis` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `transporter`
--

CREATE TABLE `transporter` (
  `transporterID` int(20) NOT NULL,
  `name` varchar(100) COLLATE utf8_danish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

--
-- Dataark for tabell `transporter`
--

INSERT INTO `transporter` (`transporterID`, `name`) VALUES
(1, 'Posten'),
(2, 'PostNord'),
(3, 'Bring');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employeeNumber`);

--
-- Indexes for table `franchise`
--
ALTER TABLE `franchise`
  ADD KEY `customerID` (`customerID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderNumber`),
  ADD KEY `customerID` (`customerID`);

--
-- Indexes for table `productionplan`
--
ALTER TABLE `productionplan`
  ADD PRIMARY KEY (`startDate`),
  ADD KEY `employeeNumber` (`employeeNumber`),
  ADD KEY `typeID` (`typeID`);

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`shipmentNumber`),
  ADD KEY `transporterID` (`transporterID`),
  ADD KEY `orderNumber` (`orderNumber`);

--
-- Indexes for table `ski`
--
ALTER TABLE `ski`
  ADD PRIMARY KEY (`productID`),
  ADD KEY `typeID` (`typeID`);

--
-- Indexes for table `skitype`
--
ALTER TABLE `skitype`
  ADD PRIMARY KEY (`typeID`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`customerID`);

--
-- Indexes for table `teamskier`
--
ALTER TABLE `teamskier`
  ADD KEY `customerID` (`customerID`);

--
-- Indexes for table `transporter`
--
ALTER TABLE `transporter`
  ADD PRIMARY KEY (`transporterID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employeeNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `shipment`
--
ALTER TABLE `shipment`
  MODIFY `shipmentNumber` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ski`
--
ALTER TABLE `ski`
  MODIFY `productID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `skitype`
--
ALTER TABLE `skitype`
  MODIFY `typeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teamskier`
--
ALTER TABLE `teamskier`
  MODIFY `customerID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transporter`
--
ALTER TABLE `transporter`
  MODIFY `transporterID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `franchise_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Begrensninger for tabell `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Begrensninger for tabell `productionplan`
--
ALTER TABLE `productionplan`
  ADD CONSTRAINT `productionplan_ibfk_1` FOREIGN KEY (`employeeNumber`) REFERENCES `employee` (`employeeNumber`),
  ADD CONSTRAINT `productionplan_ibfk_2` FOREIGN KEY (`typeID`) REFERENCES `skitype` (`typeID`);

--
-- Begrensninger for tabell `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `shipment_ibfk_1` FOREIGN KEY (`transporterID`) REFERENCES `transporter` (`transporterID`),
  ADD CONSTRAINT `shipment_ibfk_2` FOREIGN KEY (`orderNumber`) REFERENCES `orders` (`orderNumber`);

--
-- Begrensninger for tabell `ski`
--
ALTER TABLE `ski`
  ADD CONSTRAINT `ski_ibfk_1` FOREIGN KEY (`typeID`) REFERENCES `skitype` (`typeID`);

--
-- Begrensninger for tabell `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `store_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);

--
-- Begrensninger for tabell `teamskier`
--
ALTER TABLE `teamskier`
  ADD CONSTRAINT `teamskier_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
