-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-11-2024 a las 16:25:13
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_final_practicas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funciones`
--

CREATE TABLE `funciones` (
  `IdFunciones` int(11) NOT NULL,
  `IdPelicula` int(11) DEFAULT NULL,
  `Fecha_hora` datetime DEFAULT NULL,
  `IdSala` int(11) DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `funciones`
--

INSERT INTO `funciones` (`IdFunciones`, `IdPelicula`, `Fecha_hora`, `IdSala`, `Precio`) VALUES
(2, NULL, '2024-11-05 17:00:00', 2, 1000.00),
(3, NULL, '2024-11-06 11:00:00', 1, 1000.00),
(4, NULL, '2024-11-09 11:00:00', 1, 1.00),
(5, NULL, '2024-11-07 11:00:00', 1, 1000.00),
(6, 6, '2024-11-11 14:00:00', 1, 3000.00),
(7, 5, '2024-11-11 14:00:00', 2, 3500.00),
(8, 8, '2024-11-12 17:00:00', 1, 1500.00),
(9, 8, '2024-11-12 11:00:00', 1, 10000.00),
(10, 5, '2024-11-20 14:00:00', 2, 15000.00),
(11, 5, '2024-11-20 11:00:00', 1, 2000.00),
(12, 9, '2024-11-20 17:00:00', 1, 1500.00),
(13, 6, '2024-11-22 17:00:00', 2, 10000.00),
(14, 10, '2024-11-27 14:00:00', 1, 1500.00),
(15, 12, '2024-11-27 11:00:00', 2, 1500.00),
(16, 8, '2024-11-27 14:00:00', 2, 1500.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generos`
--

CREATE TABLE `generos` (
  `IdGeneros` int(11) NOT NULL,
  `NombreGenero` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `generos`
--

INSERT INTO `generos` (`IdGeneros`, `NombreGenero`) VALUES
(1, 'Acción'),
(2, 'Aventura'),
(3, 'Animación'),
(4, 'Biografía'),
(5, 'Comedia'),
(6, 'Crimen'),
(7, 'Documental'),
(8, 'Drama'),
(9, 'Familia'),
(10, 'Fantasía'),
(11, 'Historia'),
(12, 'Horror'),
(13, 'Misterio'),
(14, 'Musical'),
(15, 'Romance'),
(16, 'Ciencia Ficción'),
(17, 'Deportes'),
(18, 'Suspenso'),
(19, 'Guerra'),
(20, 'Western');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

CREATE TABLE `historial` (
  `IdHistorial` int(11) NOT NULL,
  `IdUsuario` int(11) DEFAULT NULL,
  `Fecha_Hora` datetime DEFAULT NULL,
  `Accion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `historial`
--

INSERT INTO `historial` (`IdHistorial`, `IdUsuario`, `Fecha_Hora`, `Accion`) VALUES
(1, NULL, '2024-11-04 09:57:36', 'Elimino un Usuario'),
(2, NULL, '2024-11-04 09:57:52', 'Creo un Usuario'),
(3, 2, '2024-11-04 09:58:31', 'Inicio Sesion'),
(4, 2, '2024-11-04 10:06:07', 'Inicio Sesion'),
(5, 2, '2024-11-04 10:07:10', 'Creo una Pelicula'),
(6, 2, '2024-11-04 10:10:59', 'Inicio Sesion'),
(7, 2, '2024-11-04 10:11:28', 'Agrego una Funcion'),
(8, 2, '2024-11-04 10:12:11', 'Vendio una Entrada/s'),
(9, 2, '2024-11-04 18:37:14', 'Inicio Sesion'),
(10, 2, '2024-11-04 18:38:35', 'Agrego una Funcion'),
(11, 2, '2024-11-04 18:39:12', 'Vendio una Entrada/s'),
(12, 2, '2024-11-04 18:39:23', 'Vendio una Entrada/s'),
(13, 2, '2024-11-04 18:40:30', 'Inicio Sesion'),
(14, 2, '2024-11-04 18:41:24', 'Creo una Pelicula'),
(15, 2, '2024-11-04 18:47:48', 'Inicio Sesion'),
(16, 2, '2024-11-04 18:49:13', 'Inicio Sesion'),
(17, 2, '2024-11-04 18:51:35', 'Inicio Sesion'),
(18, 2, '2024-11-05 16:28:07', 'Inicio Sesion'),
(19, 2, '2024-11-05 22:17:44', 'Inicio Sesion'),
(20, 2, '2024-11-05 22:17:54', 'Modifico una Funcion'),
(21, 2, '2024-11-05 22:24:27', 'Inicio Sesion'),
(22, 2, '2024-11-05 22:26:17', 'Inicio Sesion'),
(23, 2, '2024-11-05 22:29:19', 'Inicio Sesion'),
(24, 2, '2024-11-05 22:31:44', 'Inicio Sesion'),
(25, 2, '2024-11-05 22:33:21', 'Inicio Sesion'),
(26, 2, '2024-11-05 22:41:24', 'Inicio Sesion'),
(27, 2, '2024-11-05 22:41:37', 'Modifico Una Pelicula'),
(28, 2, '2024-11-05 22:42:56', 'Inicio Sesion'),
(29, 2, '2024-11-05 22:43:12', 'Modifico Una Pelicula'),
(30, 2, '2024-11-05 22:43:38', 'Inicio Sesion'),
(31, 2, '2024-11-05 22:45:21', 'Inicio Sesion'),
(32, 2, '2024-11-05 22:47:15', 'Creo un Usuario'),
(33, 2, '2024-11-05 22:47:23', 'Modifico un Usuario'),
(34, 2, '2024-11-05 22:47:37', 'Modifico un Usuario'),
(35, 2, '2024-11-05 22:47:41', 'Elimino un Usuario'),
(36, 2, '2024-11-06 08:41:59', 'Inicio Sesion'),
(37, 2, '2024-11-06 08:48:57', 'Inicio Sesion'),
(38, 2, '2024-11-06 08:49:14', 'Inicio Sesion'),
(39, 2, '2024-11-06 08:54:29', 'Inicio Sesion'),
(40, 2, '2024-11-06 08:55:51', 'Inicio Sesion'),
(41, 2, '2024-11-06 08:57:22', 'Inicio Sesion'),
(42, 2, '2024-11-06 09:02:24', 'Inicio Sesion'),
(43, 2, '2024-11-06 09:04:52', 'Inicio Sesion'),
(44, 2, '2024-11-06 09:05:38', 'Agrego una Funcion'),
(45, 2, '2024-11-06 09:49:29', 'Inicio Sesion'),
(46, 2, '2024-11-06 09:51:35', 'Inicio Sesion'),
(47, 2, '2024-11-06 09:54:30', 'Inicio Sesion'),
(48, 2, '2024-11-06 09:55:08', 'Elimino una Pelicula'),
(49, 2, '2024-11-06 09:55:11', 'Elimino una Pelicula'),
(50, 2, '2024-11-06 09:55:51', 'Creo una Pelicula'),
(51, 2, '2024-11-06 09:56:13', 'Modifico una Funcion'),
(52, 2, '2024-11-06 09:56:54', 'Inicio Sesion'),
(53, 2, '2024-11-06 09:57:15', 'Inicio Sesion'),
(54, 2, '2024-11-06 10:58:31', 'Inicio Sesion'),
(55, 2, '2024-11-06 10:58:50', 'Agrego una Funcion'),
(56, 2, '2024-11-06 10:59:17', 'Creo un Usuario'),
(57, 2, '2024-11-06 10:59:27', 'Modifico un Usuario'),
(58, 2, '2024-11-06 10:59:34', 'Elimino un Usuario'),
(59, 2, '2024-11-06 10:59:48', 'Elimino una Pelicula'),
(60, 2, '2024-11-06 11:00:19', 'Creo una Pelicula'),
(61, 2, '2024-11-06 11:00:42', 'Modifico una Funcion'),
(62, 2, '2024-11-06 11:01:12', 'Inicio Sesion'),
(63, 2, '2024-11-06 11:01:56', 'Inicio Sesion'),
(64, 2, '2024-11-06 11:17:08', 'Inicio Sesion'),
(65, 2, '2024-11-06 11:24:22', 'Inicio Sesion'),
(66, 2, '2024-11-06 11:25:10', 'Inicio Sesion'),
(67, 2, '2024-11-06 11:26:24', 'Inicio Sesion'),
(68, 2, '2024-11-06 11:26:38', 'Inicio Sesion'),
(69, 2, '2024-11-06 11:27:48', 'Inicio Sesion'),
(70, 2, '2024-11-06 11:33:37', 'Inicio Sesion'),
(71, 2, '2024-11-06 11:37:27', 'Inicio Sesion'),
(72, 2, '2024-11-06 11:39:38', 'Inicio Sesion'),
(73, 2, '2024-11-06 11:45:16', 'Inicio Sesion'),
(74, 2, '2024-11-06 11:50:58', 'Inicio Sesion'),
(75, 2, '2024-11-06 11:51:45', 'Inicio Sesion'),
(76, 2, '2024-11-06 11:52:43', 'Inicio Sesion'),
(77, 2, '2024-11-06 11:54:33', 'Inicio Sesion'),
(78, 2, '2024-11-06 11:55:23', 'Inicio Sesion'),
(79, 2, '2024-11-06 11:56:23', 'Inicio Sesion'),
(80, 2, '2024-11-06 11:58:01', 'Inicio Sesion'),
(81, 2, '2024-11-06 12:03:17', 'Inicio Sesion'),
(82, 2, '2024-11-06 12:04:11', 'Inicio Sesion'),
(83, 2, '2024-11-06 12:05:25', 'Inicio Sesion'),
(84, 2, '2024-11-06 12:08:30', 'Inicio Sesion'),
(85, 2, '2024-11-06 12:09:17', 'Inicio Sesion'),
(86, 2, '2024-11-06 12:10:52', 'Inicio Sesion'),
(87, 2, '2024-11-06 12:12:41', 'Inicio Sesion'),
(88, 2, '2024-11-06 12:15:00', 'Inicio Sesion'),
(89, 2, '2024-11-06 12:15:39', 'Inicio Sesion'),
(90, 2, '2024-11-06 12:18:50', 'Inicio Sesion'),
(91, 2, '2024-11-06 12:19:17', 'Inicio Sesion'),
(92, 2, '2024-11-06 12:19:57', 'Elimino una Funcion'),
(93, 2, '2024-11-06 12:20:36', 'Inicio Sesion'),
(94, 2, '2024-11-06 12:20:54', 'Agrego una Funcion'),
(95, 2, '2024-11-06 12:21:36', 'Inicio Sesion'),
(96, 2, '2024-11-06 12:24:30', 'Inicio Sesion'),
(97, 2, '2024-11-06 12:26:37', 'Inicio Sesion'),
(98, 2, '2024-11-06 16:31:17', 'Inicio Sesion'),
(99, 2, '2024-11-06 16:34:56', 'Vendio una Entrada/s'),
(100, 2, '2024-11-06 16:35:04', 'Vendio una Entrada/s'),
(101, 2, '2024-11-11 10:49:45', 'Inicio Sesion'),
(102, 2, '2024-11-11 10:53:47', 'Inicio Sesion'),
(103, 2, '2024-11-11 10:54:59', 'Creo una Pelicula'),
(104, 2, '2024-11-11 10:57:07', 'Creo una Pelicula'),
(105, 2, '2024-11-11 10:58:43', 'Creo una Pelicula'),
(106, 2, '2024-11-11 10:59:07', 'Modifico Una Pelicula'),
(107, 2, '2024-11-11 11:03:11', 'Agrego una Funcion'),
(108, 2, '2024-11-11 11:04:01', 'Agrego una Funcion'),
(109, 2, '2024-11-11 11:04:44', 'Vendio una Entrada/s'),
(110, 2, '2024-11-11 11:04:58', 'Vendio una Entrada/s'),
(111, 2, '2024-11-11 11:07:18', 'Inicio Sesion'),
(112, 2, '2024-11-11 11:07:31', 'Vendio una Entrada/s'),
(113, 2, '2024-11-11 11:07:54', 'Vendio una Entrada/s'),
(114, 2, '2024-11-11 11:11:57', 'Inicio Sesion'),
(115, 2, '2024-11-11 11:12:08', 'Vendio una Entrada/s'),
(116, 2, '2024-11-11 11:12:20', 'Vendio una Entrada/s'),
(117, 2, '2024-11-11 11:15:58', 'Inicio Sesion'),
(118, 2, '2024-11-11 11:16:06', 'Vendio una Entrada/s'),
(119, 2, '2024-11-11 11:16:33', 'Vendio una Entrada/s'),
(120, 2, '2024-11-11 11:20:05', 'Inicio Sesion'),
(121, 2, '2024-11-11 11:26:12', 'Inicio Sesion'),
(122, 2, '2024-11-11 11:29:39', 'Inicio Sesion'),
(123, 2, '2024-11-11 11:31:05', 'Inicio Sesion'),
(124, 2, '2024-11-11 11:41:19', 'Inicio Sesion'),
(125, 2, '2024-11-11 11:41:48', 'Inicio Sesion'),
(126, 2, '2024-11-11 11:42:46', 'Inicio Sesion'),
(127, 2, '2024-11-11 12:16:14', 'Inicio Sesion'),
(128, 2, '2024-11-11 12:19:17', 'Inicio Sesion'),
(129, 2, '2024-11-11 12:21:48', 'Inicio Sesion'),
(130, 2, '2024-11-11 12:24:55', 'Inicio Sesion'),
(131, 2, '2024-11-11 12:26:07', 'Inicio Sesion'),
(132, 2, '2024-11-11 12:28:38', 'Inicio Sesion'),
(133, 2, '2024-11-11 12:29:10', 'Inicio Sesion'),
(134, 2, '2024-11-11 12:30:59', 'Inicio Sesion'),
(135, 2, '2024-11-11 12:33:44', 'Inicio Sesion'),
(136, 2, '2024-11-11 12:37:25', 'Inicio Sesion'),
(137, 2, '2024-11-11 12:45:16', 'Inicio Sesion'),
(138, 2, '2024-11-12 20:17:10', 'Inicio Sesion'),
(139, 2, '2024-11-12 20:39:03', 'Inicio Sesion'),
(140, 2, '2024-11-12 20:39:59', 'Inicio Sesion'),
(141, 2, '2024-11-12 20:42:15', 'Inicio Sesion'),
(142, 2, '2024-11-12 20:46:20', 'Creo una Pelicula'),
(143, 2, '2024-11-12 20:50:03', 'Inicio Sesion'),
(144, 2, '2024-11-12 20:50:17', 'Elimino una Pelicula'),
(145, 2, '2024-11-12 20:51:47', 'Inicio Sesion'),
(146, 2, '2024-11-12 20:52:07', 'Agrego una Funcion'),
(147, 2, '2024-11-12 20:52:36', 'Vendio una Entrada/s'),
(148, 2, '2024-11-12 20:53:00', 'Agrego una Funcion'),
(149, 2, '2024-11-12 20:53:20', 'Vendio una Entrada/s'),
(150, 2, '2024-11-12 21:22:04', 'Inicio Sesion'),
(151, 2, '2024-11-12 21:23:08', 'Inicio Sesion'),
(152, 2, '2024-11-12 21:24:35', 'Inicio Sesion'),
(153, 2, '2024-11-12 21:36:07', 'Inicio Sesion'),
(154, 2, '2024-11-12 21:39:05', 'Inicio Sesion'),
(155, 2, '2024-11-12 21:43:26', 'Inicio Sesion'),
(156, 2, '2024-11-13 10:13:41', 'Inicio Sesion'),
(157, 2, '2024-11-15 09:44:12', 'Inicio Sesion'),
(158, 2, '2024-11-15 09:55:30', 'Inicio Sesion'),
(159, 2, '2024-11-15 10:11:17', 'Inicio Sesion'),
(160, 2, '2024-11-15 10:15:24', 'Inicio Sesion'),
(161, 2, '2024-11-15 10:17:07', 'Inicio Sesion'),
(162, 2, '2024-11-15 10:17:41', 'Inicio Sesion'),
(163, 2, '2024-11-15 10:27:39', 'Inicio Sesion'),
(164, 2, '2024-11-15 10:31:13', 'Inicio Sesion'),
(165, 2, '2024-11-15 10:40:08', 'Inicio Sesion'),
(166, 2, '2024-11-15 10:44:15', 'Inicio Sesion'),
(167, 2, '2024-11-15 10:46:00', 'Inicio Sesion'),
(168, 2, '2024-11-15 10:51:31', 'Inicio Sesion'),
(169, 2, '2024-11-15 11:47:28', 'Inicio Sesion'),
(170, 2, '2024-11-20 10:25:15', 'Inicio Sesion'),
(171, 2, '2024-11-20 10:38:23', 'Inicio Sesion'),
(172, 2, '2024-11-20 10:47:08', 'Inicio Sesion'),
(173, 2, '2024-11-20 10:51:30', 'Inicio Sesion'),
(174, 2, '2024-11-20 10:58:08', 'Inicio Sesion'),
(175, 2, '2024-11-20 11:09:54', 'Inicio Sesion'),
(176, 2, '2024-11-20 11:14:36', 'Inicio Sesion'),
(177, 2, '2024-11-20 11:15:51', 'Inicio Sesion'),
(178, 2, '2024-11-20 11:18:59', 'Inicio Sesion'),
(179, 2, '2024-11-20 11:23:44', 'Inicio Sesion'),
(180, 2, '2024-11-20 11:32:38', 'Inicio Sesion'),
(181, 2, '2024-11-20 11:33:13', 'Inicio Sesion'),
(182, 2, '2024-11-20 11:33:41', 'Inicio Sesion'),
(183, 2, '2024-11-20 11:36:33', 'Inicio Sesion'),
(184, 2, '2024-11-20 11:39:48', 'Inicio Sesion'),
(185, 2, '2024-11-20 11:40:18', 'Elimino una Pelicula'),
(186, 2, '2024-11-20 11:43:18', 'Inicio Sesion'),
(187, 2, '2024-11-20 11:44:23', 'Inicio Sesion'),
(188, 2, '2024-11-20 11:45:28', 'Inicio Sesion'),
(189, 2, '2024-11-20 11:47:51', 'Inicio Sesion'),
(190, 2, '2024-11-20 11:55:27', 'Inicio Sesion'),
(191, 2, '2024-11-20 11:56:15', 'Inicio Sesion'),
(192, 2, '2024-11-20 11:56:48', 'Inicio Sesion'),
(193, 2, '2024-11-20 11:57:57', 'Inicio Sesion'),
(194, 2, '2024-11-20 12:02:26', 'Inicio Sesion'),
(195, 2, '2024-11-20 12:05:21', 'Inicio Sesion'),
(196, 2, '2024-11-20 12:07:56', 'Inicio Sesion'),
(197, 2, '2024-11-20 12:08:44', 'Agrego una Funcion'),
(198, 2, '2024-11-20 12:09:15', 'Vendio una Entrada/s'),
(199, 2, '2024-11-20 12:23:35', 'Inicio Sesion'),
(200, 2, '2024-11-20 12:24:07', 'Agrego una Funcion'),
(201, 2, '2024-11-20 12:24:34', 'Vendio una Entrada/s'),
(202, 2, '2024-11-20 12:27:59', 'Creo una Pelicula'),
(203, 2, '2024-11-20 12:30:48', 'Agrego una Funcion'),
(204, 2, '2024-11-20 12:31:03', 'Vendio una Entrada/s'),
(205, 2, '2024-11-20 12:31:37', 'Vendio una Entrada/s'),
(206, 2, '2024-11-20 12:37:34', 'Inicio Sesion'),
(207, 2, '2024-11-20 12:46:10', 'Inicio Sesion'),
(208, 2, '2024-11-20 12:47:54', 'Inicio Sesion'),
(209, 2, '2024-11-20 12:51:51', 'Inicio Sesion'),
(210, 2, '2024-11-20 12:56:34', 'Inicio Sesion'),
(211, 2, '2024-11-20 13:00:44', 'Inicio Sesion'),
(212, 2, '2024-11-21 10:20:05', 'Inicio Sesion'),
(213, 2, '2024-11-21 10:23:24', 'Creo un Usuario'),
(214, 2, '2024-11-21 10:25:53', 'Elimino un Usuario'),
(215, 2, '2024-11-21 10:26:47', 'Inicio Sesion'),
(216, 2, '2024-11-21 11:16:23', 'Inicio Sesion'),
(217, 2, '2024-11-21 11:17:21', 'Inicio Sesion'),
(218, 2, '2024-11-21 11:18:17', 'Inicio Sesion'),
(219, 2, '2024-11-21 11:23:54', 'Inicio Sesion'),
(220, 2, '2024-11-21 11:25:50', 'Inicio Sesion'),
(221, 2, '2024-11-21 11:29:21', 'Inicio Sesion'),
(222, 2, '2024-11-21 11:32:03', 'Inicio Sesion'),
(223, 2, '2024-11-21 11:35:17', 'Inicio Sesion'),
(224, 2, '2024-11-21 11:40:54', 'Inicio Sesion'),
(225, 2, '2024-11-21 11:45:44', 'Inicio Sesion'),
(226, 2, '2024-11-21 11:48:50', 'Inicio Sesion'),
(227, 2, '2024-11-21 11:53:45', 'Inicio Sesion'),
(228, 2, '2024-11-21 12:01:25', 'Inicio Sesion'),
(229, 2, '2024-11-21 12:05:22', 'Inicio Sesion'),
(230, 2, '2024-11-21 12:09:05', 'Inicio Sesion'),
(231, 2, '2024-11-21 12:11:08', 'Inicio Sesion'),
(232, 2, '2024-11-21 12:14:42', 'Inicio Sesion'),
(233, 2, '2024-11-21 12:16:21', 'Inicio Sesion'),
(234, 2, '2024-11-21 16:59:15', 'Inicio Sesion'),
(235, 2, '2024-11-21 17:04:52', 'Inicio Sesion'),
(236, 2, '2024-11-22 09:41:43', 'Inicio Sesion'),
(237, 2, '2024-11-22 10:59:43', 'Inicio Sesion'),
(238, 2, '2024-11-22 11:00:27', 'Inicio Sesion'),
(239, 2, '2024-11-22 11:00:48', 'Inicio Sesion'),
(240, 2, '2024-11-22 11:01:22', 'Inicio Sesion'),
(241, 2, '2024-11-22 11:09:56', 'Inicio Sesion'),
(242, 2, '2024-11-22 11:10:59', 'Inicio Sesion'),
(243, 2, '2024-11-22 11:11:32', 'Inicio Sesion'),
(244, 2, '2024-11-22 11:13:23', 'Inicio Sesion'),
(245, 2, '2024-11-22 11:15:35', 'Inicio Sesion'),
(246, 2, '2024-11-22 11:17:10', 'Inicio Sesion'),
(247, 2, '2024-11-22 11:17:53', 'Inicio Sesion'),
(248, 2, '2024-11-22 11:18:32', 'Inicio Sesion'),
(249, 2, '2024-11-22 11:20:14', 'Inicio Sesion'),
(250, 2, '2024-11-22 11:21:27', 'Inicio Sesion'),
(251, 2, '2024-11-22 11:39:40', 'Inicio Sesion'),
(252, 2, '2024-11-22 11:44:58', 'Inicio Sesion'),
(253, 2, '2024-11-22 11:46:36', 'Inicio Sesion'),
(254, 2, '2024-11-22 11:48:23', 'Inicio Sesion'),
(255, 2, '2024-11-22 11:49:50', 'Inicio Sesion'),
(256, 2, '2024-11-22 11:50:57', 'Inicio Sesion'),
(257, 2, '2024-11-22 11:54:29', 'Inicio Sesion'),
(258, 2, '2024-11-22 11:55:48', 'Agrego una Funcion'),
(259, 2, '2024-11-22 11:56:06', 'Vendio una Entrada/s'),
(260, 2, '2024-11-22 11:56:48', 'Inicio Sesion'),
(261, 2, '2024-11-22 12:46:03', 'Inicio Sesion'),
(262, 2, '2024-11-22 12:51:40', 'Inicio Sesion'),
(263, 2, '2024-11-22 13:07:46', 'Inicio Sesion'),
(264, 2, '2024-11-22 13:12:48', 'Inicio Sesion'),
(265, 2, '2024-11-22 13:15:58', 'Inicio Sesion'),
(266, 2, '2024-11-22 13:20:49', 'Inicio Sesion'),
(267, 2, '2024-11-22 13:25:00', 'Inicio Sesion'),
(268, 2, '2024-11-22 13:25:38', 'Inicio Sesion'),
(269, 2, '2024-11-22 13:26:21', 'Inicio Sesion'),
(270, 2, '2024-11-22 13:27:21', 'Inicio Sesion'),
(271, 2, '2024-11-22 13:32:13', 'Inicio Sesion'),
(272, 2, '2024-11-22 13:32:58', 'Inicio Sesion'),
(273, 2, '2024-11-24 17:12:04', 'Inicio Sesion'),
(274, 2, '2024-11-24 17:13:40', 'Inicio Sesion'),
(275, 2, '2024-11-24 17:19:09', 'Inicio Sesion'),
(276, 2, '2024-11-24 17:22:58', 'Inicio Sesion'),
(277, 2, '2024-11-24 17:23:47', 'Inicio Sesion'),
(278, 2, '2024-11-24 17:32:26', 'Inicio Sesion'),
(279, 2, '2024-11-24 17:32:57', 'Creo un Usuario'),
(280, 2, '2024-11-24 17:36:58', 'Inicio Sesion'),
(281, 2, '2024-11-24 17:38:29', 'Inicio Sesion'),
(282, 2, '2024-11-24 17:47:54', 'Inicio Sesion'),
(283, 2, '2024-11-24 17:53:14', 'Inicio Sesion'),
(284, 2, '2024-11-24 17:56:01', 'Inicio Sesion'),
(285, 2, '2024-11-24 17:59:49', 'Inicio Sesion'),
(286, 2, '2024-11-24 18:04:32', 'Inicio Sesion'),
(287, 2, '2024-11-24 18:09:00', 'Inicio Sesion'),
(288, 2, '2024-11-24 18:12:17', 'Inicio Sesion'),
(289, 2, '2024-11-24 18:14:25', 'Inicio Sesion'),
(290, 2, '2024-11-24 18:16:19', 'Inicio Sesion'),
(291, 2, '2024-11-24 18:19:05', 'Inicio Sesion'),
(292, 2, '2024-11-24 18:20:37', 'Inicio Sesion'),
(293, 2, '2024-11-24 18:28:57', 'Inicio Sesion'),
(294, 2, '2024-11-24 18:31:20', 'Inicio Sesion'),
(295, 2, '2024-11-24 18:37:03', 'Inicio Sesion'),
(296, 2, '2024-11-24 18:39:16', 'Inicio Sesion'),
(297, 2, '2024-11-24 18:41:33', 'Inicio Sesion'),
(298, 2, '2024-11-24 18:42:06', 'Inicio Sesion'),
(299, 2, '2024-11-24 18:46:36', 'Inicio Sesion'),
(300, 2, '2024-11-24 18:50:38', 'Inicio Sesion'),
(301, 2, '2024-11-24 18:52:47', 'Inicio Sesion'),
(302, 2, '2024-11-24 19:57:18', 'Inicio Sesion'),
(303, 2, '2024-11-24 19:59:17', 'Inicio Sesion'),
(304, 2, '2024-11-24 20:00:34', 'Inicio Sesion'),
(305, 2, '2024-11-24 20:01:39', 'Inicio Sesion'),
(306, 2, '2024-11-24 20:04:33', 'Inicio Sesion'),
(307, 2, '2024-11-24 20:16:18', 'Inicio Sesion'),
(308, 2, '2024-11-24 20:20:01', 'Inicio Sesion'),
(309, 2, '2024-11-24 20:20:41', 'Inicio Sesion'),
(310, 2, '2024-11-24 20:22:07', 'Inicio Sesion'),
(311, 2, '2024-11-25 10:24:32', 'Inicio Sesion'),
(312, 2, '2024-11-25 10:39:00', 'Inicio Sesion'),
(313, 2, '2024-11-25 10:41:33', 'Inicio Sesion'),
(314, 2, '2024-11-25 10:44:18', 'Inicio Sesion'),
(315, 2, '2024-11-25 10:49:33', 'Inicio Sesion'),
(316, 2, '2024-11-25 10:51:09', 'Inicio Sesion'),
(317, 2, '2024-11-25 10:55:58', 'Inicio Sesion'),
(318, 2, '2024-11-25 10:58:41', 'Inicio Sesion'),
(319, 2, '2024-11-25 11:04:21', 'Inicio Sesion'),
(320, 2, '2024-11-25 11:09:31', 'Inicio Sesion'),
(321, 2, '2024-11-25 11:15:57', 'Inicio Sesion'),
(322, 2, '2024-11-25 11:18:07', 'Inicio Sesion'),
(323, 2, '2024-11-25 11:20:38', 'Inicio Sesion'),
(324, 2, '2024-11-25 11:21:19', 'Inicio Sesion'),
(325, 2, '2024-11-25 11:25:45', 'Inicio Sesion'),
(326, 2, '2024-11-25 11:28:08', 'Inicio Sesion'),
(327, 2, '2024-11-25 11:31:12', 'Inicio Sesion'),
(328, 2, '2024-11-25 11:47:05', 'Inicio Sesion'),
(329, 2, '2024-11-25 11:50:26', 'Inicio Sesion'),
(330, 2, '2024-11-25 11:55:15', 'Inicio Sesion'),
(331, 2, '2024-11-25 11:58:38', 'Inicio Sesion'),
(332, 2, '2024-11-25 11:59:30', 'Inicio Sesion'),
(333, 2, '2024-11-25 12:02:16', 'Inicio Sesion'),
(334, 2, '2024-11-25 12:03:19', 'Inicio Sesion'),
(335, 2, '2024-11-25 12:06:19', 'Inicio Sesion'),
(336, 2, '2024-11-25 12:07:00', 'Inicio Sesion'),
(337, 2, '2024-11-25 12:39:38', 'Inicio Sesion'),
(338, 2, '2024-11-25 12:40:15', 'Inicio Sesion'),
(339, 2, '2024-11-25 12:40:58', 'Inicio Sesion'),
(340, 2, '2024-11-25 12:42:30', 'Inicio Sesion'),
(341, 2, '2024-11-25 12:43:01', 'Inicio Sesion'),
(342, 2, '2024-11-25 12:50:52', 'Inicio Sesion'),
(343, 2, '2024-11-25 12:54:27', 'Inicio Sesion'),
(344, 2, '2024-11-25 12:56:00', 'Inicio Sesion'),
(345, 2, '2024-11-25 12:58:43', 'Inicio Sesion'),
(346, 2, '2024-11-25 13:01:11', 'Inicio Sesion'),
(347, 2, '2024-11-25 13:05:23', 'Inicio Sesion'),
(348, 2, '2024-11-25 13:06:53', 'Inicio Sesion'),
(349, 2, '2024-11-25 13:09:38', 'Inicio Sesion'),
(350, 2, '2024-11-25 13:11:54', 'Inicio Sesion'),
(351, 2, '2024-11-25 13:13:13', 'Inicio Sesion'),
(352, 2, '2024-11-26 12:22:23', 'Inicio Sesion'),
(353, 2, '2024-11-26 12:26:58', 'Inicio Sesion'),
(354, 2, '2024-11-26 12:28:47', 'Creo un Usuario'),
(355, 2, '2024-11-26 12:30:06', 'Inicio Sesion'),
(356, 2, '2024-11-26 12:47:17', 'Inicio Sesion'),
(357, 2, '2024-11-26 12:48:38', 'Inicio Sesion'),
(358, 2, '2024-11-26 12:50:09', 'Inicio Sesion'),
(359, 2, '2024-11-26 12:55:33', 'Inicio Sesion'),
(360, 2, '2024-11-26 12:56:54', 'Inicio Sesion'),
(361, 2, '2024-11-26 12:58:51', 'Inicio Sesion'),
(362, 2, '2024-11-26 12:59:52', 'Inicio Sesion'),
(363, 2, '2024-11-26 13:00:19', 'Inicio Sesion'),
(364, 2, '2024-11-26 13:05:45', 'Inicio Sesion'),
(365, 2, '2024-11-26 13:06:42', 'Inicio Sesion'),
(366, 2, '2024-11-26 13:07:22', 'Inicio Sesion'),
(367, 2, '2024-11-26 13:09:02', 'Inicio Sesion'),
(368, 2, '2024-11-26 15:51:47', 'Inicio Sesion'),
(369, 2, '2024-11-27 08:55:23', 'Inicio Sesion'),
(370, 2, '2024-11-27 09:04:54', 'Inicio Sesion'),
(371, 2, '2024-11-27 09:08:41', 'Inicio Sesion'),
(372, 2, '2024-11-27 09:16:10', 'Inicio Sesion'),
(373, 2, '2024-11-27 09:18:21', 'Inicio Sesion'),
(374, 2, '2024-11-27 09:34:42', 'Inicio Sesion'),
(375, 2, '2024-11-27 09:35:14', 'Creo un Usuario'),
(376, 6, '2024-11-27 09:52:39', 'Inicio Sesion'),
(377, 6, '2024-11-27 09:58:38', 'Creo una Pelicula'),
(378, 6, '2024-11-27 09:59:42', 'Agrego una Funcion'),
(379, 6, '2024-11-27 09:59:59', 'Vendio una Entrada/s'),
(380, 2, '2024-11-27 10:05:57', 'Inicio Sesion'),
(381, 2, '2024-11-27 10:07:22', 'Creo una Pelicula'),
(382, 2, '2024-11-27 10:08:11', 'Elimino una Pelicula'),
(383, 6, '2024-11-27 10:09:01', 'Inicio Sesion'),
(384, 6, '2024-11-27 10:13:41', 'Creo una Pelicula'),
(385, 6, '2024-11-27 10:14:04', 'Agrego una Funcion'),
(386, 6, '2024-11-27 10:14:32', 'Vendio una Entrada/s'),
(387, 2, '2024-11-27 10:16:24', 'Inicio Sesion'),
(388, 6, '2024-11-27 10:32:49', 'Inicio Sesion'),
(389, 6, '2024-11-27 10:36:27', 'Inicio Sesion'),
(390, 2, '2024-11-27 10:37:32', 'Inicio Sesion'),
(391, 6, '2024-11-27 10:37:49', 'Inicio Sesion'),
(392, 6, '2024-11-27 10:39:05', 'Inicio Sesion'),
(393, 6, '2024-11-27 10:40:14', 'Inicio Sesion'),
(394, 6, '2024-11-27 10:44:00', 'Inicio Sesion'),
(395, 6, '2024-11-27 10:50:06', 'Inicio Sesion'),
(396, 6, '2024-11-27 10:53:47', 'Inicio Sesion'),
(397, 6, '2024-11-27 10:54:39', 'Inicio Sesion'),
(398, 6, '2024-11-27 10:58:28', 'Inicio Sesion'),
(399, 6, '2024-11-27 10:59:52', 'Inicio Sesion'),
(400, 6, '2024-11-27 11:01:58', 'Inicio Sesion'),
(401, 6, '2024-11-27 11:03:49', 'Inicio Sesion'),
(402, 6, '2024-11-27 11:05:13', 'Inicio Sesion'),
(403, 2, '2024-11-27 11:07:31', 'Inicio Sesion'),
(404, 2, '2024-11-27 11:07:52', 'Modifico Una Pelicula'),
(405, 2, '2024-11-27 11:08:14', 'Agrego una Funcion'),
(406, 2, '2024-11-27 11:09:33', 'Vendio una Entrada/s'),
(407, 6, '2024-11-27 11:17:44', 'Inicio Sesion'),
(408, 6, '2024-11-27 11:18:15', 'Inicio Sesion'),
(409, 6, '2024-11-27 11:18:45', 'Inicio Sesion'),
(410, 6, '2024-11-27 11:23:51', 'Inicio Sesion'),
(411, 6, '2024-11-27 11:28:48', 'Inicio Sesion'),
(412, 6, '2024-11-27 11:29:17', 'Modifico un Usuario'),
(413, 6, '2024-11-27 11:29:32', 'Inicio Sesion'),
(414, 2, '2024-11-27 11:30:11', 'Inicio Sesion'),
(415, 2, '2024-11-27 11:30:55', 'Creo un Usuario'),
(416, 9, '2024-11-27 11:31:38', 'Inicio Sesion'),
(417, 2, '2024-11-27 11:36:16', 'Inicio Sesion'),
(418, 2, '2024-11-27 11:46:23', 'Inicio Sesion'),
(419, 2, '2024-11-27 11:48:29', 'Inicio Sesion'),
(420, 2, '2024-11-27 11:54:10', 'Inicio Sesion'),
(421, 2, '2024-11-27 11:54:43', 'Modifico un Usuario'),
(422, 2, '2024-11-27 11:55:04', 'Modifico un Usuario'),
(423, 2, '2024-11-27 11:55:12', 'Modifico un Usuario'),
(424, 2, '2024-11-27 11:55:22', 'Modifico un Usuario'),
(425, 9, '2024-11-27 11:56:35', 'Inicio Sesion'),
(426, 9, '2024-11-27 11:56:46', 'Modifico un Usuario'),
(427, 9, '2024-11-27 11:56:57', 'Modifico un Usuario'),
(428, 6, '2024-11-27 12:01:17', 'Inicio Sesion'),
(429, 8, '2024-11-27 12:03:15', 'Inicio Sesion'),
(430, 8, '2024-11-27 12:03:55', 'Inicio Sesion'),
(431, 8, '2024-11-27 12:04:25', 'Modifico un Usuario'),
(432, 8, '2024-11-27 12:04:37', 'Modifico un Usuario'),
(433, 6, '2024-11-27 12:05:49', 'Inicio Sesion'),
(434, 6, '2024-11-27 12:06:04', 'Modifico un Usuario'),
(435, 2, '2024-11-27 12:22:31', 'Inicio Sesion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculagenero`
--

CREATE TABLE `peliculagenero` (
  `IdPelicula` int(11) DEFAULT NULL,
  `IdGenero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `peliculagenero`
--

INSERT INTO `peliculagenero` (`IdPelicula`, `IdGenero`) VALUES
(NULL, 7),
(NULL, 8),
(NULL, 9),
(NULL, 10),
(NULL, 8),
(NULL, 10),
(NULL, 11),
(NULL, 12),
(NULL, 7),
(NULL, 9),
(5, 1),
(5, 8),
(NULL, 2),
(NULL, 5),
(NULL, 16),
(6, 2),
(6, 8),
(6, 16),
(9, 2),
(9, 3),
(10, 1),
(10, 2),
(10, 3),
(10, 16),
(NULL, 12),
(12, 4),
(12, 8),
(12, 18),
(8, 6),
(8, 8),
(8, 13),
(8, 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `IdPelicula` int(11) NOT NULL,
  `NombrePelicula` varchar(255) DEFAULT NULL,
  `Resumen` text DEFAULT NULL,
  `Imagen` varchar(100) DEFAULT NULL,
  `PaisOrigen` varchar(100) DEFAULT NULL,
  `FechaEstrenoMundial` date DEFAULT NULL,
  `FechaInicio` date DEFAULT NULL,
  `FechaFin` date DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL,
  `Clasificacion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`IdPelicula`, `NombrePelicula`, `Resumen`, `Imagen`, `PaisOrigen`, `FechaEstrenoMundial`, `FechaInicio`, `FechaFin`, `Duracion`, `Clasificacion`) VALUES
(5, 'Top Gun: Maverick', 'Después de más de treinta años de servicio como uno de los mejores aviadores de la Marina, Pete \"Maverick\" Mitchell sigue rompiendo los límites como un valiente piloto de pruebas, eludiendo el avance de rango que lo apartaría de volar. Cuando se encuentra entrenando a un destacamento de graduados de Top Gun para una misión especializada, Maverick debe confrontar los fantasmas de su pasado y sus miedos más profundos.', 'Top Gun: Maverick-2024-11-11_10-54-55.jpg', 'Estados Unidos', '2022-05-27', '2024-11-11', '2024-11-25', 131, '+13'),
(6, 'Interstellar', 'En un futuro donde la Tierra se enfrenta a una devastadora crisis ambiental, un grupo de astronautas emprende un viaje a través de un agujero de gusano recién descubierto en busca de un nuevo hogar para la humanidad. A medida que se adentran en lo desconocido, enfrentan desafíos que ponen a prueba sus límites físicos y emocionales.', 'Interstellar-2024-11-11_10-57-03.jpg', 'Estados Unidos, Reino Unido', '2014-11-05', '2024-11-11', '2024-11-29', 169, '+13'),
(8, 'El Secreto de Sus Ojos', 'Un thriller argentino dirigido por Juan José Campanella que narra la historia de Benjamín Espósito, un oficial de justicia jubilado, que decide escribir una novela basada en un brutal caso de homicidio no resuelto que investigó en su juventud. Al reabrir el caso, revive viejas pasiones y descubre oscuros secretos.', 'El Secreto de Sus Ojos-2024-11-12_20-46-17.jpg', 'Argentina', '2009-08-13', '2024-11-12', '2024-11-28', 129, '+18'),
(9, 'Gara', 'Gara', 'Gara-2024-11-20_12-27-54.jpg', 'china', '2024-11-20', '2024-11-20', '2024-11-21', 66, 'ATP'),
(10, 'Spider-Man: Into the Spider-Verse', 'Miles Morales, un adolescente de Brooklyn, se convierte en Spider-Man y se une a otras versiones de Spider-Man de diferentes dimensiones para detener una amenaza interdimensional que podría destruir el multiverso.', 'Spider-Man: Into the Spider-Verse-2024-11-27_09-58-34.jpg', 'Estados Unidos', '2024-11-27', '2024-11-27', '2024-12-18', 117, 'ATP'),
(12, 'Oppenheimer', '\"Oppenheimer\" es una película biográfica de drama y suspenso dirigida por Christopher Nolan, basada en la biografía \"Prometeo Americano\" de Kai Bird y Martin J. Sherwin. Narra la vida de J. Robert Oppenheimer, físico responsable del desarrollo de la bomba atómica durante el Proyecto Manhattan en la Segunda Guerra Mundial.', 'Oppenheimer-2024-11-27_10-13-38.jpg', 'Estados Unidos y Reino Unido', '2023-06-21', '2024-11-27', '2024-12-25', 180, '+13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salas`
--

CREATE TABLE `salas` (
  `IdSalas` int(11) NOT NULL,
  `NombreSala` varchar(45) DEFAULT NULL,
  `NumeroButacas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `salas`
--

INSERT INTO `salas` (`IdSalas`, `NombreSala`, `NumeroButacas`) VALUES
(1, 'A', 30),
(2, 'B', 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `IdUsuarios` int(11) NOT NULL,
  `NombreUsuario` varchar(100) NOT NULL,
  `Contrasena` varchar(255) NOT NULL,
  `Grupo` enum('Administrador','Empleado') NOT NULL,
  `FechaCreacion` datetime DEFAULT NULL,
  `FechaModificacion` datetime DEFAULT NULL,
  `FechaUltimoAcceso` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`IdUsuarios`, `NombreUsuario`, `Contrasena`, `Grupo`, `FechaCreacion`, `FechaModificacion`, `FechaUltimoAcceso`) VALUES
(2, 'leo', '3c4db4b1f809dd408df358e14aacb671b7c20a905726bc04545af2342febda8c2078be238690d82a4dbd5a0b1b130e33', 'Administrador', '2024-11-04 09:57:51', '2024-11-27 12:04:25', '2024-11-27 12:22:31'),
(6, 'pola', '24903e18e15bd6b591c9a89f9f6706810051ab37f8d79d8fde44410df7de3ca013df03d1b6823e40a9bbbcf3b5686847', 'Empleado', '2024-11-24 17:32:56', '2024-11-27 12:06:04', '2024-11-27 12:05:49'),
(7, 'juan', 'ef7a07e388f9aedaeb3a564d6b5ba4a3689dcfb0ee028ca4e2495e1fccb71547974ccbad9872cd9e3312c6e46ff273b9', 'Administrador', '2024-11-26 12:28:45', NULL, NULL),
(8, 'leo4', 'ab920b7db64ff9738d96be50e95f9c0c3ae00b98167a57895d279cad9561515fd2c5dfb8b6e9a7e28ff4f3c841e7b317', 'Administrador', '2024-11-27 09:35:12', NULL, '2024-11-27 12:03:55'),
(9, 'karen', 'f4ec3b200bb502138931668db10176f873374f58455e852294ed29edc8590f2e8b8ca0453c5e9761d1c18b8f7198a6bf', 'Empleado', '2024-11-27 11:30:55', '2024-11-27 12:04:37', '2024-11-27 11:56:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventaboletos`
--

CREATE TABLE `ventaboletos` (
  `IdVenta` int(11) NOT NULL,
  `IdFuncion` int(11) DEFAULT NULL,
  `IdUsuario` int(11) DEFAULT NULL,
  `Fecha_hora` datetime DEFAULT NULL,
  `NumeroButaca` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventaboletos`
--

INSERT INTO `ventaboletos` (`IdVenta`, `IdFuncion`, `IdUsuario`, `Fecha_hora`, `NumeroButaca`) VALUES
(1, NULL, 2, '2024-11-04 10:12:10', 14),
(2, NULL, 2, '2024-11-04 10:12:10', 15),
(3, NULL, 2, '2024-11-04 10:12:10', 16),
(4, NULL, 2, '2024-11-04 10:12:10', 20),
(5, NULL, 2, '2024-11-04 10:12:10', 21),
(6, NULL, 2, '2024-11-04 10:12:10', 22),
(7, NULL, 2, '2024-11-04 10:12:10', 23),
(8, 2, 2, '2024-11-04 18:39:11', 1),
(9, 2, 2, '2024-11-04 18:39:11', 2),
(10, 2, 2, '2024-11-04 18:39:11', 3),
(11, 2, 2, '2024-11-04 18:39:11', 4),
(12, 2, 2, '2024-11-04 18:39:11', 5),
(13, 2, 2, '2024-11-04 18:39:11', 6),
(14, 2, 2, '2024-11-04 18:39:11', 7),
(15, 2, 2, '2024-11-04 18:39:11', 8),
(16, 2, 2, '2024-11-04 18:39:11', 9),
(17, 2, 2, '2024-11-04 18:39:11', 10),
(18, 2, 2, '2024-11-04 18:39:11', 11),
(19, 2, 2, '2024-11-04 18:39:11', 12),
(20, 2, 2, '2024-11-04 18:39:11', 13),
(21, 2, 2, '2024-11-04 18:39:11', 14),
(22, 2, 2, '2024-11-04 18:39:11', 15),
(23, 2, 2, '2024-11-04 18:39:11', 16),
(24, 2, 2, '2024-11-04 18:39:11', 17),
(25, 2, 2, '2024-11-04 18:39:11', 18),
(26, 2, 2, '2024-11-04 18:39:22', 19),
(27, 2, 2, '2024-11-04 18:39:22', 20),
(28, 2, 2, '2024-11-04 18:39:22', 21),
(29, 2, 2, '2024-11-04 18:39:22', 22),
(30, 2, 2, '2024-11-04 18:39:22', 23),
(31, 2, 2, '2024-11-04 18:39:22', 24),
(32, 2, 2, '2024-11-04 18:39:22', 25),
(33, 2, 2, '2024-11-04 18:39:22', 26),
(34, 2, 2, '2024-11-04 18:39:22', 27),
(35, 2, 2, '2024-11-04 18:39:22', 28),
(36, 2, 2, '2024-11-04 18:39:22', 29),
(37, 2, 2, '2024-11-04 18:39:22', 30),
(38, 4, 2, '2024-11-06 16:34:54', 8),
(39, 4, 2, '2024-11-06 16:34:54', 9),
(40, 4, 2, '2024-11-06 16:34:54', 10),
(41, 4, 2, '2024-11-06 16:34:54', 11),
(42, 4, 2, '2024-11-06 16:34:54', 13),
(43, 4, 2, '2024-11-06 16:34:54', 14),
(44, 4, 2, '2024-11-06 16:34:54', 15),
(45, 4, 2, '2024-11-06 16:34:54', 16),
(46, 4, 2, '2024-11-06 16:34:54', 19),
(47, 4, 2, '2024-11-06 16:34:54', 20),
(48, 4, 2, '2024-11-06 16:34:54', 21),
(49, 4, 2, '2024-11-06 16:34:54', 22),
(50, 4, 2, '2024-11-06 16:34:54', 23),
(51, 5, 2, '2024-11-06 16:35:03', 11),
(52, 5, 2, '2024-11-06 16:35:03', 12),
(53, 5, 2, '2024-11-06 16:35:03', 17),
(54, 5, 2, '2024-11-06 16:35:03', 18),
(55, 5, 2, '2024-11-06 16:35:03', 23),
(56, 5, 2, '2024-11-06 16:35:03', 24),
(57, 7, 2, '2024-11-11 11:04:43', 9),
(58, 7, 2, '2024-11-11 11:04:43', 10),
(59, 7, 2, '2024-11-11 11:04:43', 11),
(60, 7, 2, '2024-11-11 11:04:43', 12),
(61, 7, 2, '2024-11-11 11:04:43', 15),
(62, 7, 2, '2024-11-11 11:04:43', 16),
(63, 7, 2, '2024-11-11 11:04:43', 17),
(64, 7, 2, '2024-11-11 11:04:43', 18),
(65, 7, 2, '2024-11-11 11:04:57', 8),
(66, 7, 2, '2024-11-11 11:04:57', 14),
(67, 7, 2, '2024-11-11 11:04:57', 20),
(68, 7, 2, '2024-11-11 11:04:57', 21),
(69, 7, 2, '2024-11-11 11:04:57', 22),
(70, 6, 2, '2024-11-11 11:07:30', 10),
(71, 6, 2, '2024-11-11 11:07:30', 11),
(72, 6, 2, '2024-11-11 11:07:30', 16),
(73, 6, 2, '2024-11-11 11:07:30', 17),
(74, 7, 2, '2024-11-11 11:07:53', 23),
(75, 6, 2, '2024-11-11 11:12:07', 15),
(76, 7, 2, '2024-11-11 11:12:19', 3),
(77, 6, 2, '2024-11-11 11:16:05', 9),
(78, 7, 2, '2024-11-11 11:16:32', 1),
(79, 7, 2, '2024-11-11 11:16:32', 7),
(80, 7, 2, '2024-11-11 11:16:32', 13),
(81, 7, 2, '2024-11-11 11:16:32', 19),
(82, 7, 2, '2024-11-11 11:16:32', 24),
(83, 7, 2, '2024-11-11 11:16:32', 25),
(84, 7, 2, '2024-11-11 11:16:32', 26),
(85, 7, 2, '2024-11-11 11:16:32', 27),
(86, 7, 2, '2024-11-11 11:16:32', 28),
(87, 7, 2, '2024-11-11 11:16:32', 29),
(88, 7, 2, '2024-11-11 11:16:32', 30),
(89, 8, 2, '2024-11-12 20:52:35', 1),
(90, 8, 2, '2024-11-12 20:52:35', 2),
(91, 8, 2, '2024-11-12 20:52:35', 3),
(92, 8, 2, '2024-11-12 20:52:35', 4),
(93, 8, 2, '2024-11-12 20:52:35', 5),
(94, 8, 2, '2024-11-12 20:52:35', 6),
(95, 8, 2, '2024-11-12 20:52:35', 7),
(96, 8, 2, '2024-11-12 20:52:35', 8),
(97, 8, 2, '2024-11-12 20:52:35', 9),
(98, 8, 2, '2024-11-12 20:52:35', 10),
(99, 8, 2, '2024-11-12 20:52:35', 11),
(100, 8, 2, '2024-11-12 20:52:35', 12),
(101, 8, 2, '2024-11-12 20:52:35', 13),
(102, 8, 2, '2024-11-12 20:52:35', 14),
(103, 8, 2, '2024-11-12 20:52:35', 15),
(104, 8, 2, '2024-11-12 20:52:35', 16),
(105, 8, 2, '2024-11-12 20:52:35', 17),
(106, 8, 2, '2024-11-12 20:52:35', 18),
(107, 8, 2, '2024-11-12 20:52:35', 20),
(108, 8, 2, '2024-11-12 20:52:35', 21),
(109, 8, 2, '2024-11-12 20:52:35', 22),
(110, 8, 2, '2024-11-12 20:52:35', 23),
(111, 8, 2, '2024-11-12 20:52:35', 24),
(112, 9, 2, '2024-11-12 20:53:19', 2),
(113, 9, 2, '2024-11-12 20:53:19', 3),
(114, 9, 2, '2024-11-12 20:53:19', 4),
(115, 9, 2, '2024-11-12 20:53:19', 5),
(116, 9, 2, '2024-11-12 20:53:19', 8),
(117, 9, 2, '2024-11-12 20:53:19', 9),
(118, 9, 2, '2024-11-12 20:53:19', 10),
(119, 9, 2, '2024-11-12 20:53:19', 11),
(120, 9, 2, '2024-11-12 20:53:19', 14),
(121, 9, 2, '2024-11-12 20:53:19', 15),
(122, 9, 2, '2024-11-12 20:53:19', 16),
(123, 9, 2, '2024-11-12 20:53:19', 17),
(124, 9, 2, '2024-11-12 20:53:19', 22),
(125, 9, 2, '2024-11-12 20:53:19', 23),
(126, 9, 2, '2024-11-12 20:53:19', 24),
(127, 9, 2, '2024-11-12 20:53:19', 29),
(128, 9, 2, '2024-11-12 20:53:19', 30),
(129, 10, 2, '2024-11-20 12:09:14', 1),
(130, 10, 2, '2024-11-20 12:09:14', 2),
(131, 10, 2, '2024-11-20 12:09:14', 3),
(132, 10, 2, '2024-11-20 12:09:14', 4),
(133, 10, 2, '2024-11-20 12:09:14', 5),
(134, 10, 2, '2024-11-20 12:09:14', 6),
(135, 10, 2, '2024-11-20 12:09:14', 7),
(136, 10, 2, '2024-11-20 12:09:14', 8),
(137, 10, 2, '2024-11-20 12:09:14', 9),
(138, 10, 2, '2024-11-20 12:09:14', 10),
(139, 10, 2, '2024-11-20 12:09:14', 11),
(140, 10, 2, '2024-11-20 12:09:14', 12),
(141, 10, 2, '2024-11-20 12:09:14', 13),
(142, 10, 2, '2024-11-20 12:09:14', 14),
(143, 10, 2, '2024-11-20 12:09:14', 15),
(144, 10, 2, '2024-11-20 12:09:14', 16),
(145, 10, 2, '2024-11-20 12:09:14', 17),
(146, 10, 2, '2024-11-20 12:09:14', 18),
(147, 10, 2, '2024-11-20 12:09:14', 19),
(148, 10, 2, '2024-11-20 12:09:14', 20),
(149, 10, 2, '2024-11-20 12:09:14', 21),
(150, 10, 2, '2024-11-20 12:09:14', 22),
(151, 10, 2, '2024-11-20 12:09:14', 23),
(152, 10, 2, '2024-11-20 12:09:14', 24),
(153, 10, 2, '2024-11-20 12:09:14', 25),
(154, 10, 2, '2024-11-20 12:09:14', 26),
(155, 10, 2, '2024-11-20 12:09:14', 27),
(156, 10, 2, '2024-11-20 12:09:14', 28),
(157, 10, 2, '2024-11-20 12:09:14', 29),
(158, 10, 2, '2024-11-20 12:09:14', 30),
(159, 11, 2, '2024-11-20 12:24:34', 1),
(160, 11, 2, '2024-11-20 12:24:34', 2),
(161, 11, 2, '2024-11-20 12:24:34', 3),
(162, 11, 2, '2024-11-20 12:24:34', 4),
(163, 11, 2, '2024-11-20 12:24:34', 5),
(164, 11, 2, '2024-11-20 12:24:34', 6),
(165, 11, 2, '2024-11-20 12:24:34', 7),
(166, 11, 2, '2024-11-20 12:24:34', 8),
(167, 11, 2, '2024-11-20 12:24:34', 9),
(168, 11, 2, '2024-11-20 12:24:34', 10),
(169, 11, 2, '2024-11-20 12:24:34', 11),
(170, 11, 2, '2024-11-20 12:24:34', 12),
(171, 11, 2, '2024-11-20 12:24:34', 13),
(172, 11, 2, '2024-11-20 12:24:34', 14),
(173, 11, 2, '2024-11-20 12:24:34', 15),
(174, 11, 2, '2024-11-20 12:24:34', 16),
(175, 11, 2, '2024-11-20 12:24:34', 17),
(176, 11, 2, '2024-11-20 12:24:34', 18),
(177, 11, 2, '2024-11-20 12:24:34', 19),
(178, 11, 2, '2024-11-20 12:24:34', 20),
(179, 11, 2, '2024-11-20 12:24:34', 21),
(180, 11, 2, '2024-11-20 12:24:34', 22),
(181, 11, 2, '2024-11-20 12:24:34', 23),
(182, 11, 2, '2024-11-20 12:24:34', 24),
(183, 11, 2, '2024-11-20 12:24:34', 25),
(184, 11, 2, '2024-11-20 12:24:34', 26),
(185, 12, 2, '2024-11-20 12:31:02', 2),
(186, 12, 2, '2024-11-20 12:31:02', 3),
(187, 12, 2, '2024-11-20 12:31:02', 8),
(188, 12, 2, '2024-11-20 12:31:02', 9),
(189, 12, 2, '2024-11-20 12:31:02', 10),
(190, 12, 2, '2024-11-20 12:31:02', 11),
(191, 12, 2, '2024-11-20 12:31:36', 1),
(192, 12, 2, '2024-11-20 12:31:36', 4),
(193, 12, 2, '2024-11-20 12:31:36', 5),
(194, 12, 2, '2024-11-20 12:31:36', 6),
(195, 12, 2, '2024-11-20 12:31:36', 7),
(196, 12, 2, '2024-11-20 12:31:36', 12),
(197, 12, 2, '2024-11-20 12:31:36', 13),
(198, 12, 2, '2024-11-20 12:31:36', 14),
(199, 12, 2, '2024-11-20 12:31:36', 15),
(200, 12, 2, '2024-11-20 12:31:36', 16),
(201, 12, 2, '2024-11-20 12:31:36', 17),
(202, 12, 2, '2024-11-20 12:31:36', 18),
(203, 12, 2, '2024-11-20 12:31:36', 19),
(204, 12, 2, '2024-11-20 12:31:36', 20),
(205, 12, 2, '2024-11-20 12:31:36', 21),
(206, 12, 2, '2024-11-20 12:31:36', 22),
(207, 12, 2, '2024-11-20 12:31:36', 23),
(208, 12, 2, '2024-11-20 12:31:36', 24),
(209, 12, 2, '2024-11-20 12:31:36', 25),
(210, 12, 2, '2024-11-20 12:31:36', 26),
(211, 12, 2, '2024-11-20 12:31:36', 27),
(212, 12, 2, '2024-11-20 12:31:36', 28),
(213, 12, 2, '2024-11-20 12:31:36', 29),
(214, 12, 2, '2024-11-20 12:31:36', 30),
(215, 13, 2, '2024-11-22 11:56:05', 7),
(216, 13, 2, '2024-11-22 11:56:05', 8),
(217, 13, 2, '2024-11-22 11:56:05', 9),
(218, 13, 2, '2024-11-22 11:56:05', 10),
(219, 13, 2, '2024-11-22 11:56:05', 11),
(220, 13, 2, '2024-11-22 11:56:05', 12),
(221, 13, 2, '2024-11-22 11:56:05', 13),
(222, 13, 2, '2024-11-22 11:56:05', 14),
(223, 13, 2, '2024-11-22 11:56:05', 15),
(224, 13, 2, '2024-11-22 11:56:05', 16),
(225, 13, 2, '2024-11-22 11:56:05', 17),
(226, 13, 2, '2024-11-22 11:56:05', 18),
(227, 13, 2, '2024-11-22 11:56:05', 20),
(228, 13, 2, '2024-11-22 11:56:05', 21),
(229, 13, 2, '2024-11-22 11:56:05', 22),
(230, 13, 2, '2024-11-22 11:56:05', 23),
(231, 13, 2, '2024-11-22 11:56:05', 24),
(232, 14, 6, '2024-11-27 09:59:58', 9),
(233, 14, 6, '2024-11-27 09:59:58', 10),
(234, 14, 6, '2024-11-27 09:59:58', 11),
(235, 14, 6, '2024-11-27 09:59:58', 12),
(236, 14, 6, '2024-11-27 09:59:58', 15),
(237, 14, 6, '2024-11-27 09:59:58', 16),
(238, 14, 6, '2024-11-27 09:59:58', 17),
(239, 14, 6, '2024-11-27 09:59:58', 18),
(240, 14, 6, '2024-11-27 09:59:58', 21),
(241, 14, 6, '2024-11-27 09:59:58', 22),
(242, 14, 6, '2024-11-27 09:59:58', 23),
(243, 14, 6, '2024-11-27 09:59:58', 24),
(244, 15, 6, '2024-11-27 10:14:31', 1),
(245, 15, 6, '2024-11-27 10:14:31', 2),
(246, 15, 6, '2024-11-27 10:14:31', 3),
(247, 15, 6, '2024-11-27 10:14:31', 4),
(248, 15, 6, '2024-11-27 10:14:31', 5),
(249, 15, 6, '2024-11-27 10:14:31', 6),
(250, 15, 6, '2024-11-27 10:14:31', 7),
(251, 15, 6, '2024-11-27 10:14:31', 8),
(252, 15, 6, '2024-11-27 10:14:31', 9),
(253, 15, 6, '2024-11-27 10:14:31', 10),
(254, 15, 6, '2024-11-27 10:14:31', 11),
(255, 15, 6, '2024-11-27 10:14:31', 12),
(256, 15, 6, '2024-11-27 10:14:31', 13),
(257, 15, 6, '2024-11-27 10:14:31', 14),
(258, 15, 6, '2024-11-27 10:14:31', 15),
(259, 15, 6, '2024-11-27 10:14:31', 16),
(260, 15, 6, '2024-11-27 10:14:31', 17),
(261, 15, 6, '2024-11-27 10:14:31', 18),
(262, 15, 6, '2024-11-27 10:14:31', 19),
(263, 15, 6, '2024-11-27 10:14:31', 20),
(264, 15, 6, '2024-11-27 10:14:31', 21),
(265, 15, 6, '2024-11-27 10:14:31', 22),
(266, 15, 6, '2024-11-27 10:14:31', 23),
(267, 15, 6, '2024-11-27 10:14:31', 24),
(268, 15, 6, '2024-11-27 10:14:31', 25),
(269, 15, 6, '2024-11-27 10:14:31', 26),
(270, 15, 6, '2024-11-27 10:14:31', 27),
(271, 15, 6, '2024-11-27 10:14:31', 28),
(272, 15, 6, '2024-11-27 10:14:31', 29),
(273, 15, 6, '2024-11-27 10:14:31', 30),
(274, 16, 2, '2024-11-27 11:09:29', 7),
(275, 16, 2, '2024-11-27 11:09:29', 8),
(276, 16, 2, '2024-11-27 11:09:29', 9),
(277, 16, 2, '2024-11-27 11:09:29', 10),
(278, 16, 2, '2024-11-27 11:09:29', 11),
(279, 16, 2, '2024-11-27 11:09:29', 12),
(280, 16, 2, '2024-11-27 11:09:29', 13),
(281, 16, 2, '2024-11-27 11:09:29', 14),
(282, 16, 2, '2024-11-27 11:09:29', 15),
(283, 16, 2, '2024-11-27 11:09:29', 16),
(284, 16, 2, '2024-11-27 11:09:29', 17),
(285, 16, 2, '2024-11-27 11:09:29', 18),
(286, 16, 2, '2024-11-27 11:09:29', 19),
(287, 16, 2, '2024-11-27 11:09:29', 20),
(288, 16, 2, '2024-11-27 11:09:29', 21),
(289, 16, 2, '2024-11-27 11:09:29', 22),
(290, 16, 2, '2024-11-27 11:09:29', 23),
(291, 16, 2, '2024-11-27 11:09:29', 24);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD PRIMARY KEY (`IdFunciones`),
  ADD KEY `fk_idPelicula_idx` (`IdPelicula`),
  ADD KEY `fk_idSala_idx` (`IdSala`);

--
-- Indices de la tabla `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`IdGeneros`);

--
-- Indices de la tabla `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`IdHistorial`),
  ADD KEY `usuarios_fk_idx` (`IdUsuario`);

--
-- Indices de la tabla `peliculagenero`
--
ALTER TABLE `peliculagenero`
  ADD KEY `fk_IdPelicula_idx` (`IdPelicula`),
  ADD KEY `generos_fk_idx` (`IdGenero`);

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`IdPelicula`);

--
-- Indices de la tabla `salas`
--
ALTER TABLE `salas`
  ADD PRIMARY KEY (`IdSalas`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`IdUsuarios`);

--
-- Indices de la tabla `ventaboletos`
--
ALTER TABLE `ventaboletos`
  ADD PRIMARY KEY (`IdVenta`),
  ADD KEY `fk_usuarios_idx` (`IdUsuario`),
  ADD KEY `fk_funciones_idx` (`IdFuncion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `funciones`
--
ALTER TABLE `funciones`
  MODIFY `IdFunciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `generos`
--
ALTER TABLE `generos`
  MODIFY `IdGeneros` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `IdHistorial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=436;

--
-- AUTO_INCREMENT de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `IdPelicula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `salas`
--
ALTER TABLE `salas`
  MODIFY `IdSalas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `IdUsuarios` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `ventaboletos`
--
ALTER TABLE `ventaboletos`
  MODIFY `IdVenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=292;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD CONSTRAINT `fk_idPelicula` FOREIGN KEY (`IdPelicula`) REFERENCES `peliculas` (`IdPelicula`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_idSala` FOREIGN KEY (`IdSala`) REFERENCES `salas` (`IdSalas`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `historial`
--
ALTER TABLE `historial`
  ADD CONSTRAINT `usuarios_fk` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`IdUsuarios`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `peliculagenero`
--
ALTER TABLE `peliculagenero`
  ADD CONSTRAINT `generos_fk` FOREIGN KEY (`IdGenero`) REFERENCES `generos` (`IdGeneros`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `peliculas_fk` FOREIGN KEY (`IdPelicula`) REFERENCES `peliculas` (`IdPelicula`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `ventaboletos`
--
ALTER TABLE `ventaboletos`
  ADD CONSTRAINT `fk_funciones` FOREIGN KEY (`IdFuncion`) REFERENCES `funciones` (`IdFunciones`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_usuarios` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`IdUsuarios`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
