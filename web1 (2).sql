-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 29, 2024 at 04:30 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `web1`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id_category` int NOT NULL,
  `name_category` enum('Samsung','Vivo','Aple','Oppo','Xiaomi') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id_category`, `name_category`) VALUES
(1, 'Samsung'),
(2, 'Vivo'),
(3, 'Aple'),
(4, 'Oppo'),
(5, 'Xiaomi');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int NOT NULL,
  `name_product` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `image_url` text COLLATE utf8mb4_general_ci,
  `price` int DEFAULT NULL,
  `category` int DEFAULT NULL,
  `in_stok` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name_product`, `image_url`, `price`, `category`, `in_stok`) VALUES
(1, 'samsung a55', 'https://th.bing.com/th/id/OIP.CEQRCq9V6bw9LHvRzJimxAHaHa?w=500&h=500&rs=1&pid=ImgDetMain', 6000000, 1, 1),
(2, 'Samsung a36', 'https://i.pinimg.com/736x/2f/4a/d3/2f4ad34255f58ce1776daa04f0f6082d.jpg', 4500000, 1, 1),
(3, 'Samsung S24Fe', 'https://specs-arena.com/wp-content/uploads/2023/10/Samsung-Galaxy-S23-FE.webp', 9999999, 1, 1),
(4, 'iphone', 'https://th.bing.com/th?id=OIP.qxiJUlU01vlJelLFKto6FgHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2', 1000, 3, 1),
(5, 'Vivo V40', 'https://th.bing.com/th/id/OIP.RQKPNgYyxgp2tRJ3mCRLiQHaHa?w=800&h=800&rs=1&pid=ImgDetMain', 6000000, 2, 1),
(6, 'iPhone 11 inter ', 'https://th.bing.com/th/id/OIP.sWsELwxNHn-BMfkDhimvPgHaHa?w=175&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7', 3500000, 3, 1),
(7, 'iPhone Xr Inter', 'https://cdn.movertix.com/media/catalog/product/cache/image/1200x/a/p/apple-iphone-xr-128-gb-rojo-0190198773227.jpg', 2500000, 3, 1),
(8, 'Redmi Not 13 Pro', 'https://techcart.com.au/wp-content/uploads/2024/01/76661-Redmi-Note-13-Pro-5G-512GB12GB-Aurora-Purple-Global-Version-550x550.png', 3000000, 5, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id_category`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id_category` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
