-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Des 2024 pada 08.18
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `idea_distro`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang`
--

CREATE TABLE `barang` (
  `ID_Barang` varchar(12) NOT NULL,
  `Nama_Barang` varchar(255) NOT NULL,
  `Type_Barang` varchar(255) NOT NULL,
  `Harga` int(12) NOT NULL,
  `Stock` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `barang`
--

INSERT INTO `barang` (`ID_Barang`, `Nama_Barang`, `Type_Barang`, `Harga`, `Stock`) VALUES
('A001', 'Curved Long Tee', 'T-Shirt', 85000, 7),
('A002', 'Polo', 'T-Shirt', 90000, 0),
('A003', 'V-Neck Standard', 'T-Shirt', 75000, 8),
('B001', 'Aged Canvas', 'Outterwear', 150000, 19),
('B002', 'Nylon Work Jacket', 'Outterwear', 175000, 15),
('B003', 'Waterproof Tech Zip Jacket', 'Outterwear', 200000, 10),
('C001', 'Double Knee Work Pants', 'Bottoms', 130000, 13),
('C002', 'Lounge Pants', 'Bottoms', 100000, 10),
('C003', 'Cargo Pants', 'Bottoms', 125000, 15),
('D001', 'New Era Tucker Hat', 'Accessories', 90000, 8),
('D002', 'Logo Beanie Hat', 'Accessories', 85000, 10),
('D003', 'Holster Bag', 'Accessories', 75000, 18);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pegawai`
--

CREATE TABLE `pegawai` (
  `ID_Pegawai` int(11) NOT NULL,
  `Nama_Pegawai` varchar(255) NOT NULL,
  `Alamat` varchar(255) NOT NULL,
  `No_Tlp` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pegawai`
--

INSERT INTO `pegawai` (`ID_Pegawai`, `Nama_Pegawai`, `Alamat`, `No_Tlp`) VALUES
(230705189, 'M Farfi Artila', 'Blang Krueng', '2147483647'),
(230705134, 'Mithzia Ahza Imanullah', 'Kuta Alam', '628127383295'),
(230705144, 'Imam Syuja', 'Beurawe', '628136078586'),
(230705165, 'Muzakir', 'Labui', '2147483647');

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `ID_Transaksi` varchar(12) NOT NULL,
  `ID_Barang` varchar(12) NOT NULL,
  `Jumlah` int(11) NOT NULL,
  `Harga_Satuan` int(12) NOT NULL,
  `Total_Harga` int(12) NOT NULL,
  `Tanggal` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`ID_Transaksi`, `ID_Barang`, `Jumlah`, `Harga_Satuan`, `Total_Harga`, `Tanggal`) VALUES
('T001', 'A002', 3, 90000, 270000, '2024-12-16 14:25:58'),
('T002', 'D001', 1, 90000, 90000, '2024-12-16 14:33:46'),
('T003', 'B001', 1, 150000, 150000, '2024-12-16 14:36:21'),
('T004', 'D003', 7, 75000, 525000, '2024-12-16 14:40:00'),
('T005', 'B002', 1, 175000, 175000, '2024-12-16 14:42:16'),
('T006', 'B002', 2, 175000, 350000, '2024-12-17 02:32:15'),
('T007', 'D001', 4, 90000, 360000, '2024-12-17 02:39:53'),
('T008', 'B003', 2, 200000, 400000, '2024-12-17 02:41:12'),
('T009', 'A002', 2, 90000, 180000, '2024-12-17 02:44:10'),
('T010', 'A002', 2, 90000, 180000, '2024-12-18 08:54:26'),
('T011', 'A001', 3, 85000, 255000, '2024-12-18 08:55:50'),
('T012', 'C001', 2, 130000, 260000, '2024-12-18 09:03:28'),
('T013', 'A001', 3, 85000, 255000, '2024-12-18 09:13:55'),
('T014', 'C001', 2, 130000, 260000, '2024-12-18 09:19:39'),
('T015', 'A003', 2, 75000, 150000, '2024-12-18 09:21:47'),
('T016', 'C003', 2, 125000, 250000, '2024-12-18 09:26:31'),
('T017', 'C003', 2, 125000, 250000, '2024-12-18 09:27:41'),
('T018', 'D001', 2, 90000, 180000, '2024-12-18 09:29:36'),
('T019', 'D003', 2, 75000, 150000, '2024-12-18 09:37:03');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`ID_Barang`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`ID_Transaksi`),
  ADD KEY `ID_Barang` (`ID_Barang`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`ID_Barang`) REFERENCES `barang` (`ID_Barang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
